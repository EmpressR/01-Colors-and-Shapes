from random import choice
from itertools import combinations
import my_library
import easy


# ------------------------------------------------------------------------


def create_board(points, hp):

    board = []
    for piece in my_library.my_objects:
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
    print(f"{a1.name}, {a2.name}, {a3.name}, {b1.name}, {b2.name}, {b3.name}, "
           f" {c1.name}, {c2.name}, {c3.name}")
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
# example made_choices a1, a2, a3, .. a1, a2, b1, .. a1, a2, b2, ...


def check_matches(points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3, choice_count, made_choices):

    checking = True
    used_board = [a1, a2, a3, b1, b2, b3, c1, c2, c3]

    for a, b, c in combinations(used_board, 3):
        if not made_choices:
            print(a.name, b.name, c.name)
            yes = choice1(a, b, c, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
                          choice_count, made_choices, checking)
            if yes:
                print("True")
                return True
        else:
            print("It is here")
            print(a.name, b.name, c.name)
            temp = [a, b, c]
            temp2 = [a, c, b]
            temp3 = [b, a, c]
            temp4 = [b, c, a]
            temp5 = [c, a, b]
            temp6 = [c, b, a]

            temp_count = 0
            temp_list0_2 = []
            temp_list3_5 = []
            temp_list6_8 = []
            temp_list9_11 = []
            temp_list12_14 = []
            temp_list15_17 = []
            temp_list18_20 = []
            temp_list21_23 = []
            temp_list24_26 = []
            temp_list27_29 = []
            temp_list30_32 = []
            temp_list33_35 = []

            for i in made_choices:
                if temp_count < 3:
                    temp_list0_2.append(i)
                    temp_count += 1
                elif temp_count < 6:
                    temp_list3_5.append(i)
                    temp_count += 1
                elif temp_count < 9:
                    temp_list6_8.append(i)
                    temp_count += 1
                elif temp_count < 12:
                    temp_list9_11.append(i)
                    temp_count += 1
                elif temp_count < 15:
                    temp_list12_14.append(i)
                    temp_count += 1
                elif temp_count < 18:
                    temp_list15_17.append(i)
                    temp_count += 1
                elif temp_count < 21:
                    temp_list18_20.append(i)
                    temp_count += 1
                elif temp_count < 24:
                    temp_list21_23.append(i)
                    temp_count += 1
                elif temp_count < 27:
                    temp_list24_26.append(i)
                    temp_count += 1
                elif temp_count < 30:
                    temp_list27_29.append(i)
                    temp_count += 1
                elif temp_count < 33:
                    temp_list30_32.append(i)
                    temp_count += 1
                else:
                    temp_list33_35.append(i)

            combined_temp = [temp_list0_2, temp_list3_5, temp_list6_8, temp_list9_11, temp_list12_14, temp_list15_17,
                             temp_list18_20, temp_list21_23, temp_list24_26, temp_list27_29, temp_list30_32,
                             temp_list33_35]

            if temp in combined_temp:
                print("It was here1")
                continue
            elif temp2 in combined_temp:
                print("It was here2")
                continue
            elif temp3 in combined_temp:
                print("It was here3")
                continue
            elif temp4 in combined_temp:
                print("It was here4")
                continue
            elif temp5 in combined_temp:
                print("It was here5")
                continue
            elif temp6 in combined_temp:
                print("It was here6")
                continue
            else:
                print("Goes to choice")
                yes = choice1(a, b, c, points, hp, a1, a2, a3, b1, b2, b3, c1, c2, c3,
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
    easy.new_game_easy()

# ------------------------------------------------------------------------


