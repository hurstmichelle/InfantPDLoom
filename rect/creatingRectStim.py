import random
import math
from PIL import Image, ImageDraw

# script for creating dot stimuli with two sets deteremined based on a ratio
# script by Michelle Hurst, hurst.mich@gmail.com, April 2022

# setting up canvas size
stimW = 400
stimH = 600

# setting global properties of the stim (for now, we could vary them though, e.g., vary dot size so that area is varied)
colorOptions = ["darkorange", "blue"]
hueNames = ["orange", "blue"]
unit = 5 # height for each unit of the fraction
radius = 12 #of the corresponding circles
gap = 10 #minimum space between edge of canvas and rectangle

#setting up stim parameters
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

# draw the rectangles
def create_rect(w, unitH, size, color, x0, y0): #width, unit height in pixels, number of units in the height, color, x1, y1 of rect
    x0 = x0
    x1 = x0 + w
    
    y0 = y0
    y1 = y0 + unitH*size

    return draw.rectangle((x0, y0, x1, y1), fill = color, outline = color)

# now to actually create the stim
# looping through the stimList and creating the dots needed for each


for v in range(1, 3): #to make two sets

    for m in range(0, len(colorOptions)): # to make a set for each color to be dominant, to be counterbalanced

        majorColor = colorOptions[m]
        minorColor = colorOptions[(m+1)%2]

        for j in range(0, len(stimList)):

            # setting up new image from PIL
            stim = Image.new('RGBA', (stimW, stimH), color = 'white')
            draw = ImageDraw.Draw(stim)
            draw.rectangle([(0,0), (stimW - 1,stimH - 1)], outline = 'white')

            width = random.randrange(round(stimW*(1/6)), round(stimW*(1/3)), 1) # total width, randomly selected
            unitHeight = (math.pi * (radius*radius))/width # creating pixle unit of height, based on width so that area of a single dot will be the area of a single "unit"

            set1 = stimList[j][0] #getting the number of units in the bottom set
            set2 = stimList[j][1] #getting the number of units in the top set

            # setting the x0 and y0 of each of the rectangles to be made
            totalHeight = set1 * unitHeight + set2 * unitHeight #height of the whole rectangle

            max_vertical_jitter = round(.25*((stimH - totalHeight)/2 - gap)) #range of vertical jitter
            max_horizontal_jitter = round(.25*((stimW - width)/2 - gap*2)) #range of horizontal jitter
            
            vertical_jitter = random.randrange(-max_vertical_jitter, max_vertical_jitter, 1)
            horizontal_jitter = random.randrange(-max_horizontal_jitter, max_horizontal_jitter, 1)

            centX = stimW/2 + horizontal_jitter
            centY = stimH/2 + vertical_jitter

            x0 = centX - width/2
            y0_r2 = centY - (totalHeight/2)
            y0_r1 = y0_r2 + set2*unitHeight

            create_rect(width, unitHeight, set1, majorColor, x0, y0_r1)
            create_rect(width, unitHeight, set2, minorColor, x0, y0_r2)

            # save image with name of the form cont_habtype_set1_set2
            # to make a second version
            fileName = "rect_" + str(hueNames[m]) + "_" + stimList[j][2] + "_" +  str(stimList[j][0]) + "_" + str(stimList[j][1]) + "_V" +str(v) +  ".png"
            stim.save("StimFiles/" + fileName)




