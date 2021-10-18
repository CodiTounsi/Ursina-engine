#squid game by CodiTounsi
from ursina import *
from ursina.prefabs.first_person_controller \
import FirstPersonController

app = Ursina()
Sky()
player = FirstPersonController(
    z=50
)
ground = Entity(
    model = 'plane',
    texture = 'grass',
    collider = 'mesh',
    scale=(500,0,500)
)

doll = Entity(
    model='assets/squid.fbx',
    scale=0.02
)


start = Entity(
    color = color.red,
    model='cube', z=40,
    scale=(100,0.1,1)
)

goal = duplicate(
    start,z=5
)

def rotate():
    val = doll.rotation_y
    doll.animate_rotation_y(
        val+180,duration=2
    )
    invoke(rotate, delay=4)
rotate()

label = Text(
    size=Text.size,
    text = f'Time left {00}\t',
    position=(-0.5,0.4)
)
label.create_background()

def UpdateTime(sec):
    if sec==0:
        if player.z > 5:
            player.speed = 0
            player.y = -1.5 
    label.text = f'Time left {sec}\t'
    if sec > 0:
        invoke(UpdateTime,sec-1, delay=1)

UpdateTime(30)
    
def update():
    walking = held_keys['q'] or \
        held_keys['d'] or \
        held_keys['z'] or \
        held_keys['s']
    if player.z < 40 and player.z > 5:
        if walking or player.y > 0 or \
            not mouse.velocity == \
            Vec3(0,0,0):
            if doll.rotation_y%360 == 0:
                player.speed = 0
                player.y = -1.5 

app.run()
