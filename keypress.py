import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False #if I press the key, the 'ans' is True, otherwise it is False
    #for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key Pressed")
    if getKey("ESCAPE"):
        print('ESC be pressed!')
        return False


if __name__ == '__main__':
    init()
    while True:
        main()