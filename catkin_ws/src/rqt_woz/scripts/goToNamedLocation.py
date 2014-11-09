#! /usr/bin/env python
from gotoClient import goto
import sys
import rospy
# goToNamedLocation.py NAME
if __name__=="__main__":
    rospy.init_node("goToNamedLocationNode")

    # create an interactive marker server on the topic namespace simple_marker

    location = sys.argv[1]
    f = open('../Marker_Location.txt','r')
    for line in f:
        arr = line.split()
        if (arr[2] == location):
            goto(float(arr[0]), float(arr[1]))