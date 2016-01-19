"""
Author: Paul Zenie
File: letterHist.py
date: 11/30/14
"""
from turtle import *
import math

def letterFreqPlot(freqPlotList):
    """
    Draws a histogram of letter frequencies
    :param freqList: A list of floating point values between 0.0 and 1.0.
    :return: None
    """
    speed(10)
    maxvalue = 0
    for i in freqPlotList:
        if i > maxvalue:
            maxvalue = i
    value = maxvalue / 10
    hideturtle()
    setup(width=1000, height=600)
    up()
    setpos(-400,-250)
    down()
    height = 500
    width = 800
    lt(90)
    fd(height)
    bk(height)
    rt(90)
    fd(width)
    bk(width)
    x = height / 10
    i = 0
    while i <= height:
        left(180)
        fd(10)
        bk(10)
        rt(90)
        fd(x)
        rt(90)
        i += x
    p = 0
    y = -250
    k = value
    value = 0
    while p <= 10:
       value = math.ceil(value*100)/100
       write1(-420, y, str(value))
       y += 50
       value += k
       p += 1
    w = width/26
    l = -400
    q = 0
    lst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    while q < 26:
        write1((l+w/2), -270, lst[q])
        q += 1
        l += w
    write1(0, -290, "Letter")
    write1(-480, 0, "Frequency")
    q = 0
    fillcolor("blue")
    up()
    goto(-400, -250)
    down()
    for i in freqPlotList:
        begin_fill()
        i =  (50/k) * i
        lt(90)
        fd(i)
        rt(90)
        fd(w)
        rt(90)
        fd(i)
        lt(90)
        end_fill()

def write1(x, y, s):
    """
    writes the string at the given position
    :param x: x value at which to write the string
    :param y: y value at which to write the string
    :param s: the string of which to write
    :return:None
    """
    penup()
    goto(x, y)
    pendown() 
    write(s)

