import random

colors = ["red", "blue", "yellow"]
shapes = ["circle", "square", "triangle"]
bgs = ["wbg", "bbg", "gbg"]

# -------------------------------------------------------------------


def make_object(ob_lst):

    ob_lst1 = random.choice(colors)
    ob_lst2 = random.choice(shapes)
    ob_lst3 = random.choice(bgs)
    ob_lst = [ob_lst1, ob_lst2, ob_lst3]
    return ob_lst

# -------------------------------------------------------------------


def create_a1(ob_lst):

    a1 = make_object(ob_lst)
    return a1


def create_a2(ob_lst):

    a2 = make_object(ob_lst)
    return a2


def create_a3(ob_lst):

    a3 = make_object(ob_lst)
    return a3


def create_b1(ob_lst):

    b1 = make_object(ob_lst)
    return b1


def create_b2(ob_lst):

    b2 = make_object(ob_lst)
    return b2


def create_b3(ob_lst):

    b3 = make_object(ob_lst)
    return b3


def create_c1(ob_lst):
    c1 = make_object(ob_lst)
    return c1


def create_c2(ob_lst):
    c2 = make_object(ob_lst)
    return c2


def create_c3(ob_lst):
    c3 = make_object(ob_lst)
    return c3

# ------------------------------------------------------------------------


def check_dup(a1, a2, a3, b1, b2, b3, c1, c2, c3, ob_lst):

    if a2 == a1:
        create_a2(ob_lst)
    elif a3 == any([a1, a2]):
        create_a3(ob_lst)
    elif b1 == any([a1, a2, a3]):
        create_b1(ob_lst)
    elif b2 == any([a1, a2, a3, b1]):
        create_b2(ob_lst)
    elif b3 == any([a1, a2, a3, b1, b2]):
        create_b3(ob_lst)
    elif c1 == any([a1, a2, a3, b1, b2, b3]):
        create_c1(ob_lst)
    elif c2 == any([a1, a2, a3, b1, b2, b3, c1]):
        create_c2(ob_lst)
    elif c3 == any([a1, a2, a3, b1, b2, b3, c1, c2]):
        create_c3(ob_lst)
    else:
        return a1, a2, a3, b1, b2, b3, c1, c2, c3
# ------------------------------------------------------------------------


def new_game_easy():

    easy_points = 0
    easy_health = 3
    create_board(easy_points, easy_health)

# ------------------------------------------------------------------------


def create_board(points, hp):
    ob_lst = []
    a1, a2, a3, b1, b2, b3, c1, c2, c3 = check_dup(create_a1(ob_lst), create_a2(ob_lst), create_a3(ob_lst),
                                                   create_b1(ob_lst), create_b2(ob_lst), create_b3(ob_lst),
                                                   create_c1(ob_lst), create_c2(ob_lst), create_c3(ob_lst))
    choice_count = 0
    made_choices = []
    print([f"A) {a1}, B) {a2}, C) {a3}, D) {b1}, E) {b2}, "
           f"F) {b3}, G) {c1}, H) {c2}, I) {c3}"])
    level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

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

    print(f"Choices were: {click1}, {click2}, {click3}")

    if choice_count > 0:
        choice_count += 1
        made_choices += click1, click2, click3
        same_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)
    else:
        choice_count += 1
        made_choices += click1, click2, click3

    choice(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
           choice_count, made_choices)

# ------------------------------------------------------------------------


def same_choices2(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
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
                                choice_count2 + 1
                                if choice_count2 == 1:
                                    if len(made_choices) > 6:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 2:
                                    if len(made_choices) > 9:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 3:
                                    if len(made_choices) > 12:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 4:
                                    if len(made_choices) > 15:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 5:
                                    if len(made_choices) > 18:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 6:
                                    if len(made_choices) > 21:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 7:
                                    if len(made_choices) > 24:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 8:
                                    if len(made_choices) > 27:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 9:
                                    if len(made_choices) > 30:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                elif choice_count2 == 10:
                                    if len(made_choices) > 33:
                                        len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                                         choice_count, choice_count2, made_choices)
                                else:
                                    level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                                          choice_count, made_choices)
        else:
            choice_count2 + 1

    if choice_count2 == 1:
        if len(made_choices) > 6:
            len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                             choice_count, choice_count2, made_choices)

    else:
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


def same_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    choice_count2 = 0
    made_choices1 = [made_choices[0], made_choices[1], made_choices[2]]
    same_choices2(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                  choice_count, choice_count2, made_choices, made_choices1)

# ------------------------------------------------------------------------


def len_made_choices(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                     choice_count, choice_count2, made_choices):

    if choice_count2 == 1:
        made_choices1 = made_choices[3:6]
    elif choice_count2 == 2:
        made_choices1 = made_choices[6:9]
    elif choice_count2 == 3:
        made_choices1 = made_choices[9:12]
    elif choice_count2 == 4:
        made_choices1 = made_choices[12:15]
    elif choice_count2 == 5:
        made_choices1 = made_choices[15:18]
    elif choice_count2 == 6:
        made_choices1 = made_choices[18:21]
    elif choice_count2 == 7:
        made_choices1 = made_choices[21:24]
    elif choice_count2 == 8:
        made_choices1 = made_choices[24:27]
    elif choice_count2 == 9:
        made_choices1 = made_choices[27:30]
    elif choice_count2 == 10:
        made_choices1 = made_choices[30:33]

    same_choices2(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                  choice_count, choice_count2, made_choices, made_choices1)

# ------------------------------------------------------------------------


def game_over():

    print("Game Over!")
    print("New game started!")
    new_game_easy()

# ------------------------------------------------------------------------


def choice(click1, click2, click3, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
           choice_count, made_choices):

    if all([click1[0] == click2[0], click1[0] == click3[0],
            click1[1] == click2[1], click1[1] == click3[1]]):
        points += 1
        print(f"{click1} and {click2} and {click3} points: {points}")
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1[0] == click2[0], click1[0] == click3[0],
              click1[2] == click2[2], click1[2] == click3[2]]):
        points += 1
        print(f"{click1} and {click2} and {click3} points: {points}")
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1[1] == click2[1], click1[1] == click3[1],
              click1[2] == click2[2], click1[2] == click3[2]]):
        points += 1
        print(f"{click1} and {click2} and {click3} points: {points}")
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1[0] == click2[0], click1[0] == click3[0],
              click1[1] != click2[1], click1[1] != click3[1], click2[1] != click3[1],
              click1[2] != click2[2], click1[2] != click3[2], click2[2] != click3[2]]):
        points += 1
        print(f"{click1} and {click2} and {click3} points: {points}")
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1[1] == click2[1], click1[1] == click3[1],
              click1[0] != click2[0], click1[0] != click3[0], click2[0] != click3[0],
              click1[2] != click2[2], click1[2] != click3[2], click2[2] != click3[2]]):
        points += 1
        print(f"{click1} and {click2} and {click3} points: {points}")
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1[2] == click2[2], click1[2] == click3[2],
              click1[1] != click2[1], click1[1] != click3[1], click2[1] != click3[1],
              click1[0] != click2[0], click1[0] != click3[0], click2[0] != click3[0]]):
        points += 1
        print(f"{click1} and {click2} and {click3} points: {points}")
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    elif all([click1[0] != click2[0], click1[0] != click3[0], click2[0] != click3[0],
              click1[1] != click2[1], click1[1] != click3[1], click2[1] != click3[1],
              click1[2] != click2[2], click1[2] != click3[2], click2[2] != click3[2]]):
        points += 1
        print(f"{click1} and {click2} and {click3} points: {points}")
        level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

    else:
        hp -= 1
        print(f"{click1} and {click2} and {click3} are not a match! Health points: {hp}")
        if hp == 0:
            game_over()
        else:
            level(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices)

# ------------------------------------------------------------------------


new_game_easy()
