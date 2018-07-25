# -*- coding: utf-8 -*-
"""
Programmer: Darshan Patel
Project: Python Session Activity 1
Date: July 23rd, 2018
Description: Calculates distance between two user inputted co-ordinates
Company: KPIT
Copyright: KPIT C 2018
"""

"""
Code will ask user to enter part by part coordinates. 
For ex: if you want to enter following coordinates:
					90 E, 789 N 
						and
					16 W, 34 S;
		90 is numeric part of Horizontal Coordinate 1 and
		E is direction of Horizontal Coordinate 1;
		
		789 is numeric part of Vertical Coordinate 1 and
		N is direction of Horizontal Coordinate 1;
		
		16 is numeric part of Horizontal Coordinate 2 and
		W is direction of Horizontal Coordinate 2;
		
		34 is numeric part of Vertical Coordinate 2 and
		S is direction of Horizontal Coordinate 2.

After entering these coordinates, code will calculate distance between this
two coordinates set in miles.
"""

"""
Variable Meaning
horizontal_coordinate_1    horizontal 1st coordinate(numeric)
vertical_coordinate_1      vertical 1st coordinate(numeric)
horizontal_coordinate_2    horizontal 2nd coordinate(numeric)
vertical_coordinate_2      vertical 2nd coordinate(numeric)
horizontal_direction_1     horizontal 1st direction in ('E' or 'W')
vertical_direction_1       vertical 1st direction in ('N' or 'S')
horizontal_direction_2     horizontal 2nd direction in ('E' or 'W')
vertical_direction_2       vertical 2nd direction in ('N' or 'S')
distance                   distance between coordinates in miles
temp1              power of (horizontal_coordinate_2 - horizontal_coordinate_1)
temp2              power of (vertical_coordinate_2 - vertical_coordinate_1)
"""

import math

'''USER Input'''
horizontal_coordinate_1 = int(input('Enter horizontal numeric' 
                                    ' part of first coordinate: '))

horizontal_direction_1 = input('Enter horizontal direction'
                               ' ("E" or "W") of first coordinate: ')

vertical_coordinate_1 = int(input('Enter vertical numeric'
                                  ' part of first coordinate: '))

vertical_direction_1 = input('Enter vertical direction'
                             ' ("N" or "S") of first coordinate: ')

horizontal_coordinate_2 = int(input('Enter horizontal numeric'
                                    ' part of second coordinate: '))

horizontal_direction_2 = input('Enter horizontal direction'
                               ' ("E" or "W") of second coordinate: ')

vertical_coordinate_2 = int(input('Enter vertical numeric'
                                  ' part of second coordinate: '))

vertical_direction_2 = input('Enter vertical direction'
                             ' ("N" or "S") of second coordinate: ')

'''User Input conversion to uppercase'''
horizontal_direction_1 = horizontal_direction_1.upper()
vertical_direction_1 = vertical_direction_1.upper()
horizontal_direction_2 = horizontal_direction_2.upper()
vertical_direction_2 = vertical_direction_2.upper()

flag = 1

'''Input Data Validation'''
if horizontal_direction_1 != 'E' and horizontal_direction_1 != 'W':
    flag = 0
    print('1st Coordinate Horizontal Direction is Invalid.')
if vertical_direction_1 != 'N' and vertical_direction_1 != 'S':
    flag = 0
    print('1st Coordinate Vertical Direction is Invalid.')
if horizontal_direction_2 != 'E' and horizontal_direction_2 != 'W':
    flag = 0
    print('2nd Coordinate Horizontal Direction is Invalid.')
if vertical_direction_2 != 'N' and vertical_direction_2 != 'S':
    flag = 0
    print('2nd Coordinate Vertical Direction is Invalid.')


'''Calculation'''
temp1 = math.pow((horizontal_coordinate_2 - horizontal_coordinate_1), 2)
temp2 = math.pow((vertical_coordinate_2 - vertical_coordinate_1), 2)
distance = math.sqrt(temp1 + temp2)

'''Output'''
if flag == 1:
    print('Distance between coordinates is %f miles.', distance)
