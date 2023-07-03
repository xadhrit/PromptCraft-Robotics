Prompt = "I need you to find me a object. Objects might be scattered around the scene, so if you don't find it right away , a good strategy is to turn "

def search_for_bottle():
    num_turns = 4 #turn around 4 times to look for the bottle 
    for i in range(num_turns):
        turn_left()
        img = get_image()
        obj_list , obj_locs = detect_objects(img)
        if 'bottle' in obj_list:
            # get the coordinates of bottle in the image
            bottle_idx = obj_list.index('bottle')
            bbox = obj_locs(bottle_idx)

            # computer the center of bounding bo x 
            center_x = (bbox[0] + bbox[2]) / 2 

            center_y = (bbox[1] + bbox[3]) / 2 

            # print the center coordinates of the bottle 
            print(f"Found th bottle at ({center_x}, {center_y})")  

Prompt = "Great! Now let's say we did find hte bottle. Now I want to move towards it. The only information we have , is the location of bottle bounding box in the image. Can you give me code to make this happen?"

center_x = (bbox[0] + bbox[2]) / 2 
center_y = (bbox[1] + bbox[3]) / 2 

# compute the distance and angle to the center of the box 
img_width, img_height = img.size 
angle = math.atan2(center_x - img_width / 2, img_height / 2 - center_y)
distance = (center_x - img_width / 2) / (img_width / 2)

if abs(distance) > 0.05:
    if distance > 0:
        # bottle is the to the right, so turn right and move forward
        turn_right()
        forward()

    else:
        # bottle is to the left, so turn left and move forward
        turn_left()
        forward()

Prompt = "I want you to modualrize this code a bit. Why don't you try coming up with a few high level function and use them?"

def get_object_distance_and_angle(img, depth_img, obj_name):
    # code omitted for brevity
    pass  
def turn_towards_angle(angle):
    pass 
def search_for_object_and_move_to_it(obj_name):
    pass 

Prompt = "Now let's assume you have access to all these functions you just created. Let's get to work solving some tasks. Find our where I can warm up my lunch"

# search for a microwave
search_for_object_and_move_to_it("microwave")









