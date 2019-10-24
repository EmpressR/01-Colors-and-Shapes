from random import choice
from itertools import combinations


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

    a1 = choice(board)
    board.remove(a1)

    a2 = choice(board)
    board.remove(a2)

    a3 = choice(board)
    board.remove(a3)

    b1 = choice(board)
    board.remove(b1)

    b2 = choice(board)
    board.remove(b2)

    b3 = choice(board)
    board.remove(b3)

    c1 = choice(board)
    board.remove(c1)

    c2 = choice(board)
    board.remove(c2)

    c3 = choice(board)

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
    choice1(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
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


def no_matches(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    if check_matches(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):
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

# ------------------------------------------------------------------------


def check_matches(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    checking = True
    used_board = [a1, a2, a3, b1, b2, b3, c1, c2, c3]

    for x, y, z in combinations(used_board, 3):
        print(zip(made_choices*3))
        if any([(x, y, z), (x, z, y), (z, x, y), (z, y, x), [y, x, z], (y, z, x)]) not in zip(made_choices*3):
            yes = choice1(x, y, z, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                          choice_count, made_choices, checking)
            if yes:
                print("True")
                return True
    return False
# ------------------------------------------------------------------------


def choice1(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
            choice_count, made_choices, checking):

    if all([click1.color == click2.color, click1.color == click3.color,
            click1.shape == click2.shape, click1.shape == click3.shape]):
        if checking:
            return True
        else:
            choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        if checking:
            return True
        else:
            choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        if checking:
            return True
        else:
            choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        if checking:
            return True
        else:
            choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        if checking:
            return True
        else:
            choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.bg == click2.bg, click1.bg == click3.bg,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color]):
        if checking:
            return True
        else:
            choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        if checking:
            return True
        else:
            choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    else:
        if checking:
            return False
        else:
            hp -= 1
            print(f"{click1.name} and {click2.name} and {click3.name} are not a match! Health points: {hp}")
            if hp == 0:
                game_over()
            else:
                level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def choice2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    choice_count += 1
    made_choices += click1, click2, click3
    same_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def same_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    if choice_count > 1:
        choice_count2 = 0
        made_choices1 = [made_choices[0], made_choices[1], made_choices[2]]
        same_choices2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                      choice_count, choice_count2, made_choices, made_choices1)
    else:
        points_reward(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                      choice_count, made_choices)

# ------------------------------------------------------------------------


def same_choices2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                  choice_count, choice_count2, made_choices, made_choices1):

    for made_choice in made_choices1:
        if made_choices[-1] == made_choice:
            for made_choice2 in made_choices1:
                if made_choices[-2] == made_choice2:
                    for made_choice3 in made_choices1:
                        if made_choices[-3] == made_choice3:
                            hp -= 1
                            print(f"Combination already used! Health points: {hp}")
                            if hp == 0:
                                game_over()
                            else:
                                made_choices = made_choices[:-3]
                                level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)
    choice_count2 += 1

    if choice_count2 == 1:
        if len(made_choices) > 6:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 2:
        if len(made_choices) > 9:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 3:
        if len(made_choices) > 12:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 4:
        if len(made_choices) > 15:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 5:
        if len(made_choices) > 18:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 6:
        if len(made_choices) > 21:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 7:
        if len(made_choices) > 24:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 8:
        if len(made_choices) > 27:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 9:
        if len(made_choices) > 30:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    if choice_count2 == 10:
        if len(made_choices) > 33:
            len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)
    else:
        points_reward(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count,
                      made_choices)
    points_reward(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def points_reward(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):
    points += 1
    print(f"{click1.name}, {click2.name} and {click3.name} points: {points}")
    level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def len_made_choices(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                     choice_count, choice_count2, made_choices):

    if choice_count2 == 1:
        made_choices1 = made_choices[3:6]
    if choice_count2 == 2:
        made_choices1 = made_choices[6:9]
    if choice_count2 == 3:
        made_choices1 = made_choices[9:12]
    if choice_count2 == 4:
        made_choices1 = made_choices[12:15]
    if choice_count2 == 5:
        made_choices1 = made_choices[15:18]
    if choice_count2 == 6:
        made_choices1 = made_choices[18:21]
    if choice_count2 == 7:
        made_choices1 = made_choices[21:24]
    if choice_count2 == 8:
        made_choices1 = made_choices[24:27]
    if choice_count2 == 9:
        made_choices1 = made_choices[27:30]
    if choice_count2 == 10:
        made_choices1 = made_choices[30:33]

    same_choices2(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                  choice_count, choice_count2, made_choices, made_choices1)

# ------------------------------------------------------------------------


def game_over():

    print("Game Over!")
    print("New game started!")
    new_game_easy()

# ------------------------------------------------------------------------


new_game_easy()
