import random
import curses
import time


##use curses to initialize the screen
s = curses.initscr()
curses.curs_set(0)
##get width and height from the maximum screen values
sh, sw = s.getmaxyx()
##create a new window using height and width that opens in top right hand corner of screen
w = curses.newwin(sh, sw, 0, 0)
##let it accept keypad input
w.keypad(1)
w.timeout(100)

score = 0

##create snakes initial position
snk_x = sw/4
snk_y = sh/2

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), "*")

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    #create the conditions for when the player loses(ie snake runs out of bounds, eats itself, etc)
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        w.addstr(int(sh/2), int(sw/2), "Your final score is: " + str(score))
        w.refresh()
        time.sleep(3)
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    #using keyboard input to move the snake
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    #when the snake eats the food, generate a new piece of food
    if snake[0] == food:
        food = None
        score += 1
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], "*")
    #otherwise the snake continues on its merry way
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)


