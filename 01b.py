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
     y_c_w, y_c_b, y_c_g, y_s_w, y_s_b, y_s_g, y_t_w, y_t_b, y_t_g))

# ------------------------------------------------------------------------


def new_game_easy():

    easy_points = 0
    easy_health = 3
    create_board(easy_points, easy_health)

# ------------------------------------------------------------------------


def create_board(points, hp):

    board = []
    for piece in my_objects:
        board.append(piece)

    a1 = random.choice(board)
    board.remove(a1)

    a2 = random.choice(board)
    board.remove(a2)

    a3 = random.choice(board)
    board.remove(a3)

    b1 = random.choice(board)
    board.remove(b1)

    b2 = random.choice(board)
    board.remove(b2)

    b3 = random.choice(board)
    board.remove(b3)

    c1 = random.choice(board)
    board.remove(c1)

    c2 = random.choice(board)
    board.remove(c2)

    c3 = random.choice(board)

    print([f"A) {a1.name}, B) {a2.name}, C) {a3.name}, D) {b1.name}, E) {b2.name}, F) {b3.name}, "
           f" G) {c1.name}, H) {c2.name}, I) {c3.name}, N) No possible matches"])
    choice_count = 0
    made_choices = []
    level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    click1 = inputs(input("> "), points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    click2 = inputs(input("> "), points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    click3 = inputs(input("> "), points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    print(f"Choices were: {click1.name}, {click2.name} and {click3.name}")

    checking = False
    choice(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
           choice_count, made_choices, checking)

# ------------------------------------------------------------------------


def inputs(cl, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    letters = {
        "A": a1,
        "B": a2,
        "C": a3,
        "D": b1,
        "E": b2,
        "F": b3,
        "G": c1,
        "H": c2,
        "I": c3,
        "N": "N"
    }
    for letter in letters:
        if cl == letter:
            click = letters.get(letter)
            if click == "N":
                no_matches(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)
            return click

# ------------------------------------------------------------------------


def no_matches(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    more_matches = False
    check_matches(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)
    if more_matches:
        hp -= 1
        print(f"There are still matches! Health points: {hp}")
        if hp == 0:
            game_over()
        else:
            level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)
    else:
        points += 2
        print(f"There are no more matches! Points: {points}")
        create_board(points, hp)


new_game_easy()
