import pgzrun
import random
import time
WIDTH=800
HEIGHT=600
satelite=[]
lines=[]
next_satelite=0
start_time=0
end_time=0
total_time=0
number_of_satelites=20
def create_satelites():
    for i in range(0,20):
        satelite=Actor("satelite")
        satelite.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        satelite.append(satelite)
    start_time=time()
def draw():
    screen.blit("background",(0,0))
    number=1
    for i in satelite():
        screen.draw.text(str(number),(satelite.pos[0],satelite.pos[1]+20))
        satelite.draw()
        number=number+1
pgzrun.go