from pico2d import*

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running == False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running == False

running = True

close_canvas()