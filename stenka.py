import pygame as pg
from random import randint, random
pg.init()
screen = pg.display.set_mode((1196, 610))
finish = False
FPS = 100

#непосредственно ракетка
class Raketka:
    def __init__(self, screen, a = 300):
        self.screen = screen
        self.color = 'white'
        self.a = a 

    def draw(self): # прорисовка
        pg.draw.rect(self.screen, self.color,  (100, self.a, 20, 100))

    def motion(self, event): # движение относительно движения мыши
        self.a = event.pos[1]

    def restart(self): # рестарт
        self.a = 300

#непосредственно ball
class Ball():
    def __init__(self, screen, x=randint(500, 800), y=randint(1, 610)):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 10
        self.vy = 10
        self.tan = random()
        
    def turn(self):
        self.tan = random()    
        
    def draw(self): # прорисовка
        pg.draw.circle(self.screen, 'white', (self.x, self.y), self.r)

    def motion(self): # расчёт движения
        self.x += self.vx
        self.y += self.vy * self.tan
    
    def restart(self): #рестарт
        self.x = randint(300, 1000)
        self.y = randint(1, 610)
    
    def hittest(self, obj):
        """Функция проверяет сталкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        obj = Target(screen)
        if abs((self.x - obj.x)**2 + (self.y - obj.y)**2 - (obj.r + self.r)**2) < 100:
            return True           
        else:
            return False

class Target():
    def __init__(self, screen, x=randint(900, 1000), y=randint(100, 500)):
        self.points = 0
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 20
        

    def draw(self): # прорисовка
        pg.draw.circle(self.screen, 'red', (self.x, self.y), self.r)
    
    def restart(self):
        self.x = randint(200, 1000) 
        self.y= randint(300, 400)


f1 = pg.font.Font(None, 36)
f2 = pg.font.Font(None, 36)

r = Raketka(screen)

b = Ball(screen)

t = Target(screen)
clock = pg.time.Clock()

pg.display.update()

total = 0
max = 0
while not finish:
    screen.fill('black')
    '''Табло с очками'''

    text1 = f1.render(str(total), True, (255, 255, 255))
    screen.blit(text1, (598, 305))

    '''Максимум'''
    if total > max:
        max = total
    text2 = f2.render(str(max), True, (255, 255, 255))
    screen.blit(text2, (1000, 100))


    r.draw()

    '''Работа мячика'''
    b.draw()
    b.motion()
    if b.x >= 1196: 
        b.vx = -b.vx
        b.turn()          #
    if b.y >= 610 or b.y <= 0:  # отталкивание от стен
        b.vy = -b.vy
        b.turn()          #
    if b.x <= 110: # рестарт
        r.restart()
        b.restart()
        total = 0
    if b.x - b.r <= 120 and r.a <= b.y <= r.a + 100: # условие отталкивания от ракетки
        b.turn()
        b.vx = -b.vx
        b.vy = -b.vy
        total += 1
    
    '''Цель'''
    t.draw() 
    if b.hittest(t):
        t.restart()
        total += 10
        

    pg.display.update()
    clock.tick(FPS)
    for event in pg.event.get():    
        if event.type == pg.QUIT:
            finish = True
        if event.type == pg.MOUSEMOTION:
            r.motion(event)                    
    pg.display.update()    
pg.quit()
