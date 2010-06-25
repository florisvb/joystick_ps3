#!/usr/bin/env python
import roslib; roslib.load_manifest('joystick_ps3')
import rospy
from joystick_ps3.msg import ps3values
from joy.msg import Joy
import time


class Listener:
    def __init__(self):
        self.msg = None
        rospy.Subscriber("joy", Joy, self.callback)
        self.pub = rospy.Publisher("ps3_interpreter", ps3values)
        rospy.init_node('ps3_interpreter', anonymous=True)
        self.run()

    def callback(self, Joy):
        
        self.msg = ps3values(   joyleft_x = Joy.axes[0]*-1.,
                                joyleft_y = Joy.axes[1]*-1,
                                joyright_x = Joy.axes[2]*-1.,
                                joyright_y = Joy.axes[3]*-1,
                                up = Joy.buttons[4],
                                down = Joy.buttons[6],
                                left = Joy.buttons[7],
                                right = Joy.buttons[5],
                                triangle = Joy.buttons[12],
                                x = Joy.buttons[14],
                                square = Joy.buttons[15],
                                circle = Joy.buttons[13],
                                select = Joy.buttons[0],
                                start = Joy.buttons[3],
                                playstation = Joy.buttons[16],
                                L1 = Joy.buttons[10],
                                L2 = Joy.axes[12],
                                R1 = Joy.buttons[11],
                                R2 = Joy.axes[13])

    
    def run(self):
        
        r = rospy.Rate(40) # 40hz
        while not rospy.is_shutdown():
            try:
                self.pub.publish(self.msg)
            except:
                pass
            r.sleep()

        
        
    

if __name__ == '__main__':
    listener = Listener()

