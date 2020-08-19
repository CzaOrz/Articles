<!--
2020-08-19 16:53:43
https://ae01.alicdn.com/kf/H6afaf3902644461a866e1e09bf6004480.png
工具
jmeter使用
jmeter的一些常用指令学习
jmeter的一些常用指令学习
-->

## jmeter使用

> jmeter的一些常用指令学习

启动指令的使用
```
nohup /opt/apache-jmeter-5.2/bin/jmeter-server -Djava.rmi.server.hostname=10.251.250.80 > Log.log 2>&1 &
jmeter -n -t baidu_requests_results.jmx -r -l baidu_requests_results.jtl -e -o /home/tester/apache-jmeter-3.0/resultReport
```

#### 随机工具的使用  
点击option选项，选择语言为中文，然后点击tools，点击函数对话框助手即可
