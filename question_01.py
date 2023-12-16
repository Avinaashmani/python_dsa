import numpy as np
import math 

## Forward Kinematics for 3R Spatial robot ##

l0 = 0.5
l1 = 1
l2 = 0.75
l3 = 0.5


theta_1_ik = 0.0
theta_2_ik = 0.0
theta_3_ik = 0.0

def forward_kinematics():

    theta_1 = float(input("Enter Theta 1 = "))
    theta_2 = float(input("Enter Theta 2 = "))
    theta_3 = float(input("Enter Theta 3 = "))

    ## T 0 -----> 1 ##
    ## Translate (l0, z) * Rotational (theta  1, z)

    a = [[math.cos(theta_1), -math.sin(theta_1), 0, 0], 
        [math.sin(theta_1), math.cos(theta_1), 0, 0], 
        [0, 0, 1, l0], 
        [0, 0, 0, 1]]

## T 1 -----> 2 ## 
## Transalate (l1, y)

    b = [[1, 0, 0, 0],
        [0, 1, 0, l1],
        [0, 0, 1, 0], 
        [0, 0, 0, 1]]

## T  2 -----> 3 ##
## Transalate (l2, y) * Rotational (theta 2, x)

    c = [[1, 0, 0, 0], 
        [0, math.cos(theta_2), -math.sin(theta_2), l2],
        [0, math.sin(theta_2), math.cos(theta_2), 0],
        [0, 0, 0, 0]]

## T 3 -----> 4 ##
## Transalate (l3, y) * Rotational (theta 3, x)

    d = [[1, 0, 0, 0],
        [0, math.cos(theta_3), -math.sin(theta_3), l3],
        [0, math.sin(theta_3), math.cos(theta_3), 0],
        [0, 0, 0, 1]]

    result_1 = np.dot(a, b)
    result_2 = np.dot(c, d)

    ## T 0 -----> 4 ##

    result = np.dot(result_1, result_2)

    ## Columns A, B and C = Orientation 
    ## Column D = Position (x, y, z)

    print (result)

def inverse_kinematics():

    theta_1_ik = 0.0
    theta_2_ik = 0.0
    theta_3_ik = 0.0

    ## Inverse Kinematics of a 3R spatial Robot ##

    ## Theta 1 ##   

    x = float(input("Enter X Coordinate = "))
    y = float(input("Enter Y Coordinate = "))
    z = float(input("Enter Z Coordinate = "))

    theta_1_ik = math.atan2 (y, x)
    theta_2_ik = math.atan2 ((z - l1 - l0) / math.sqrt ((x ** 2) + (y ** 2)), (math.sin(theta_3_ik) / (l2 + math.cos(theta_3_ik)*l3)))
    theta_3_ik = -1*(math.cos (x**2 + y**2 + ((z - l1 - l0) ** 2) - l2**2 - l3**2) / (2*l2 * l3))
    print(theta_1_ik)
    print(theta_2_ik)
    print(theta_3_ik)

#forward_kinematics()
inverse_kinematics()