import random
import math
from PIL import Image, ImageDraw

# script for creating dot stimuli with two sets deteremined based on a ratio
# script by Michelle Hurst, hurst.mich@gmail.com, April 2022

# setting up canvas size
stimW = 400
stimH = 600

# setting global properties of the stim (for now, we could vary them though, e.g., vary dot size so that area is varied)
radius = 12
gap = 10
colorOptions = ["darkorange", "blue"]
hueNames = ["orange", "blue"]

# this is the list of stim we want to make
# includes: set1 size, set2 size, habtype as an indicator of stim category
stimList = [
    [8, 4, "hab21"],
    [10, 5, "hab21"],
    [14, 7, "hab21"],
    [16, 8, "hab21"],
    [20, 10, "hab21"],
    [24, 12, "hab21"],
    [28, 14, "hab21"],
    [30, 15, "hab21"],
    [34, 17, "hab21"],
    [36, 18, "hab21"],
    [40, 20, "hab21"],
    [42, 21, "hab21"],
    [46, 23, "hab21"],
    [48, 24, "hab21"], # NEW

    [9, 3, "hab31"],
    [12, 4, "hab31"],
    [15, 5, "hab31"],
    [21, 7, "hab31"],
    [24, 8, "hab31"],
    [27, 9, "hab31"],
    [30, 10, "hab31"],
    [33, 11, "hab31"],
    [39, 13, "hab31"],
    [42, 14, "hab31"],
    [45, 15, "hab31"],
    [48, 16, "hab31"],
    [51, 17, "hab31"],
    [54, 18, "hab31"], # NEW

    [8, 2, "hab41"],
    [12, 3, "hab41"],
    [16, 4, "hab41"],
    [20, 5, "hab41"],
    [24, 6, "hab41"],
    [28, 7, "hab41"],
    [32, 8, "hab41"],
    [36, 9, "hab41"],
    [40, 10, "hab41"],
    [44, 11, "hab41"],
    [48, 12, "hab41"],
    [52, 13, "hab41"],
    [56, 14, "hab41"],
    [60, 15, "hab41"], # NEW
]

# creating the functions needed to create the specs for circles, to draw the circles, and to export the image
# create specs
def generateDots(radius, gap, set1Color, set2Color, set1, set2):
    # creating a dot class to then load into 
    class dot: 
        def __init__(self, x, y, set1, set2, color): 
            self.x = x 
            self.y = y
            self.set1 = set1
            self.set2 = set2
            self.color = color
    n = 0
    while len(circleList) < (set1 + set2):
        # randomly generating x, y coordinates of the dot - using the if statement to add different colors to the dot
        # the first dots will be set1, up until set1 is maxed, then it'll be set2
        if n < set1:
            curDot = dot(random.randrange(radius + gap, stimW - radius - gap, 1), random.randrange(radius + gap, stimH - radius - gap, 1), set1, set2, set1Color)
        else:
            curDot = dot(random.randrange(radius + gap, stimW - radius - gap, 1), random.randrange(radius + gap, stimH - radius - gap, 1), set1, set2, set2Color)
        # now checking that the new dot doesn't overlap with the previously made dots
        overlap = False

        for i in range(0, len(circleList)):
            checkDot = circleList[i]
                # this distance needs to be larger than the radii of each dot + the required minimum gap
            distance = math.sqrt(pow(curDot.x - checkDot.x, 2) + pow(curDot.y - checkDot.y, 2))
            if distance < radius + radius + gap: 
                overlap = True

        if overlap == False:
            circleList.append(curDot)
            n = n + 1

# draw the circles
def create_circle(x, y, r, dotColor): #center coordinates, radius, dotColor which will be used for the outline and fill
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return draw.ellipse((x0, y0, x1, y1), fill = dotColor, outline = dotColor) 

# now to actually create the stim
# looping through the stimList and creating the dots needed for each

for v in range(1, 3): #to make two sets

    for m in range(0, len(colorOptions)): # to make a set for each color to be dominant, to be counterbalanced

        majorColor = colorOptions[m]
        minorColor = colorOptions[(m+1)%2]

        for j in range(0, len(stimList)): #to actually make each stimulus

            # setting up new image from PIL
            stim = Image.new('RGBA', (stimW, stimH), color = 'white')
            draw = ImageDraw.Draw(stim)
            draw.rectangle([(0,0), (stimW - 1,stimH - 1)], outline = 'white')

            # getting the number of dots in set1 and set2 from stimList
            set1 = stimList[j][0]
            set2 = stimList[j][1]

            # create specs for circles and add them to new circleList
            circleList = []
            generateDots(radius, gap, majorColor, minorColor, set1, set2)

            # draw each circle in the circleList
            for c in range(0, len(circleList)):
                create_circle(circleList[c].x, circleList[c].y, radius, circleList[c].color)
                
            # save image with name of the form disc_habtype_set1_set2
            fileName = "disc_" + str(hueNames[m]) + "_" + stimList[j][2] + "_" +  str(stimList[j][0]) + "_" + str(stimList[j][1]) + "_V" +str(v) +  ".png"
            stim.save("StimFiles/" + fileName)




