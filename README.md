# ロボットシステム学 課題2
ロボットシステム学の授業の第10回で作成したROSパッケージをベースに、オリジナリティーある改造をしてGithubに置く。
---
# 概要
ROSを用いてオリジナリティーあるシステムを作成することを目的とする。パブリッシャであるターミナル2が1999年(私の干支)から順に1年ずつ表示し、サブスクライバであるターミナル3にメッセージを引き渡す。ターミナル3は受け取った年号に応じた干支を順に表示する。
---
# 動作環境
* OS : Ubuntu 20.04 server
* Raspi : Raspberry Pi 3B+
* ROS : noetic
---
# インストール方法
```
cd ~/catkin_ws/src
git clone https://github.com/Ryo0927/robosys_ros.git
```
---
# 実行方法
```
cd ..
catkin_make
source ~/.bashrc
```
ターミナル1
```
roscore
```
ターミナル2
```
rosrun mypkg twice.py
```
ターミナル3
```
rosrun mypkg count.py
```
