from pico2d import*

open_canvas(1280,1024)
background = load_image('TUK_GROUND.png')
character = load_image('SPRITE_SHEET.png')

def handle_events():
    global running
    global dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running == False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = 800//2
y = 800//2
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    background.draw(640,512)
    character.clip_draw(frame*100,136,100,136,x,y,150,150)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()