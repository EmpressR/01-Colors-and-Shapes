from itertools import combinations


class Object:
    def __init__(self, color, shape, bg, name):
        self.color = color
        self.shape = shape
        self.bg = bg
        self.name = name


# ------------------------------------------------------------------------
RedCircleWhite = Object("red", "circle", "wbg", "RedCircleWhite")
RedCircleBlack = Object("red", "circle", "bbg", "RedCircleBlack")
RedCircleGray = Object("red", "circle", "gbg", "RedCircleGray")

RedSquareWhite = Object("red", "square", "wbg", "RedSquareWhite")
RedSquareBlack = Object("red", "square", "bbg", "RedSquareBlack")
RedSquareGray = Object("red", "square", "gbg", "RedSquareGray")

RedTriangleWhite = Object("red", "triangle", "wbg", "RedTriangleWhite")
RedTriangleBlack = Object("red", "triangle", "bbg", "RedTriangleBlack")
RedTriangleGray = Object("red", "triangle", "gbg", "RedTriangleGray")
# ----------------------------------------------------
BlueCircleWhite = Object("blue", "circle", "wbg", "BlueCircleWhite")
BlueCircleBlack = Object("blue", "circle", "bbg", "BlueCircleBlack")
BlueCircleGray = Object("blue", "circle", "gbg", "BlueCircleGray")

BlueSquareWhite = Object("blue", "square", "wbg", "BlueSquareWhite")
BlueSquareBlack = Object("blue", "square", "bbg", "BlueSquareBlack")
BlueSquareGray = Object("blue", "square", "gbg", "BlueSquareGray")

BlueTriangleWhite = Object("blue", "triangle", "wbg", "BlueTriangleWhite")
BlueTriangleBlack = Object("blue", "triangle", "bbg", "BlueTriangleBlack")
BlueTriangleGray = Object("blue", "triangle", "gbg", "BlueTriangleGray")
# ----------------------------------------------------
YellowCircleWhite = Object("yellow", "circle", "wbg", "YellowCircleWhite")
YellowCircleBlack = Object("yellow", "circle", "bbg", "YellowCircleBlack")
YellowCircleGray = Object("yellow", "circle", "gbg", "YellowCircleGray")

YellowSquareWhite = Object("yellow", "square", "wbg", "YellowSquareWhite")
YellowSquareBlack = Object("yellow", "square", "bbg", "YellowSquareBlack")
YellowSquareGray = Object("yellow", "square", "gbg", "YellowSquareGray")

YellowTriangleWhite = Object("yellow", "triangle", "wbg", "YellowTriangleWhite")
YellowTriangleBlack = Object("yellow", "triangle", "bbg", "YellowTriangleBlack")
YellowTriangleGray = Object("yellow", "triangle", "gbg", "YellowTriangleGray")
# ------------------------------------------------------------------------


def check_matches(a1, a2, a3, b1, b2, b3, c1, c2, c3):

    made_choices = []
    used_board = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    a1.name = "A"
    a2.name = "B"
    a3.name = "C"
    b1.name = "D"
    b2.name = "E"
    b3.name = "F"
    c1.name = "G"
    c2.name = "H"
    c3.name = "I"
#    n = 3
#    split_made_choices = zip(*(iter(range(len(made_choices))),) * n)

    for a, b, c in combinations(used_board, 3):
        if not made_choices:
            yes = choice1(a, b, c)
            if yes:
                made_choices += [a, b, c]

        else:
            temp = [a, b, c]
            temp2 = [a, c, b]
            temp3 = [b, a, c]
            temp4 = [b, c, a]
            temp5 = [c, a, b]
            temp6 = [c, b, a]

            if temp in made_choices:
                continue
            elif temp2 in made_choices:
                continue
            elif temp3 in made_choices:
                continue
            elif temp4 in made_choices:
                continue
            elif temp5 in made_choices:
                continue
            elif temp6 in made_choices:
                continue
            else:
                yes = choice1(a, b, c)
                if yes:
                    made_choices += [a, b, c]

    temp_count = 0

    for j in made_choices:
        temp_count += 1

    print(temp_count)

# ------------------------------------------------------------------------


def choice1(click1, click2, click3):

    if all([click1.color == click2.color, click1.color == click3.color,
            click1.shape == click2.shape, click1.shape == click3.shape]):
        print(f"{click1.name}, {click2.name}, {click3.name}")
        return True

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        print(f"{click1.name}, {click2.name}, {click3.name}")
        return True

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.bg == click2.bg, click1.bg == click3.bg]):
        print(f"{click1.name}, {click2.name}, {click3.name}")
        return True

    elif all([click1.color == click2.color, click1.color == click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        print(f"{click1.name}, {click2.name}, {click3.name}")
        return True

    elif all([click1.shape == click2.shape, click1.shape == click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        print(f"{click1.name}, {click2.name}, {click3.name}")
        return True

    elif all([click1.bg == click2.bg, click1.bg == click3.bg,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.color != click2.color, click1.color != click3.color, click2.color != click3.color]):
        print(f"{click1.name}, {click2.name}, {click3.name}")
        return True

    elif all([click1.color != click2.color, click1.color != click3.color, click2.color != click3.color,
              click1.shape != click2.shape, click1.shape != click3.shape, click2.shape != click3.shape,
              click1.bg != click2.bg, click1.bg != click3.bg, click2.bg != click3.bg]):
        print(f"{click1.name}, {click2.name}, {click3.name}")
        return True

    else:
        return False

# ------------------------------------------------------------------------


check_matches(YellowCircleWhite, BlueTriangleWhite, RedSquareBlack, YellowCircleBlack, RedCircleGray, YellowTriangleWhite,  YellowTriangleGray, RedTriangleBlack, YellowCircleGray)

