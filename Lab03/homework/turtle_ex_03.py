from turtle import*

def draw_square (length, square_color):
    color(square_color)
    for j in range (4):
        forward(length)
        right(90)
    
