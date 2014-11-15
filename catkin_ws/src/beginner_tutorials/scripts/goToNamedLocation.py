#! /usr/bin/env python
from gotoClient import goto
import sys
import rospy
# goToNamedLocation.py NAME

def goToNamedLocation(location): 
    rospy.init_node("goToNamedLocationNode")

    # create an interactive marker server on the topic namespace simple_marker

    f = open('../Marker_Location.txt','r')
    for line in f:
        arr = line.split()
        if (arr[2] == location):
            goto(float(arr[0]), float(arr[1]))

if __name__=="__main__":
   goToNamedLocation(sys.argv[1])


