#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

zodiac_num = 0

print("卯")

def cb(message):
    global zodiac_num
    zodiac_num = message.data
    zodiac_num = zodiac_num - 1995

    while zodiac_num > 12:
        if zodiac_num > 12:
            zodiac_num = zodiac_num - 12
        elif zodiac_num <= 12:
            zodiac_num = zodiac_num

    if zodiac_num % 12 == 0:
        print("亥")
    elif zodiac_num % 11 == 0:
        print("戌")
    elif zodiac_num % 10 == 0:
        print("酉")
    elif zodiac_num % 9 == 0:
        print("申")
    elif zodiac_num % 8 == 0: 
        print("未") 
    elif zodiac_num % 7 == 0:
        print("午") 
    elif zodiac_num % 6 == 0:
        print("巳") 
    elif zodiac_num % 5 == 0:
        print("辰") 
    elif zodiac_num % 4 == 0:
        print("卯") 
    elif zodiac_num % 3 == 0:
        print("寅") 
    elif zodiac_num % 2 == 0: 
        print("丑")
    elif zodiac_num % 1 == 0:
        print("子")  

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(zodiac_num)
        rate.sleep()
    
