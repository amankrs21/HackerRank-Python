"""
PROBLEM STATEMENT:

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Input Format
A single line containing the thickness value for the logo.

Constraints
The thickness must be an odd number.

Output Format
Output the desired logo.
"""

# Solution

thickness = int(input()) #This must be an odd number

letter = 'H'

# STEP 1: Top Cone
for i in range(thickness):
    print((letter*i).rjust(thickness-1) + letter + (letter*i).ljust(thickness-1))

# STEP 2: Top Pillars
for i in range(thickness+1):
    print((letter*thickness).center(thickness*2) + (letter*thickness).center(thickness*6))
    
# STEP 3: Middle Belt
for i in range((thickness+1)//2):
    print((letter*thickness*5).center(thickness*6))
    
# STEP 4: Bottom Pillars (same as step 3)
for i in range(thickness+1):
    print((letter*thickness).center(thickness*2) + (letter*thickness).center(thickness*6))
    
# STEP 5: Bottom Cone
for i in range(thickness):
    print(((letter*(thickness-i-1)).rjust(thickness) + letter + (letter*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

