import pygame, sys, random

### Constants ###
FPS = 60
game_start_time=0
lvl2_start_time=0

# Standered template stuff
# Don't mind this very much
pygame.init()
pygame.mixer.init()
SCREEN_WIDTH=1000
SCREEN_HEIGHT=650
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Fruit Catcher!")
clock = pygame.time.Clock()
start_tick = pygame.time.get_ticks()
# NEW LEVEL INTERMEDIATE

### GLOBAL VARIABLES ###
scorez=''
player_speed = 10
fall_speed = 2
spawn_rate = 2

seconds = 0
last_apple_time = 0
bckgrnd = pygame.image.load('start-title.png')
cur_fruit = ""
l1b = pygame.image.load('l1_back.png')
l2b = pygame.image.load('l2_back.png')
lvlintr = pygame.image.load('lvl1.png')
level_one_score = 0
level_two_score = 0
high_l1 = 0
high_l2 = 0

apfrt = pygame.image.load("apples.png")
bafrt = pygame.image.load("banana.png")
stfrt = pygame.image.load("strawberry.png")
bomb=pygame.image.load("bomb.png")
hud_font = pygame.font.Font('pixelify.ttf', 40) #Load font object.

# Setting the default state
gameState = 'start'
# Setting the starting basket position.
player_pos = pygame.Vector2((screen.get_width() / 2)-100, (screen.get_height() - 100))
# Fruit locations
fruit_dict = [{'name': "apple", 'loc': [500,0], 'rect': None}]

# We'll be using this function to change the game state instead of
# manually using global variables
def set_state(state):
    global gameState
    gameState = state

def backimg(img):
    size = pygame.transform.scale(img,(1000,650))
    screen.blit(size,(0,0))

### PLAYER SPECIFIC FUNCTIONS ###

def score_change(change):
    global level_one_score, level_two_score
    if gameState == 'level 1':
        level_one_score += change
        if level_one_score >= 100:
            change_to_inter()
    elif gameState == 'level 2':
        level_two_score += change
        if level_two_score >= 150:
            change_to_end()

def player_control():

    global player_pos

    basket = pygame.image.load("new_basket.png")
    basketrect = basket.get_rect()
    basketrect.x = player_pos.x
    basketrect.y = player_pos.y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if not player_pos.x < 0:
            player_pos.x -= player_speed
    if keys[ pygame.K_RIGHT] or keys[pygame.K_d]:
        if not player_pos.x > 850:
            player_pos.x += player_speed

    # Teleporting movement   
    # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    #     player_pos.x -= player_speed
    #     if player_pos.x<0:
    #         player_pos.x += SCREEN_WIDTH 
    # if keys[ pygame.K_RIGHT] or keys[pygame.K_d]:
    #     player_pos.x += player_speed
    #     if player_pos.x>1000:
    #         player_pos.x -= SCREEN_WIDTH

    frtrectlist = []
    for frt in fruit_dict:
        frtrectlist.append(frt['rect'])
    col_i = basketrect.collidelist(frtrectlist)
    if col_i != -1:
        print(fruit_dict[col_i]['name'])
        col_fruit = fruit_dict[col_i]['name']
        fruit_dict.pop(col_i)

        if cur_fruit == col_fruit:
            sound1=pygame.mixer.Sound("pling.mp3")
            sound1.play(loops=0, maxtime=0, fade_ms=0)
            print(f"curfruit is {cur_fruit} and fruit is {col_fruit}")
            score_change(10)
        elif col_fruit == 'bomb':
            sound2=pygame.mixer.Sound("small-explosion-129477.mp3")
            sound2.play(loops=0, maxtime=0, fade_ms=0)
            if gameState == 'level 2':
                score_change(-10)
            else:
                score_change(-5)
        else:
            score_change(5)

    screen.blit(basket, basketrect)

### FRUIT SPECIFIC FUNCTIONS ###

def fruit_generator():
    global fruit_dict, last_apple_time


    #calculate how many seconds
    seconds = (pygame.time.get_ticks()-start_tick)/1000

    if seconds - last_apple_time > spawn_rate:
        fruitlist = ["apple","banana","strawberry", "bomb", "bomb", "bomb"]
        a = random.randint(0,5)
        print(seconds)
        last_apple_time = seconds
        entry = {'name': fruitlist[a], 'loc': [random.randint(25,975), 0], 'rect': None}
        fruit_dict.append(entry)

        # Debug stuff
        # print(fruit_dict)

    
    for fl in fruit_dict:
        if fl['name'] == 'apple':
            frt = apfrt
        elif fl['name'] == 'banana':
            frt = bafrt
        elif fl['name'] == 'strawberry':
            frt = stfrt
        elif fl['name']=='bomb':
            frt=bomb
        

        frtrect = frt.get_rect()
        fl['rect'] = frtrect
        frtrect.x = fl['loc'][0]
        frtrect.y = fl['loc'][1]

        ## Update the falling for next round
        fl['loc'][1] = frtrect.y + fall_speed
        if frtrect.y > 650:
            fruit_dict.remove(fl)

        screen.blit(frt, frtrect)


# Here we'll put the fruit falling logic and then
# call them in the level functions

### GAME STATES ###

# The Start screen

sfont = pygame.font.Font('pixelify.ttf',50)
def mouse1():
    m=pygame.mouse.get_pos()
    if 410<m[0]<410+140 and 525<m[1]<525+80:
        pygame.draw.rect(screen, (135, 232, 97), (410, 525, 140, 80))
        button1()
        
def button1():
    b=sfont.render('START',True,(255,255,255))
    screen.blit(b,(410,535,100,50))

def change_to_l1():
    global game_start_time, cur_fruit
    pygame.mixer.music.load("music_lvl1.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
    set_state('level 1')
    fruitlist=["apple","banana","strawberry"]
    a=random.randint(0,2)
    cur_fruit = fruitlist[a]
    game_start_time = pygame.time.get_ticks()
    set_state('level 1')
    fruitlist=["apple","banana","strawberry"]
    a=random.randint(0,2)
    cur_fruit = fruitlist[a]
    game_start_time = pygame.time.get_ticks()

def startScreen():
    global game_start_time, cur_fruit

    # 135,232,97 substitue color
    # We should replace the plain blue with a proper title
    # and start button.
    screen.fill('blue')
    backimg(bckgrnd) 
    pygame.draw.rect(screen,(247, 159, 27),(410,525,140,80))
    button1()
    mouse1()

    moupos=pygame.mouse.get_pos()
    moupres=pygame.mouse.get_pressed()[0]
    is_hovered=(410<=moupos[0]<=410+140 and 525<=moupos[1]<=525+80)
    for eve in pygame.event.get():
        if eve.type == pygame.MOUSEBUTTONDOWN and is_hovered:
            change_to_l1()
# keys = pygame.key.get_pressed
#     if keys[pygame.MOUSEBUTTONDOWN]:
#         #print("Space pressed")
#         set_state('level 1')

def timer_disp(l_start):
    global hud_font

    time_left = (60000+(l_start - start_tick)-pygame.time.get_ticks())/1000
    time_text='Time left: '+str(time_left)
    if time_left > 0:
        timer=hud_font.render(time_text, True, (0,0,0))
        screen.blit(timer,(650,10))
    return time_left

def score_disp(l_score):
    score='Score: ' + str(l_score)
    text_image = hud_font.render(score, True, (0,0,0)) #Render text image.
    screen.blit(text_image, (40,10)) #Draw image to screen.

def add_score():
    global high_l1, high_l2
    try:
        file = open('save.txt','r+')
        scores = file.readline()
        score_list = scores.split()
        
        scorez = ""
        if int(score_list[0]) < level_one_score:
            scorez += str(level_one_score)+' '
            high_l1 = level_one_score
        else:
            scorez += str(score_list[0])+' '
            high_l1 = int(score_list[0])

        if int(score_list[1]) < level_two_score:
            scorez += str(level_two_score)+' '
            high_l2 = level_two_score
        else:
            scorez += str(score_list[1])+' '
            high_l2 = int(score_list[1])

        high_total = high_l1 + high_l2
        scorez += str(high_total)
        file.seek(0)
        file.write(scorez)
    except FileNotFoundError:
        file = open('save.txt', 'w+')
        file.write(str(level_one_score)+' '+str(level_two_score)+' '+str(level_one_score+level_two_score))

# Scene switchers

def change_to_inter():
    pygame.mixer.music.stop()
    set_state('inter')

# Level One Logic
def level_one():

    backimg(l1b) 
    time_left = timer_disp(game_start_time)
    score_disp(level_one_score)
    
    catch = "Catch only " + cur_fruit

    catch_text = hud_font.render(catch, True, (255,255,0)) #Render text image
    catch_rect= catch_text.get_rect()
    catch_rect.center = (1000// 2, 650// 2)
    screen.blit(catch_text,catch_rect)  # Draw text in the center
    keys = pygame.key.get_pressed()

    # Level over if timer reaches zero 
    if time_left<=0:
        change_to_inter()

    if keys[pygame.K_SPACE]:
        pygame.mixer.music.stop()
        print("Space pressed")
        print("State has been set ast inter.")
        set_state('inter')

    fruit_generator()
    player_control()

def change_to_l2():
    global lvl2_start_time, cur_fruit
    global fall_speed, spawn_rate
    print('Enter pressed')

    pygame.mixer.music.load("music_lvl2.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)

    fall_speed = 6
    spawn_rate = 1

    set_state('level 2')
    fruitlist=["apple","banana","strawberry"]
    a = random.randint(0,2)
    cur_fruit = fruitlist[a]
    lvl2_start_time = pygame.time.get_ticks()

def intermediate():

    screen.blit(lvlintr,(0,0))
    intr_font = pygame.font.Font('pixelify.ttf', 80)
    intr_scr = 'Score:' + str(level_one_score)
    intr_disp = intr_font.render(intr_scr,True,(46,0,32))
    intr_disp_shadow = intr_font.render(intr_scr,True,(255,99,71))
    screen.blit(intr_disp,(200,450))
    screen.blit(intr_disp_shadow, (205, 445))

    intr_nxt='Press "ENTER" for next level'
    intr_nfont = pygame.font.Font('pixelify.ttf', 20)
    intr_btm = intr_nfont.render(intr_nxt,True,(46,0,32))
    screen.blit(intr_btm,(350,600))
    key=pygame.key.get_pressed()

    if key[pygame.K_RETURN] or key[pygame.K_KP_ENTER]:
        change_to_l2()

def change_to_end():
    pygame.mixer.music.stop()
    set_state('end')

def level_two():

    backimg(l2b)
    tl = timer_disp(lvl2_start_time)
    score_disp(level_two_score)
    
    catch2 = "Catch only " + cur_fruit
    catch_text2 = hud_font.render(catch2,True,(255,255,0)) #Render text image
    catch_rect2= catch_text2.get_rect()
    catch_rect2.center = (1000// 2, 650// 2)
    screen.blit(catch_text2,catch_rect2)  # Draw text in the center
    #keys = pygame.key.get_pressed()
    if tl<=0:
        change_to_end()
    player_control()
    fruit_generator()

## New end screen

def end_screen():

    add_score()

    mpos=pygame.mouse.get_pos()
    mpres=pygame.mouse.get_pressed()[0]
    print("End screen called")
    gamovr=pygame.image.load('final_background image.png')
    gameover= gamovr.get_rect()
    screen.fill('yellow')
    screen.blit(gamovr,gameover)

    qtext = hud_font.render('QUIT', True, (10,10,10))
    pygame.draw.rect(screen,(33,94,97),(550,575,83,50))
    screen.blit(qtext, (550,575))
    quitrect = qtext.get_rect()
    quitrect.topleft = (550, 575)

    #displaying score
    l1 = level_one_score
    l2 = level_two_score
    highl1 = high_l1
    highl2 = high_l2
    sumyour=l1+l2
    sumhigh=highl1+highl2

    l1dis=hud_font.render(str(l1), True, (10,10,10))
    l2dis=hud_font.render(str(l2), True, (10,10,10))
    highl1dis=hud_font.render(str(highl1), True, (10,10,10))
    highl2dis=hud_font.render(str(highl2), True, (10,10,10))
    sumyourdis=hud_font.render(str(sumyour), True, (10,10,10))
    sumhighdis=hud_font.render(str(sumhigh), True, (10,10,10))

    l1dis_rect= l1dis.get_rect()
    l1dis_rect.center = (490,275)
    screen.blit(l1dis,l1dis_rect)

    l2dis_rect= l2dis.get_rect()
    l2dis_rect.center = (490,352)
    screen.blit(l2dis,l2dis_rect)

    highl1dis_rect= highl1dis.get_rect()
    highl1dis_rect.center = (621,275)
    screen.blit(highl1dis,highl1dis_rect)

    highl2dis_rect=highl2dis.get_rect()
    highl2dis_rect.center = (621,352)
    screen.blit(highl2dis,highl2dis_rect)

    sumyourdisdis_rect= sumyourdis.get_rect()
    sumyourdisdis_rect.center = (490,428)
    screen.blit(sumyourdis,sumyourdisdis_rect)

    sumhighdis_rect=sumhighdis.get_rect()
    sumhighdis_rect.center = (621,428)
    screen.blit(sumhighdis,sumhighdis_rect)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if quitrect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


### MAIN GAME LOOP ###
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if gameState == 'start':
        startScreen()
    elif gameState == 'level 1':
        level_one()
    elif gameState == 'inter':
        intermediate()
    elif gameState == 'level 2':
        level_two()
    elif gameState == 'end':
        end_screen()

    pygame.display.flip()
    clock.tick(FPS)


# Stuff to refer
# Video showing how to manage game states
# https://www.youtube.com/watch?v=r0ixaTQxsUI
# But this guys uses actual classes, which we are not gonna use.
