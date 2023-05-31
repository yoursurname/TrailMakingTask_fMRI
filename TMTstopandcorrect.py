# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:33:33 2021

@author: emilo
"""

import numpy as np
import random
from PIL import Image, ImageDraw, ImageFont
import os
import pandas as pd

inf=np.inf
pi=np.pi

#Circle cross...
def length_AB(A, B):
    return pow(pow(A[0]-B[0], 2)+pow(A[1]-B[1], 2), 1/2)

def check_circles_cross(A, ra, B, rb):
    length=length_AB(A, B)
    if length<=ra+rb:
        cross=True
    else:
        cross=False
    return cross

#直線A, Bの傾き
#Slope of straight lines A and B
def gradient_2_dots(A, B):
    if A[0]==B[0]:
        k=inf
    else:
        k=(B[1]-A[1])/(B[0]-A[0])
    return k

#入力の点A, B, C, Dについて、直線ABと直線CDの交点XをpOA+(1-p)OB、qOC+(1-q)ODで表す時のp, q
#なお直線ABの傾きは無限大ではないこと、二直線は平行でないこと、の2点は満たしていることを前提とする
#For the input points A, B, C, D, p, q when the intersection X of the straight line AB and the straight line CD is represented by pOA + (1-p) OB and qOC + (1-q) OD.
# It is assumed that the two points that the slope of the straight line AB is not infinite and that the two straight lines are not parallel are satisfied.
def calc_pq(A, B, C, D):
    q=((D[1]-B[1])*(A[0]-B[0])-(D[0]-B[0])*(A[1]-B[1]))/((C[0]-D[0])*(A[1]-B[1])-(C[1]-D[1])*(A[0]-B[0]))
    p=(q*(C[0]-D[0])+D[0]-B[0])/(A[0]-B[0])
    return p, q

#点A, B, C, Dが与えられたとき、線分ABと線分CDが交差するか判定する関数
# A function that determines whether line segment AB and line segment CD intersect when points A, B, C, and D are given.
def check_AB_CD_cross(A, B, C, D):
    k1=gradient_2_dots(A, B)
    k2=gradient_2_dots(C, D)
    
    if k1==inf and k2==inf:
        cross=False
    elif k1==k2:
        cross=False
    else:
        if k1!=inf:
            p, q=calc_pq(A, B, C, D)
        else:
            p, q=calc_pq(C, D, A, B)
            
        if p*(1-p)>=0 and q*(1-q)>=0:
            cross=True
        else:
            cross=False
    return cross

#Skaffa en uppsättning TMT -noder

def get_nodes(n_nodes, space, white, diameter):
    cross=True
    while cross==True:
        nodes=np.c_[np.random.rand(n_nodes)*(space[0]-2*white[0])+white[0], np.random.rand(n_nodes)*(space[1]-2*white[1])+white[1]]
        #Emil Removed diameter/2 to minimize chance of linecrossing trail
        cross=check_all_circles_cross(nodes, diameter)
    return nodes

def check_all_circles_cross(nodes, r):
    cross=False
    for x in range(nodes.shape[0]-1):
        for y in range(x+1, nodes.shape[0]):
            if check_circles_cross(nodes[x], r, nodes[y], r):
                cross=True
    return cross

def uncrosser(nodes, space, white, diameter):
    cross=True
    while cross==True:
        nodes, cross=line_uncrosser(nodes)
    
    return nodes

def line_uncrosser(nodes):
    cross=False
    for x in range(nodes.shape[0]-3):
        for y in range(x+2, nodes.shape[0]-1):
            if check_AB_CD_cross(nodes[x], nodes[x+1], nodes[y], nodes[y+1]):
                cross=True
                nodes=AB_CD_2_AC_BD(nodes, x, y)
                break
        
        if cross==True:
            break
    return nodes, cross

def AB_CD_2_AC_BD(nodes, x, y):
    nodes=np.r_[nodes[:x+1], nodes[y:x:-1], nodes[(y+1):]]
    return nodes



#n_nodes=12
n_nodes=25
space_w=1920
space_h=1080
white_w=100
white_h=50
diameter=65

space=np.array([space_w, space_h])
white=np.array([white_w, white_h])

#Making several iterations of the TMT maps in one go
iterations = [12]
for it in iterations:

    #Create a list for squarePos
    Squareoptions = ["Above", "Left", "Right"]
    n = 0
    Squares = ['x']
    while n < 25:
        squarePos = random.choice(Squareoptions)
        if Squares[n] != squarePos:
            Squares.append(squarePos)
            n = n + 1
    del Squares[0]


    #TMT-Stop
    nodes=get_nodes(n_nodes, space, white, diameter)
    nodes=uncrosser(nodes, space, white, diameter)

    im=Image.new('RGB', (space[0], space[1]), (255, 255, 255))
    draw=ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 44)



    #Parameters add by Pierre for convenience 
    task = "TMT-stop-A"
    iteration = it
    images_folder = "".join(["TMT", task[-1], "_images/num_", str(iteration)])
    image_prefix = "".join([task, "_1_", str(iteration)])
    image_path = "".join([images_folder, "/",image_prefix])



    if os.path.exists(images_folder) is False:
        os.mkdir(images_folder)





    if task[-1]=="B":
        #TMT B
        characters_num=[' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13']
        characters_jpn=[' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J', ' K', ' L']
        characters=[None]*25
        characters[::2]=characters_num
        characters[1::2]=characters_jpn
        
    if task[-1]=="A":
        # #TMT A
        characters=[' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']


    #Draw Start and End
    draw.text((nodes[0][0]-diameter*1/2, nodes[0][1]+diameter*1/2), "Start", (0, 255, 0), font)
    #draw.text((nodes[11][0]-diameter*1/2, nodes[11][1]+diameter*1/2), "End", (0, 0, 0), font)
    draw.text((nodes[24][0]-diameter*1/2, nodes[24][1]+diameter*1/2), "End", (0, 0, 0), font)

    for i in range(nodes.shape[0]):
        temp=nodes[i]
        x, y = nodes[i]
        tempsquares=Squares[i]
        draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
        draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)
        
        #Draw squares
        radius = diameter/2
        box_length = diameter/2.3

        #Added by Pierre
        square_shapes = {
        "Above": [x-box_length/2, y-radius-box_length, x+box_length/2, y-radius],
        "Left": [x-radius-box_length, y-box_length/2, x-radius, y+box_length/2],   
        "Right": [x+radius, y-box_length/2, x+radius+box_length, y+box_length/2]
        }
        
        draw.rectangle(square_shapes[tempsquares], fill= "black")


    im.save(f'{image_path}.png', quality=95)
    draw.text((nodes[0][0]-diameter*1/2, nodes[0][1]+diameter*1/2), "Start", (0, 0, 0), font)

    #Image for filled first number/letter
    draw.ellipse((nodes[0][0]-diameter/2, nodes[0][1]-diameter/2, nodes[0][0]+diameter/2, nodes[0][1]+diameter/2), fill=(0, 255, 0), outline=(0, 0, 0))
    draw.text((nodes[0][0]-diameter*2/5, nodes[0][1]-diameter*2/5), characters[0], (0, 0, 0), font)
    im.save(f'{image_path}firstgreen.png', quality=95)
    draw.ellipse((nodes[0][0]-diameter/2, nodes[0][1]-diameter/2, nodes[0][0]+diameter/2, nodes[0][1]+diameter/2), fill=(255, 0, 0), outline=(0, 0, 0))
    draw.text((nodes[0][0]-diameter*2/5, nodes[0][1]-diameter*2/5), characters[0], (0, 0, 0), font)
    im.save(f'{image_path}firstred.png', quality=95)
    draw.ellipse((nodes[0][0]-diameter/2, nodes[0][1]-diameter/2, nodes[0][0]+diameter/2, nodes[0][1]+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))  
    draw.text((nodes[0][0]-diameter*2/5, nodes[0][1]-diameter*2/5), characters[0], (0, 0, 0), font)

    #Draw lines (trails) and save as images
    for i in range(nodes.shape[0]-1):
        x, y =nodes[i]
        x2, y2=nodes[i+1]
        draw.line((x, y, x2, y2), fill=(0, 0, 0), width=6)
        im.save(f'{image_path}linestimulus{i}.png', quality=95)
        draw.line((x, y, x2, y2), fill=(0, 255, 0), width=6)
        draw.ellipse((x2-diameter/2, y2-diameter/2, x2+diameter/2, y2+diameter/2), fill=(0, 255, 0), outline=(0, 0, 0))
        draw.text((x2-diameter*2/5, y2-diameter*2/5), characters[i+1], (0, 0, 0), font)
        draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
        draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)
        im.save(f'{image_path}greenlinestimulus{i}.png', quality=95)
        draw.line((x, y, x2, y2), fill=(0, 0, 0), width=6)
        draw.ellipse((x2-diameter/2, y2-diameter/2, x2+diameter/2, y2+diameter/2), fill=(255, 0, 0), outline=(0, 0, 0))
        draw.text((x2-diameter*2/5, y2-diameter*2/5), characters[i+1], (0, 0, 0), font)
        draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
        draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)
        im.save(f'{image_path}redlinestimulus{i}.png', quality=95)
        draw.line((x, y, x2, y2), fill=(0, 0, 0), width=6)
        draw.ellipse((x2-diameter/2, y2-diameter/2, x2+diameter/2, y2+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))  
        draw.text((x2-diameter*2/5, y2-diameter*2/5), characters[i+1], (0, 0, 0), font)
        draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
        draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)

    #Saving data for trial excel file
    data = pd.DataFrame(
        {
            "NumberLetter": characters + [""],
            "corrAns": ['["2"]' if pos == "Above" else '["1"]' if pos == "Left" else '["3"]' for pos in Squares] + [""],
            "Correct": [2 if pos == "Above" else 1 if pos == "Left" else 3 for pos in Squares] + [""],
            "StimFile": [f'Images/{image_prefix}.png', f'Images/{image_prefix}.png'] + [f'Images/{image_prefix}linestimulus{i}.png' for i in range(n_nodes-1)],
            "Correct_StimFile": [f'Images/{image_prefix}.png', f'Images/{image_prefix}firstgreen.png'] + [f'Images/{image_prefix}greenlinestimulus{i}.png' for i in range(n_nodes-1)],
            "False_StimFile_Version": [f'Images/{image_prefix}.png', f'Images/{image_prefix}firstred.png'] + [f'Images/{image_prefix}redlinestimulus{i}.png' for i in range(n_nodes-1)]
        }
    )
    data.to_csv(f"{images_folder}/{image_prefix}.csv", sep= ';',  index=False)
'''
#TMT Circle control
im=Image.new('RGB', (space[0], space[1]), (255, 255, 255))
draw=ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 44)
# characters_num=[' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13']
# characters_jpn=[' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J', ' K', ' L']
# characters=[None]*25
# characters[::2]=characters_num
# characters[1::2]=characters_jpn
#For only numbers:
#characters=[' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12']
#For only letters:
#characters=[' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J', ' K', ' L']
characters=[' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
#characters=[' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J', ' K', ' L', ' M', ' N', ' O', ' P', ' Q', ' R', ' S', ' T', ' U', ' V', ' W', ' X', ' Y']

#Circle nodes
Circlenodes = []

# Draw 12 ellipses along the contours of the circle
# Change 0 and 360 to adjust start and end node
#step 14 for 25
for i in np.arange(-90, 270, 14.4):
    x = int(1920/2 + 1920/4 * math.cos(math.radians(i)))
    y = int(1080/2 + 1080/2.5 * math.sin(math.radians(i)))
    circlenode = x-5, y-5, x+5, y+5
    Circlenodes.append(circlenode)
    #draw.ellipse((x-5, y-5, x+5, y+5), fill = 'black', outline ='black')
    
for i in range(nodes.shape[0]):
    temp=Circlenodes[i]
    tempsquares=Squares[i]
    draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
    draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)
    
#Draw squares
    if tempsquares == "Above":
        draw.rectangle((x-diameter/5, y-diameter/2, x+diameter/5, y-diameter/2), fill=(0, 0, 0), outline=(0, 0, 0))
    elif tempsquares == "Left":
        draw.rectangle((x-diameter/2, y-diameter/5, x-diameter/5, y+diameter/5), fill=(0, 0, 0), outline=(0, 0, 0))
    elif tempsquares == "Right":
        draw.rectangle((x+diameter/2, y-diameter/5, x+diameter/2, y+diameter/5), fill=(0, 0, 0), outline=(0, 0, 0))
  
#Draw Start and End
draw.text((Circlenodes[0][0]-diameter*1/2, Circlenodes[0][1]+diameter*1/2), "Start", (0, 255, 0), font)
draw.text((Circlenodes[24][0]-diameter*1/2, Circlenodes[24][1]+diameter*1/2), "End", (0, 0, 0), font)

          #Save the image
im.save('TMTstop-control_1_3.jpg', quality=95)
draw.text((Circlenodes[0][0]-diameter*1/2, Circlenodes[0][1]+diameter*1/2), "Start", (0, 0, 0), font)

#Image for filled first number/letter
draw.ellipse((Circlenodes[0][0]-diameter/2, Circlenodes[0][1]-diameter/2, Circlenodes[0][0]+diameter/2, Circlenodes[0][1]+diameter/2), fill=(0, 255, 0), outline=(0, 0, 0))
draw.text((Circlenodes[0][0]-diameter*2/5, Circlenodes[0][1]-diameter*2/5), characters[0], (0, 0, 0), font)
im.save('TMTstop-control_1_3firstgreen.png', quality=95)
draw.ellipse((Circlenodes[0][0]-diameter/2, Circlenodes[0][1]-diameter/2, Circlenodes[0][0]+diameter/2, Circlenodes[0][1]+diameter/2), fill=(255, 0, 0), outline=(0, 0, 0))
draw.text((Circlenodes[0][0]-diameter*2/5, Circlenodes[0][1]-diameter*2/5), characters[0], (0, 0, 0), font)
im.save('TMTstop-control_1_3firstred.png', quality=95)
draw.ellipse((Circlenodes[0][0]-diameter/2, Circlenodes[0][1]-diameter/2, Circlenodes[0][0]+diameter/2, Circlenodes[0][1]+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))  
draw.text((Circlenodes[0][0]-diameter*2/5, Circlenodes[0][1]-diameter*2/5), characters[0], (0, 0, 0), font)


#Draw lines (trails) and save as images
for i in range(nodes.shape[0]-1):
    temp=Circlenodes[i]
    temp2=Circlenodes[i+1]
    draw.line((x, y, x2, y2), fill=(0, 0, 0), width=6)
    im.save('TMTstop-control_1_3linestimulus{0}.png'.format(i), quality=95)
    draw.line((x, y, x2, y2), fill=(0, 255, 0), width=6)
    draw.ellipse((x2-diameter/2, y2-diameter/2, x2+diameter/2, y2+diameter/2), fill=(0, 255, 0), outline=(0, 0, 0))
    draw.text((x2-diameter*2/5, y2-diameter*2/5), characters[i+1], (0, 0, 0), font)
    draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
    draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)
    im.save('TMTstop-control_1_3greenlinestimulus{0}.png'.format(i), quality=95)
    draw.line((x, y, x2, y2), fill=(0, 0, 0), width=6)
    draw.ellipse((x2-diameter/2, y2-diameter/2, x2+diameter/2, y2+diameter/2), fill=(255, 0, 0), outline=(0, 0, 0))
    draw.text((x2-diameter*2/5, y2-diameter*2/5), characters[i+1], (0, 0, 0), font)
    draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
    draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)
    im.save('TMTstop-control_1_3redlinestimulus{0}.png'.format(i), quality=95)
    draw.line((x, y, x2, y2), fill=(0, 0, 0), width=6)
    draw.ellipse((x2-diameter/2, y2-diameter/2, x2+diameter/2, y2+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))  
    draw.text((x2-diameter*2/5, y2-diameter*2/5), characters[i+1], (0, 0, 0), font)
    draw.ellipse((x-diameter/2, y-diameter/2, x+diameter/2, y+diameter/2), fill=(255, 255, 255), outline=(0, 0, 0))
    draw.text((x-diameter*2/5, y-diameter*2/5), characters[i], (0, 0, 0), font)


    
'''
    


    



