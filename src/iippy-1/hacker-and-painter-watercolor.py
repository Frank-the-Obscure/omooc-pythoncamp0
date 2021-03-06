# -*- coding: utf-8 -*-
# Author Frank Hu
# Hacker and Painter, watercolor version
# V2.0, 20150416

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import re

# initalize globals
WIDTH = 300
HEIGHT = 300
SIZE = 10
color_in_use = 'rgb(0,255,255)'
shape_in_use = 'Circle'
size_in_use = SIZE
drawing_list = []
temp_drawing_list = []
pixel_list = []
interval = 2000
time = 0 # for count ticking
timer = 0 
UI_protect = False 

class Drawing:
    # class for a single draw action
    # note: type of painter maybe added in later version.
    def __init__(self, color, position, shape, size):
        self.color = color
        self.position = position
        self.shape = shape
        self.size = size

    def __str__(self): # print for debugging
        return self.color, self.position, self.shape, self.size

class Pixel:
    # class for a single pixel, storing its color and position
    # may be defined as a single pixel Drawing.
    def __init__(self, color, position):
        self.color = color
        self.position = position
        
    def __str__(self): # print for debugging
        return str(self.color), str(self.position)
        
    def draw(self, pixel_list):        
        for i in pixel_list:
            if i.position == self.position: 
            # i.e. there are something in the new pixel, need to merge color
                # first converse RGB to CMYK;
                # then merge CMYK;
                # final transfer back to RGB;
                # i.color = (r, g, b). i.e. a tuple with 3 elements 
                i.color = CMYK_to_RGB(merge_CMYK(RGB_to_CMYK(i.color), 
                                      RGB_to_CMYK(self.color)))
                return pixel_list        
        pixel_list.append(self)
        return pixel_list

def draw_pixel(drawing):
    # draw by append every pixel in the single drawing to pixel list
    i = 0 - drawing.size
    while i < drawing.size:
        j = 0 - drawing.size
        while j < drawing.size:
            distence = i * i + j * j
            if distence < drawing.size * drawing.size:
                drawing_color_CMYK = RGB_to_CMYK(drawing.color)
                new_pixel = Pixel(CMYK_to_RGB(watercolor(drawing_color_CMYK, drawing.size * drawing.size, distence)), 
                                  [drawing.position[0] + i, drawing.position[1] + j])
                new_pixel.draw(pixel_list)
            j += 1
        i += 1

def watercolor(color_CMYK, shape_size, distence):
    # calculate the distence / max size ratio
    watercolor_ratio = float(shape_size - distence) / shape_size
    return (float(color_CMYK[0]) * watercolor_ratio, 
            float(color_CMYK[1]) * watercolor_ratio,
            float(color_CMYK[2]) * watercolor_ratio, 
            float(color_CMYK[3]) * watercolor_ratio)

def RGB_to_CMYK(color_RGB):
    # the format is 'rgb(r,g,b)', cut rgb(), then translate into a int tuple
    color_RGB_cut = color_RGB.strip('rgb()')
    color_RGB_tuple = color_RGB_cut.split(',')
    color_R = float(int(color_RGB_tuple[0])) / 255
    color_G = float(int(color_RGB_tuple[1])) / 255
    color_B = float(int(color_RGB_tuple[2])) / 255
    color_K = 1 - max(color_R, color_G, color_B)
    if color_K == 1:
        # a special case: 1 - K = 0
        return (0, 0, 0, 1)
    else:
        return ((1 - color_R - color_K) / (1 - color_K), 
                (1 - color_G - color_K) / (1 - color_K), 
                (1 - color_B - color_K) / (1 - color_K),
                color_K)

def merge_CMYK(color_1, color_2):
    return (max(color_1[0], color_2[0]), max(color_1[1], color_2[1]),
            max(color_1[2], color_2[2]), max(color_1[3], color_2[3]))

def CMYK_to_RGB(color_CMYK):
    # R = 255(1-C)(1-K); G = 255(1-M)(1-K); B = 255(1-Y)(1-K)
    color_R = int((255 * (1 - color_CMYK[0]) * (1 - color_CMYK[3])))
    color_G = int((255 * (1 - color_CMYK[1]) * (1 - color_CMYK[3])))
    color_B = int((255 * (1 - color_CMYK[2]) * (1 - color_CMYK[3])))
    return 'rgb' + str((color_R, color_G, color_B))
    # return format 'rgb(r,g,b)'

def paint(canvas): 
    # main print function
    # display color and shape in use, in canvas
    # as it is not supported to print on label
    for i in pixel_list:
        canvas.draw_point(i.position, i.color)
    # protect from input when playing
    if UI_protect == True:
            canvas.draw_text('Playing, not able to draw now.',
                            (20,20), 14, 'Black')
            return
    canvas.draw_text('Color in use: %s' % (color_in_use), 
                     (20, 20), 14, 'Black') 
    canvas.draw_polygon([(210, 5), (230,5), (230,25), (210,25)], 1, color_in_use, color_in_use)
    canvas.draw_text('Play interval in use: %s' % (interval),
                     (20, 40), 14, 'Black') 

def append_drawing(mouse_click): # catch mouse click when not playing
    if UI_protect == False: #i.e. not protecting
        print mouse_click, color_in_use, shape_in_use, size_in_use
        single_drawing = Drawing(color_in_use, mouse_click, shape_in_use, size_in_use)
        drawing_list.append(single_drawing)
        draw_pixel(single_drawing)
    
def color_setter(color_input): # input color
    global color_in_use
    color_in_use = 'rgb(' + str(color_input) + ')' 

def random_color():
    global color_in_use
    random_color_tuple = (random.randrange(0,255),
                          random.randrange(0,255),
                          random.randrange(0,255))
    color_in_use = 'rgb' + str(random_color_tuple)

# next three functions for replay
def play():
    # 1: process lists to temp place
    global drawing_list
    global pixel_list
    global temp_drawing_list
    global timer
    global UI_protect
    temp_drawing_list = drawing_list
    # 2: clear list
    pixel_list = []
    drawing_list = []
    # 3: remake list with delay
    print interval
    timer = simplegui.create_timer(interval, tick)
    timer.start()
    UI_protect = True

def tick():
    # playing with interval, as canvas is always drawing
    # appending new steps with interval to play
    global drawing_list
    global time 
    global timer
    global UI_protect
    if time < len(temp_drawing_list):
        drawing_list.append(temp_drawing_list[time])
        draw_pixel(temp_drawing_list[time])
        time += 1
        print time
    else:
        timer.stop()
        UI_protect = False
        time = 0
        print "Play finished!"

def change_interval(interval_input): # change interval
    global interval
    # regular expression for robustness. Never be afraid of bad guys now, haha:) 
    # return wrong in console
    if re.match("^[0-9]*[1-9][0-9]*$", interval_input, ): 
        interval = int(interval_input)
    else:
        print 'Wrong interval input! Please input a number!'
    print interval

# create frame
frame = simplegui.create_frame('Hacker and painter, watercolor version', WIDTH, HEIGHT)
frame.set_canvas_background('White')
frame.set_draw_handler(paint)

# set event handler
frame.set_mouseclick_handler(append_drawing) # get click position
# use a input box to get color
# rewrite it in a label...
frame.add_input('Color: valid input is r,g,b. e.g.: 0,255,255',
                color_setter, 150) 
# buttoms for setting shape and color
frame.add_button('Random color', random_color, 150)
# button to play whole progress
frame.add_input('Play interval in ms', change_interval, 150)
frame.add_button('Play', play, 150)
#start frame
frame.start()