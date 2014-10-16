#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

UNPROCESSED_BUMP = False

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
    global UNPROCESSED_BUMP
    UNPROCESSED_BUMP = True
    

def roomba():
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist)
    rospy.init_node('roomber', anonymous=True)
    rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback)
    twist = Twist()
    r = rospy.Rate(3)
    while not rospy.is_shutdown():
        global UNPROCESSED_BUMP
        if UNPROCESSED_BUMP:
            UNPROCESSED_BUMP = False
            twist.linear.x = -0.7
            twist.angular.z = 1.5
        else:
            twist.linear.x = 0.3
            twist.angular.z = 0.0
        pub.publish(twist)
        "rospy.loginfo(twist)"
        r.sleep()
        
if __name__ == '__main__':
    try:
        roomba()
    except rospy.ROSInterruptException: pass


#  * /mobile_base/events/bumper [kobuki_msgs/BumperEvent]
