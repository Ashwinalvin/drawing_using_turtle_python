import turtle
t = turtle.Turtle()
t.hideturtle()
t1 = turtle.Turtle()
t1.hideturtle()
scr = turtle.Screen()
scr.bgcolor('black')
def filler(x,y,length,x1,y1,len):
  t.begin_fill()
  t.fillcolor('white')
  t.up()
  t.goto(x,y)# moves that co ordinates
  t.down()
  t.circle(length)
  t.end_fill()

  t1.begin_fill()
  t1.fillcolor('yellow')
  t1.up()
  t1.goto(x1,y1)  # moves that co ordinates
  t1.down()
  t1.circle(len)
  t1.end_fill()

filler(0,-50,50,0,-30,30)
filler(200,200,50,200,220,30)
filler(-200,200,50,-200,220,30)
filler(200,-200,-50,200,-220,-30)
filler(-200,-200,-50,-200,-220,-30)










