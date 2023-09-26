from pico2d import*

open_canvas(1280,1024)
background = load_image('TUK_GROUND.png')
character = load_image('SPRITE_SHEET.png')
idle_character = load_image('IDLE.png')

running = True
x = 1280//2
y = 1024//2
frame = 0
dir_x = 0
dir_y = 0

idle = 0
move_r, move_l, move_u, move_d = 1, 2, 3, 4
state = idle

def handle_events():
    global running
    global dir_x, dir_y
    global state

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running == False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                state = move_r
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                state = move_l
            elif event.key == SDLK_UP:
                dir_y += 1
                state = move_u
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                state = move_d
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
            if dir_x == 0 and dir_y == 0:
                state = idle

while running:

    clear_canvas()
    background.draw(640,512)

    if state == idle:
        idle_character.clip_draw(frame*100,0,100,200,x,y,150,150)
    elif state == move_r:
        character.clip_draw(frame*100,136,100,136,x,y,150,150)
    elif state == move_l:
        character.clip_draw(frame*100,272,100,136,x,y,150,150)
    elif state == move_u:
        character.clip_draw(frame*100,0,100,136,x,y,150,150)
    elif state == move_d:
        character.clip_draw(frame*100,408,100,136,x,y,150,150)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()