# JH_obstacle-avoiding-robot
This repository contains the code needed to run a robot that avoids colliding with obstacles in its path.

The complete procedure of making this robot can be found on - https://sites.google.com/site/projectsriza/obstacle-avoiding-robot

Sensors - The robot uses 2 IR sensors that are placed at each edge of the robot. These sensors detect any obstacles in their path according to which the robot changes its direction of movement.
	  
The Brain - The movement of robot is random and primarily focuses on avoiding collision with obstacles. The different cases involved in this project are discussed on the mentioned above. If the robot finds an obstacle on the right, it moves to left. If an obstacle is found on left, the direction is changed to right. If obstacle is found on both ends, the robot turns right/left randomly then checks for obstacles again, if found again on both ends, the robot takes a U-turn and then a 90 degree turn in the same direction if obstacles were found on both ends after taking a U-turn.
