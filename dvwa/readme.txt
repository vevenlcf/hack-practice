初始化dvwa平台：

1、初始化docker
yum install docker
service docker restart

2、安装dvwa漏洞平台 （https://hub.docker.com/r/citizenstig/dvwa/）
docker pull citizenstig/dvwa
docker run -d -p 80:80 citizenstig/dvwa

http://172.16.8.95/login.php  （用户名：admin  、 密码：password）

3、降低安全等级  否则注入不一定成功
