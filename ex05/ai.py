import pygame
import random

win = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

class Bird:
    def __init__(self,win):
        self.win = win
        self.y = 300
        self.x = 25
        self.gravity = 1
        self.velocity = 0
        self.lift = -2
        self.air = 0

    def show(self):
        pygame.draw.circle(self.win,(255,255,255),(self.x,self.y),16)

    def update(self):
        if self.air == 0:
            self.velocity += self.gravity
            self.y += self.velocity
            self.air = 1
        elif self.air > 2:
            self.air = 0
        elif self.air > 0:
            self.air += 1


        if self.y > 600:
            self.y = 600
            self.velocity = 0

        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def up(self):
        self.velocity += self.lift

class Pipe:
    def __init__(self,win):
        self.win = win
        self.top = random.randint(0,300)
        self.bottom = random.randint(0,300)
        self.w = 20
        self.x = 400
        self.speed = 2
        self.passed = False
        self.color = (255,255,255)

    def show(self):
        pygame.draw.rect(self.win,self.color,(self.x,0,self.w,self.top))
        pygame.draw.rect(self.win,self.color,(self.x,600-self.bottom,self.w,self.bottom))

    def update(self):
        self.x -= self.speed

    def hits(self,bird):
        if bird.y < self.top or bird.y > 600 - self.bottom:
            if bird.x >= self.x and bird.x <= self.x + self.w:
                return True
        return False

def drawWindow(bird,pipes):
    bird.show()
    bird.update()
    for pipe in pipes:
        pipe.show()

    pygame.display.update()

bird = Bird(win)
pipes = [Pipe(win)]
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        bird.up()

    add_pipe = False
    rem = []
    for pipe in pipes:
        if pipe.x + pipe.w < 0:
                rem.append(pipe)
        if not pipe.passed and pipe.x < bird.x:
            pipe.passed = True
            add_pipe = True

        if pipe.hits(bird):
            pipe.color = (255,0,0)

        pipe.update()

    if add_pipe:
        pipes.append(Pipe(win))

    for r in rem:
        pipes.remove(r)

    win.fill((0,0,0))
    drawWindow(bird,pipes)