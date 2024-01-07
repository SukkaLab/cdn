# 锐速云
- pcwaf.com
- nbwaf.com

Google 搜 pcwaf.com CDN， 在 www.pctl.hk 的快照中有 pcwaf 相关请求

https://webapi.pcwaf.com/rs/webEssayRest/getEssay?essayCode=Q3aS4Bl35INtx5BC 

几个关键点
1. API 状态码 rs000 `"code":"rs000"`

进一步发现，

> https://webapi.pcwaf.com/rs/commonRest/webBasicInfo?webDomain=www.linkstarwin.com
> https://webapi.pcwaf.com/rs/commonRest/webBasicInfo?webDomain=www.pctl.hk

2. CDN cname IP 默认 https 证书 www.rswaf.com

3. 锐速云的企业介绍中，莫名其妙出现鵬雲科技（www.pctl.hk）的介绍。https://www.ruisuyun.com/aboutus/36.html

# wcdnga.com
IP 默认 https 证书 default.chinanetcenter.com，网宿

# 方能
```bah
nslookup 7886m.com 1.1.1.1
Server:		1.1.1.1
Address:	1.1.1.1#53

Non-authoritative answer:
7886m.com	canonical name = q9uapyex-u.funnull02.vip.
q9uapyex-u.funnull02.vip	canonical name = 17f77fb7.u.fn01.vip.
17f77fb7.u.fn01.vip	canonical name = 5d97d06c3.n.fnvip100.com.
Name:	5d97d06c3.n.fnvip100.com
Address: 134.122.160.166
Name:	5d97d06c3.n.fnvip100.com
Address: 134.122.160.133
```
