<!--
2020-08-14 16:20:38
https://ae01.alicdn.com/kf/H096aac2dd76541a4a00a405e6ed8d67eN.png
python
原生logging架构学习
logging使用最多，学习下
可以综合Golong中的logrus看看，我到是觉得那种日志输出很舒服
-->

## 原生logging架构学习

> 可以综合Golong中的logrus看看，我到是觉得那种日志输出很舒服

不要直接实例化日志，而应该通过`logging.getLogger(__name__)`这种方式来获取模块级的日志记录器，多次使用相同的名字调用，
会一只返回相同的Logger对象的引用，这里的name一般最好是句点分割，所以此处可以这样使用

#### 日志写到文件
需要先配置好`logging.basicConfig`，该配置是一次性配置，只有第一次调用会进行操作，后续调用将不会有效
- filename: 定义日志输出文件
- level: 定义日志等级
- filemode: 定义日志文件的写方式，如‘w’表示重新写
- format: 日志输出格式
    - asctime: 日志输出格式，默认格式为`2020-12-12 11:11:11,123`
        - RFC 3339
    - datefmt: 日志中对asctime的补充，可以自定义日期的格式
    - levelname: 日志等级
    - message: 日志消息


