#!/usr/bin/env python3
# coding: utf-8
# @2022-06-16 11:24:03
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

import re
import yaml
from publicsuffixlist import PublicSuffixList

ps = PublicSuffixList(accept_unknown=False)
cdn = {}


class Colors:
    ip = '\033[92m'  # GREEN
    host = '\033[93m'  # YELLOW
    info = '\033[91m'  # RED
    reset = '\033[0m'  # RESET COLOR


def load_cdn(yml):
    cdn = yaml.load(open(yml), Loader=yaml.BaseLoader)
    # 编译成正则
    cdn = {re.compile(k): cdn[k] for k in cdn if '[' in k}
    return cdn


def fix_cdn(line: str) -> str:
    line = line.strip()
    if not line:
        return line
    if '[' in line:  # 已有 CDN 信息
        return line

    cname_list = line.split()
    # 只有首尾可能是 cname
    fix_list = [cname_list[0], cname_list[-1]]
    for i in range(len(fix_list)):
        cname = fix_list[i].rstrip('.')
        if '.' not in cname:
            continue
        tld = ps.privatesuffix(cname)
        for regex in cdn:
            if regex.match(tld):
                fix_list[i] = f'{cname}[{cdn[regex]["name"]}]'
                break

    cname_list[0] = fix_list[0]
    cname_list[-1] = fix_list[1]
    return ' '.join(cname_list)


def colour_print(line: str) -> None:
    if not line:
        print(line)
        return
    if '[' not in line:
        print(line)
        return
    for i in line.split('['):
        host = i.split()[-1]
        if '.' in host:
            line = line.replace(host, colour_host(host))
        if ']' in i:
            info = i.split(']')[0]
            line = line.replace(info, colour_info(info))
    print(line)


def colour_host(host: str) -> str:
    colour = Colors.ip
    if ps.privatesuffix(host):
        colour = Colors.host
    return f'{colour}{host}{Colors.reset}'


def colour_info(text: str) -> str:
    colour = Colors.info
    return f'{colour}{text}{Colors.reset}'


if __name__ == '__main__':
    import sys
    import os
    cdn = load_cdn(os.path.expanduser('~/.nali/cdn.yml'))

    for line in sys.stdin:
        line = fix_cdn(line)
        colour_print(line)
