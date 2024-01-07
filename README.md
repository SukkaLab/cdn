常见 CDN 的 cname 库，配合 [https://github.com/zu1k/nali](https://github.com/zu1k/nali) 使用。

## 效果
nslookup 默认效果
```bash
nslookup www.baidu.com 114.114.114.114
Server:		114.114.114.114
Address:	114.114.114.114#53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com.
Name:	www.a.shifen.com
Address: 220.181.38.150
Name:	www.a.shifen.com
Address: 220.181.38.149
```

叠加 `nali` 后效果
```bash
nslookup www.baidu.com 114.114.114.114 | nali
Server:		114.114.114.114 [114DNS.COM 114DNS.COM]
Address:	114.114.114.114 [114DNS.COM 114DNS.COM] #53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com [百度旗下业务地域负载均衡系统] .
Name:	www.a.shifen.com [百度旗下业务地域负载均衡系统]
Address: 220.181.38.149 [中国 北京 北京]
Name:	www.a.shifen.com [百度旗下业务地域负载均衡系统]
Address: 220.181.38.150 [中国 北京 北京]
```

更多用法见 [https://github.com/zu1k/nali](https://github.com/zu1k/nali)
