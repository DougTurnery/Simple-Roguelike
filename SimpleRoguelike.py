import esper as ecs
from bearlibterminal import terminal as blt



def main():
    screen_width = 160
    screen_height = 50
    
    blt.open()
    blt.setf(
        "window: size={}x{}, resizeable=true;", 
        screen_width, screen_height)
    blt.setf("font: ../DroidSansMono.ttf, size=12")
    blt.clear()
    blt.refresh()
    while True:
        blt.clear()
        blt.printf(2,1,"Hello World!")
        blt.refresh()
        if blt.read() == blt.TK_CLOSE:
            break
    blt.close()

if __name__ == "__main__":
    main()