import pgzrun
from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
tijd = 7
tijd_over = tijd
game_over = False

vos = Actor('fox')
vos.pos = 100, 100

munt = Actor('coin')
munt.pos = 200, 200

def draw():
    global game_over
    global score
    global tijd_over
    global tijd
    
    screen.fill('green')
    vos.draw()
    munt.draw()
    screen.draw.text('Score: ' + str(score), color='black', topleft=(10, 10))
    screen.draw.text('Tijd over: ' + str(tijd_over), color='black', topleft=(10, 30))

    if game_over:
        screen.fill('green')
        screen.draw.text('Eindscore: ' + str(score), color='black', center=(200, 200), fontsize=60)
        screen.draw.text('Druk op spatie om te herstarten', color='black', center=(200, 230), fontsize=30)
        if keyboard.space:
            game_over = False
            score = 0
            tijd_over = 7
            clock.schedule(tijd_om, tijd)

def plaats_munt():
    munt.x = randint(20, (WIDTH - 20))
    munt.y = randint(20, (HEIGHT - 20))

def update_timer():
    global tijd_over
    tijd_over = tijd_over - 1
    
def tijd_om():
    global game_over
    game_over = True

def update():
    global score
    if game_over == False:
        if keyboard.left:
            vos.x = vos.x - 2
        if keyboard.right:
            vos.x = vos.x + 2
        if keyboard.up:
            vos.y = vos.y - 2
        if keyboard.down:
            vos.y = vos.y + 2

    munt_verzameld = vos.colliderect(munt)

    if munt_verzameld:
        score = score + 1
        plaats_munt()

clock.schedule(tijd_om, tijd)
clock.schedule_interval(update_timer, 1.0)
plaats_munt()

pgzrun.go()
