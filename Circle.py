import turtle
import math
window = turtle.Turtle()
def c(windows,r,rangle):
    height = 2 * math.pi * r / 200
    for i in range(rangle):
        windows.fd(height)
        windows.lt(1)

c(window,150,360)
#怎么测试自己代码话的圆半径为100？
#window.lt(90)
#window.fd(100)
#window.lt(90)
#window.fd(100)
#将这4句代码添加即可
turtle.mainloop()
