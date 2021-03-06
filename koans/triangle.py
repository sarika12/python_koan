#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def checkvalue(func):
    def inner(x, y,z):
        if x > 0 and y > 0 and z > 0 and x+y+z-max(x,y,z) > max(x,y,z):        
            return func(x, y,z)          
        else:
            raise TriangleError          
        
    return inner

@checkvalue
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if a == b == c:
        return 'equilateral'
    if a == b or a == c or  b == c:
        return 'isosceles'
    if a != b != c: 
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
