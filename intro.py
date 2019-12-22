# Write your code here :-)
alien = Actor('alien')
alien.topright = 0 ,10

#sets window wid\ndow height and alien location
HEIGHT = alien.height + 20
WIDTH = 500

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    # resets alien to unhurt after 1 sec delay
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'