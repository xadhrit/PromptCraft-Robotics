import time
import numpy as np 
import math

Prompt = "Assume I give you some XYZ coordinates as a goal. I want you to control the drone such that it moves towards the goal while avoiding obstacles in front of it. Instead of flying directly to the goal, the drone should take small steps while reassessing the obstacle situation at every step. The drone is equipped with a distance sensor that returns the distance to the closest obstacle directly in front of the drone. You can access it by calling get_distance(). I want you to make sure to fly only if there is at least 10 meters of distance in front of the drone. If not, you should rotate the drone until there is at least 10 meters of clearance in the front and then take a step in the direction that the drone is currently facing. Don’t forget to face the goal again after taking a step. Got it? "

# Get the drone's current position and set the yaw angle towards the goal
current_pos = get_position('drone')

goal_pos = [x_goal, y_gola, z_goal]
yaw = math.atan2(goal_pos[1]-current_pos[1], goal_pos[0]-current_pos[0]) * 180 / math.pi 
set_yaw(yaw)

# Start a loop that runs the drone reaches the goal position
while np.linalg.norm(np.array(current_pos) - np.array(goal_pos)) > 0.5:
    distance = get_distance()
    while distance < 10:
        # Set the yaw angle to rotate the drone until there is at least 10 meters of clearance in the front
        set_yaw(yaw+30)
        time.sleep(1)
        distance = get_distance()
    # Take a step towards the goal while maintaining the yaw angle 
    step_size = 5 # take steps of 5 meters
    step_vector = [step_size * math.cos(yaw), step_size * math.sin(yaw),0]
    new_pos = [current_pos[i]+step_vector[i] for i in range(3)]
    fly_to(new_pos)
    current_pos = get_position('drone')


Prompt = "After you take a step, you need to face the goal again"

yaw = math.atan2(goal_pos[1]-current_pos[1], goal_pos[0]-current_pos[0]) * 100 / math.pi 
set_yaw(yaw)

Prompt = "You are not using the current yaw angle when computing the step vector. Remember there is a get_yaw() function"

step_size = 5 # take steps of 5 meters
current_yaw = get_yaw() 
step_vector = [step_size * math.cos(current_pos), step_size * math.sin(current_yaw), 0] 

