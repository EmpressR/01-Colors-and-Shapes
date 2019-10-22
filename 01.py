import random


class Object:
    def __init__(self, color, shape, bg, name):
        self.color = color
        self.shape = shape
        self.bg = bg
        self.name = name


# ------------------------------------------------------------------------
r_c_w = Object("red", "circle", "wbg", "RedCircleWhite")
r_c_b = Object("red", "circle", "bbg", "RedCircleBlack")
r_c_g = Object("red", "circle", "gbg", "RedCircleGray")

r_s_w = Object("red", "square", "wbg", "RedSquareWhite")
r_s_b = Object("red", "square", "bbg", "RedSquareBlack")
r_s_g = Object("red", "square", "gbg", "RedSquareGray")

r_t_w = Object("red", "triangle", "wbg", "RedTriangleWhite")
r_t_b = Object("red", "triangle", "bbg", "RedTriangleBlack")
r_t_g = Object("red", "triangle", "gbg", "RedTriangleGray")
# ----------------------------------------------------
b_c_w = Object("blue", "circle", "wbg", "BlueCircleWhite")
b_c_b = Object("blue", "circle", "bbg", "BlueCircleBlack")
b_c_g = Object("blue", "circle", "gbg", "BlueCircleGray")

b_s_w = Object("blue", "square", "wbg", "BlueSquareWhite")
b_s_b = Object("blue", "square", "bbg", "BlueSquareBlack")
b_s_g = Object("blue", "square", "gbg", "BlueSquareGray")

b_t_w = Object("blue", "triangle", "wbg", "BlueTriangleWhite")
b_t_b = Object("blue", "triangle", "bbg", "BlueTriangleBlack")
b_t_g = Object("blue", "triangle", "gbg", "BlueTriangleGray")
# ----------------------------------------------------
y_c_w = Object("yellow", "circle", "wbg", "YellowCircleWhite")
y_c_b = Object("yellow", "circle", "bbg", "YellowCircleBlack")
y_c_g = Object("yellow", "circle", "gbg", "YellowCircleGray")

y_s_w = Object("yellow", "square", "wbg", "YellowSquareWhite")
y_s_b = Object("yellow", "square", "bbg", "YellowSquareBlack")
y_s_g = Object("yellow", "square", "gbg", "YellowSquareGray")

y_t_w = Object("yellow", "triangle", "wbg", "YellowTriangleWhite")
y_t_b = Object("yellow", "triangle", "bbg", "YellowTriangleBlack")
y_t_g = Object("yellow", "triangle", "gbg", "YellowTriangleGray")
# ------------------------------------------------------------------------

my_objects = (
    (r_c_w, r_c_b, r_c_g, r_s_w, r_s_b, r_s_g, r_t_w, r_t_b, r_t_g,
     b_c_w, b_c_b, b_c_g, b_s_w, b_s_b, b_s_g, b_t_w, b_t_b, b_t_g,
     y_s_w, y_s_b, y_s_g, y_s_w, y_s_b, y_s_w, y_t_w, y_t_b, y_t_g))

# ------------------------------------------------------------------------


def new_game_easy():

    easy_points = 0
    easy_health = 3
    level_start(easy_points, easy_health)


# ------------------------------------------------------------------------


def level_start(points, health_points):

    a1 = random.choice(my_objects)
    a2 = random.choice(my_objects)
    a3 = random.choice(my_objects)
    b1 = random.choice(my_objects)
    b2 = random.choice(my_objects)
    b3 = random.choice(my_objects)
    c1 = random.choice(my_objects)
    c2 = random.choice(my_objects)
    c3 = random.choice(my_objects)

    game_board = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    click1 = random.choice(game_board)

    game_board2 = []
    for piece in game_board:
        if piece != click1:
            game_board2.append(piece)
    click2 = random.choice(game_board2)

    game_board3 = []
    for piece in game_board2:
        if piece != click2:
            game_board3.append(piece)
    click3 = random.choice(game_board3)
    print(f"Choices were: {click1.name}, {click2.name}, {click3.name}")
    choice(click1, click2, click3, points, health_points)

# ------------------------------------------------------------------------


def game_over():

    print("Game Over!")

# ------------------------------------------------------------------------


def choice(click1, click2, click3, points, health_points):

    if all([click1.color == click2.color, click1.color == click3.color,
            click1.shape == click2.shape, click1.shape == click3.shape]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level_start(points, health_points)

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level_start(points, health_points)

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level_start(points, health_points)

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level_start(points, health_points)

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level_start(points, health_points)

    elif all([click1.bg == click2.bg, click1 == click3.bg,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level_start(points, health_points)

    elif all([click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level_start(points, health_points)

    else:
        health_points -= 1
        print(f"{click1.name} and {click2.name} and {click3.name} are not a match! Health points: {health_points}")
        if health_points == 0:
            game_over()
        else:
            level_start(points, health_points)


# ------------------------------------------------------------------------

new_game_easy()
