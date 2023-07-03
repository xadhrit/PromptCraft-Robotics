"""
Write a python script that execute a visual servoing approach towards catching a basketball in a court. 
"""

import cv2 
import numpy as np 

def get_image(object_name):
    pass 


def detect_ball(frame):
    # Convert the image to HSV color space for better color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define the range of orange color in HSV
    lower_orange = np.array([10,100,100])
    upper_orange = np.array([30,255, 255])
    # threshold the image to get only the orange color 
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    #find the contours of the threshold image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # if a contour is found, return its center 
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea) 
        M = cv2.moments(c)
        if M["m00"] > 0: 
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            return center 
    return None

def catch_ball():
    ## Continuosly get images from the camera
    while True:
        frame = get_image()
        # detect the ball in the image
        ball_center = detect_ball(frame)
        # if the ball is detected, move towards its location
        if ball_center is not None:
            x, y = ball_center
            robot_x, robot_y = get_location()
            vx = (x - robot_x) * 0.5 
            vy = (y - robot_y) * 0.5 
            move_by_velocity(vx, vy)

if __name__ == '__main__':
    catch_ball()
     
