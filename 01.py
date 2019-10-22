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


# ------------------------------------------------------------------------


def new_game_easy():

    easy_points = 0
    easy_health = 3
    create_board(easy_points, easy_health)

# ------------------------------------------------------------------------


def create_board(points, health_points):

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
           f" G) {c1.name}, H) {c2.name}, I) {c3.name}"])
    choice_count = 0
    made_choices = []
    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    cl1 = input("> ")

    if cl1 == "A":
        click1 = a1

    if cl1 == "B":
        click1 = a2

    if cl1 == "C":
        click1 = a3

    if cl1 == "D":
        click1 = b1

    if cl1 == "E":
        click1 = b2

    if cl1 == "F":
        click1 = b3

    if cl1 == "G":
        click1 = c1

    if cl1 == "H":
        click1 = c2

    if cl1 == "I":
        click1 = c3

    # make click1 unusable
    cl2 = input("> ")

    if cl2 == "A":
        click2 = a1

    if cl2 == "B":
        click2 = a2

    if cl2 == "C":
        click2 = a3

    if cl2 == "D":
        click2 = b1

    if cl2 == "E":
        click2 = b2

    if cl2 == "F":
        click2 = b3

    if cl2 == "G":
        click2 = c1

    if cl2 == "H":
        click2 = c2

    if cl2 == "I":
        click2 = c3

    # make click2 unusable
    cl3 = input("> ")

    if cl3 == "A":
        click3 = a1

    if cl3 == "B":
        click3 = a2

    if cl3 == "C":
        click3 = a3

    if cl3 == "D":
        click3 = b1

    if cl3 == "E":
        click3 = b2

    if cl3 == "F":
        click3 = b3

    if cl3 == "G":
        click3 = c1

    if cl3 == "H":
        click3 = c2

    if cl3 == "I":
        click3 = c3

    print(f"Choices were: {click1.name}, {click2.name}, {click3.name}")

    if choice_count > 0:
        choice_count += 1
        made_choices += click1, click2, click3
        same_choices(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)
    else:
        choice_count += 1
        made_choices += click1, click2, click3

    choice(click1, click2, click3, points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
           choice_count, made_choices)

# ------------------------------------------------------------------------


# ------------------------------------------------------------------------


def same_choices(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    made_choices1 = [made_choices[0], made_choices[1], made_choices[2]]
    for made_choice in made_choices1:
        if made_choices[-1] == made_choice:
            for made_choice2 in made_choices1:
                if made_choices[-2] == made_choice2:
                    for made_choice3 in made_choices1:
                        if made_choices[-3] == made_choice3:
                            print("Combination already used!")
                            health_points -= 1
                            if health_points == 0:
                                game_over()
                            else:
                                level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                      choice_count, made_choices)

    if len(made_choices) > 6:
        made_choices2 = [made_choices[3], made_choices[4], made_choices[5]]
        for made_choice in made_choices2:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices2:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices2:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 9:
        made_choices3 = [made_choices[6], made_choices[7], made_choices[8]]
        for made_choice in made_choices3:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices3:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices3:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 12:
        made_choices4 = [made_choices[9], made_choices[10], made_choices[11]]
        for made_choice in made_choices4:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices4:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices4:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 15:
        made_choices5 = [made_choices[12], made_choices[13], made_choices[14]]
        for made_choice in made_choices5:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices5:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices5:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)
    if len(made_choices) > 18:
        made_choices6 = [made_choices[15], made_choices[16], made_choices[17]]
        for made_choice in made_choices6:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices6:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices6:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 21:
        made_choices7 = [made_choices[18], made_choices[19], made_choices[20]]
        for made_choice in made_choices7:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices7:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices7:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 24:
        made_choices8 = [made_choices[21], made_choices[22], made_choices[23]]
        for made_choice in made_choices8:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices8:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices8:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 27:
        made_choices9 = [made_choices[24], made_choices[25], made_choices[26]]
        for made_choice in made_choices9:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices9:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices9:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 30:
        made_choices10 = [made_choices[27], made_choices[28], made_choices[29]]
        for made_choice in made_choices10:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices10:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices10:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

    if len(made_choices) > 33:
        made_choices11 = [made_choices[30], made_choices[31], made_choices[32]]
        for made_choice in made_choices11:
            if made_choices[-1] == made_choice:
                for made_choice2 in made_choices11:
                    if made_choices[-2] == made_choice2:
                        for made_choice3 in made_choices11:
                            if made_choices[-3] == made_choice3:
                                print("Combination already used!")
                                health_points -= 1
                                if health_points == 0:
                                    game_over()
                                else:
                                    level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)

# ------------------------------------------------------------------------


def game_over():

    print("Game Over!")
    print("New game started!")
    new_game_easy()

# ------------------------------------------------------------------------


def choice(click1, click2, click3, points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3,
           choice_count, made_choices):

    if all([click1.color == click2.color, click1.color == click3.color,
            click1.shape == click2.shape, click1.shape == click3.shape]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.bg == click2.bg, click1 == click3.bg,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        points += 1
        print(f"{click1.name} and {click2.name} and {click3.name} points: {points}")
        level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    else:
        health_points -= 1
        print(f"{click1.name} and {click2.name} and {click3.name} are not a match! Health points: {health_points}")
        if health_points == 0:
            game_over()
        else:
            level(points, health_points, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)


# ------------------------------------------------------------------------

new_game_easy()
