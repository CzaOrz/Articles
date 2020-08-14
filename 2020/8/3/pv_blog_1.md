<!--
2020-08-03 19:03:19
https://ae01.alicdn.com/kf/H46b03db65df345d8915c1d803a9c8b16u.png
redis
快速搭建redis集群
快速搭建redis集群
快速搭建redis集群
-->

## 快速搭建redis集群

> 快速搭建redis集群

基于 docker 快速搭建 redis 主从配置
```
// 创建三个 docker 镜像服务
// 以一个容器为 master，通过 inspect 查看内网 ip
// 进入其他两个容器内部，执行 SALAVEOF hostname port
// 然后可以通过 info replication 来查看 redis 的配置情况
```

基于 docker 快速搭建 redis 哨兵配置  
```
在本地编写 sentinel.conf 配置，内容为:
sentinel monitor hostname ip port 1
然后把配置 cp 到 docker 容器内部，如: docker cp /path/to/sentinel.conf ${container}:/path/to/sentinel.conf
然后在容器内部执行 redis-senticel /path/to/sentinel.conf

哨兵一般是单独再启动的，也可以在已有 redis 服务的机器上继续启动
BGSAVE
sdown
odown
quonum
```

