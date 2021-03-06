from vars import *
from ursina import *


class body:

    # pos is Vec3
    def __init__(self,name,mass,pos,vel,color=color.white):
        self.name=name
        self.mass=mass
        self._pos=pos
        self.vel=vel
        self.acc=Vec3(0,0,0)
        self.ent=Entity(model='sphere', color=color)
        self.ent.position=self._pos/DFACTOR
        self.trail=Entity(model=Mesh(vertices=[],mode='point',thickness=0.05,render_points_in_3d=True))

    def __str__(self):
        return f"{self.name} pos:{str(self.pos)}, vel:{str(self.vel)}, acc:{str(self.vel)}"

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self,p):
        self._pos=p
        self.ent.position=p/DFACTOR

    @property
    def x(self):
        return self._pos.x

    @x.setter
    def x(self,v):
        self._pos.x=v
        self.ent.x=self._pos.x/DFACTOR

    @property
    def y(self):
        return self._pos.y

    @y.setter
    def y(self,v):
        self._pos.y=v
        self.ent.y=self._pos.y/DFACTOR

    @property
    def z(self):
        return self._pos.z

    @z.setter
    def z(self,v):
        self._pos.z=v
        self.ent.z=self._pos.z/DFACTOR


class world:

    def __init__(self):

        self.G = 6.6743e-11
        self.parts = []
        self.T=0
        self.dT=dT

    # inelastic collision for every pair of bodies closer than a threshold
    def handle_collisions(self):
        for p in self.parts:
            for q in self.parts:
                if p!=q:
                    d = q.pos - p.pos
                    m = d.length()
                    if m< CONTACTD:
                        p.mass+=q.mass
                        mp=p.mass*p.vel
                        mq=q.mass*q.vel
                        v=(mp*mq)/p.mass
                        p.vel=v
                        self.parts.remove(q)


    def update_acc(self, p):
        p.acc = Vec3(0, 0, 0)
        for q in self.parts:
            if p != q:
                d = q.pos - p.pos
                m=d.length()
                if m==0:
                    m=0.1
                denom = m ** (-3)
                #a = [x * denom * q.mass for x in d.data]
                a=d*denom*q.mass
                p.acc = p.acc + a
        #p.acc.data = [self.G * x for x in p.acc.data]
        p.acc=self.G*p.acc

    # update positions using kick-drift-kick. https://en.wikipedia.org/wiki/Leapfrog_integration
    def update_positions(self):
        for p in self.parts:
            a=p.acc * self.dT /2
            p.vel = p.vel + a

            v=p.vel*self.dT
            p.pos = p.pos + v

            # draw trails
            p.trail.model.vertices.append(p.ent.position)
            if len(p.trail.model.vertices)>30:
                p.trail.model.vertices.pop(0)
            p.trail.model.generate()

            self.update_acc(p)

            a=p.acc*self.dT
            p.vel = p.vel + Vec3(a)
        self.T += self.dT