<!--
2020-07-31 10:13:21
https://ae01.alicdn.com/kf/H096aac2dd76541a4a00a405e6ed8d67eN.png
nginx
nginx学习
nginx官网学习
学习参考：https://www.nginx.cn/doc/
-->

## nginx学习

> nginx官网学习，参考：https://www.nginx.cn/doc/

在 win10 上要实现挂载，首先需要在 settings 进行相关的配置
```nginx
alias  # 为 location 中的路由分配一个新的路径
root /web  # 指定工作路径
error_page 404 /web/error_page/404.html;
limit_except GET {
    allow  192.168.0.0/32;
    deny  all;
}

log_format gzip '$remote_addr - $remote_user [$time_local]  '  # 日志格式
access_log /web/log  # 日志输出路径
```


```nginx
http {
    server {
        listen  80;
        server_name  www.xyz.com;
        access_log  /web/log/nginx.log main;
        location / {
            index  index.html;
            root  
        }
    }
}

```
