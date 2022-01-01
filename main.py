from ursina import *
from vars import *
from body import *
import random

GO=False

app = Ursina()
window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter


# shifts the camera in a circle whose center is the target
# ang<0 anticlock. ang>0 clockwise
def rotCamXZ(delta):
    #camX=camera.x
    #camZ=camera.z

    v=camera.position.xz
    d=v.length()
    ang=v.signedAngleRad(Vec2(1,0))
    #print(f"ang: {ang*180/PI}")
    #(d, ang) = vec_mag_ang(camX, camZ)
    newang = ang + delta

    if newang < 0:
        newang = (2 * PI) + newang
    elif newang > (2 * PI):
        newang = newang - (2 * PI)

    #print(f"newang: {newang * 180 / PI}")
    newX = d * math.cos(newang)
    newZ = -d * math.sin(newang)

    camera.x = newX
    camera.z = newZ

def rotCamYZ(delta):
    #camX=camera.x
    #camZ=camera.z

    v=camera.position.yz
    d=v.length()
    ang=v.signedAngleRad(Vec2(0,1))
    #print(f"ang: {ang*180/PI}")
    #(d, ang) = vec_mag_ang(camX, camZ)
    newang = ang + delta

    if newang < 0:
        newang = (2 * PI) + newang
    elif newang > (2 * PI):
        newang = newang - (2 * PI)

    #print(f"newang: {newang * 180 / PI}")
    newY = d * math.sin(newang)
    newZ = d * math.cos(newang)

    camera.y = newY
    camera.z = newZ

# this seems to work to avoid quick repetition of pressed keys
def input(key):
    global W
    global GO

    if key=='p':
        W.dT*=10
        print(dT)
    if key=='o':
        W.dT/=10
        print(dT)
    if key=='g':
        GO= not GO

def update():   # update gets automatically called.
    global GO

    if GO:
        # handle collisions
        W.handle_collisions()
        # update positions
        W.update_positions()



    camera.z -= held_keys['x'] * STEP
    camera.z += held_keys['z'] * STEP
    camera.x -= held_keys['a'] * STEP
    camera.x += held_keys['d'] * STEP
    camera.y -= held_keys['s'] * STEP
    camera.y += held_keys['w'] * STEP

    if held_keys['q']:
        rotCamXZ(rotdelta)
    if held_keys['e']:
        rotCamXZ(-rotdelta)

    if held_keys['f']:
        rotCamYZ(rotdelta)
    if held_keys['r']:
        rotCamYZ(-rotdelta)


    camera.lookAt(0, 0, 0)

    # print(f"rot: {camera.rotation}")
    # print(f"pos: {camera.position}")
    pass


def rand_exp(minexp,maxexp):
    sign=random.randint(0,1)
    if sign==0:
        sign=-1
    base=random.randint(1,9)
    #base = random.random()*10
    exp=random.randint(minexp,maxexp)
    return sign*base*pow(10,exp)


# mass=2e30
# pos=Vec3(1e5,0,0)
# vel=Vec3(0,0,0)
# b1=body("b1",mass,pos,vel)
#
# mass=6e24
# pos=Vec3(147e9,0,0)
# vel=Vec3(0,3e4,0)
# b2=body("b2",mass,pos,vel)
#
# mass=2e24
# pos=Vec3(-1e11,0,0)
# vel=Vec3(-1e4,0,0)
# b3=body("b3",mass,pos,vel)

# points = [Vec3(0,0,0), Vec3(0,.5,0), Vec3(1,1,0)]
# curve_renderer = Entity(model=Mesh(vertices=points, mode='line'))

points = [Vec3(0,0,0), Vec3(0,1,0)]
curve_renderer = Entity(model=Mesh(vertices=points, mode='line'))
points = [Vec3(0,0,0), Vec3(0,0,-1)]
curve_renderer = Entity(model=Mesh(vertices=points, mode='line'))
points = [Vec3(0,0,0), Vec3(1,0,0)]
curve_renderer = Entity(model=Mesh(vertices=points, mode='line'))


W=world()

# for i in range(0,NBODIES):
#     mass=rand_exp(10,20)
#     (x,y,z)=(rand_exp(5,10),rand_exp(5,10),rand_exp(5,10))
#     pos=Vec3(x,y,z)
#     (x,y,z)=(rand_exp(1,4),rand_exp(1,4),rand_exp(1,4))
#     (x,y,z)=(0,0,0)
#     vel=Vec3(x,y,z)
#     name=f"b{i}"
#     b=body(name,mass,pos,vel)
#     W.parts.append(b)
#

# b=body("sun",6e26,Vec3(0,0,0),Vec3(0,0,0),color.red)
# W.parts.append(b)
#
# for p in W.parts:
#     print(p.ent.position)
#
b=body("p1",6e24,Vec3(0,0,0),Vec3(0,0,0),color.white)
W.parts.append(b)

b=body("p2",6e10,Vec3(-1e8,0,0),Vec3(0,-1000,0),color.white)
W.parts.append(b)

b=body("p3",6e23,Vec3(8e8,0,0),Vec3(-500,500,0),color.white)
W.parts.append(b)

b=body("p4",6e20,Vec3(0,1e8,0),Vec3(-800,0,0),color.white)
W.parts.append(b)

b=body("p5",6e8,Vec3(1e7,1e7,1e7),Vec3(0,5000,0),color.white)
W.parts.append(b)

b=body("p6",6e12,Vec3(2e8,0,0),Vec3(20,400,0),color.white)
W.parts.append(b)

b=body("p7",6e12,Vec3(3e8,0,0),Vec3(10,400,0),color.white)
W.parts.append(b)




#b=body("p5",6e26,Vec3(0,-1e10,0),Vec3(0,0,0),color.white)
#W.parts.append(b)


# W.parts.append(b1)
# W.parts.append(b2)
# W.parts.append(b3)

camera.position=(0,0,-150)
camera.lookAt(0,0,0)

app.run()   # opens a window and starts the game.
