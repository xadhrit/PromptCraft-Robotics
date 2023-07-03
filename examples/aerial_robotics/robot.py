"""
Inspect orchid from 3 points on a half circle
"""

import numpy as np 

# get the position of the orchid
orchid_position = self.dict_of_objects['orchid']

# define the angle range for the half-circle
angles = np.linspace(-60,-120, num=3, endpoint=False) * np.pi / 180 
# define the distance from orchid to inspect from

distance = 1.0

# define the inspection points
inspection_points = [orchid_position[:3] + [distance * np.cos(angles), distance * np.sin(angle), 0] for angle in angles]

# fly the drone to each inspection point and look at the orhid
for point in inspection_points:
    self.tello.fly_to(point + [np.arctan2(orchid_position[1] - point[1], orchid_position[0] - point[0]), orchid_position[3]])


---------------------------------------------------------------------------------

#get the position of Turbine 2 

turbine_position = get_position("Turbine 2")
# set the target position to be 12 meters away from turbine along the X-axis and 50 meters height 

target_position = [turbine_position[0] - 12, turbine_position[1], 50]
#fly the drone to the target position

fly_to(target_position)

Prompt
```
To inspect the turbine blade , I need you to fly in the bottom-right direction at an angle of -30 degrees from the horizontal axis 
You should fly in YZ plane for a distance of 30 meters, and then back to the current position
```

import math 
# get the drone's current position 
current_position = get_position("Drone") 
# Calculate the target position , which is 30 meters away in the YZ plane at an angle of -30 degree 

angle = math.radians(-30)
target_position = [
    current_position[0],
    current_position[1] + 30 * math.cos(angle)
    current_position[2] + 30 * math.cos(angle)
]

# fly the drone to the target position 

fly_to(target_position)

# fly the drone back to the current position

fly_to(current_position)