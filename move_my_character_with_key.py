from pico2d import*

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running
    global x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running == False
        elif event.type == SDLK_ESCAPE:
            running == False


running = True
frame = 0
for x in range(0,800,5):

    clear_canvas()
    background.draw(600,100)
    character.clip_draw(frame*50,0,100,100,x,130,200,200)
    update_canvas()

    handle_events()
    if not running:
        break

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()