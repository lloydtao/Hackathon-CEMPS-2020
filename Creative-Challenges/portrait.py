from turtle import Turtle
t = Turtle()
t.speed(0)
# David's face is stored as 7 SVG paths
path_count = 7
paths = []

for i in range(7):
    with open("path{}.txt".format(str(i+1))) as file:
        path = file.read()
        path = path.replace("\n", " ")
        paths.append(path)


def chr_is_letter(character):
    if len(character) == 0:
        return False
    o = ord(character)
    if o >= ord("a") and o <= ord("z"):
        return True
    if o >= ord("A") and o <= ord("Z"):
        return True
    return False


def find_instruction(string):
    if len(string) == 0:
        return False
    if len(string) == 1:
        return string
    i = 1
    char = string[i]
    while not chr_is_letter(char) and i < (len(string) - 1):
        i += 1
        char = string[i]
    if chr_is_letter(char):  # we've hit the next instruction
        return string[0:(i-1)]
    else:  # we've hit the end of the path
        return string


def parse_path(path):
    instruction_list = []
    while len(path) > 0:
        instruction = find_instruction(path)
        if not instruction:
            break
        instruction_list.append(instruction)
        path = path[len(instruction) + 1:]
    return instruction_list


def lerp(a, b, t):
    # Linear interpolation function. returns a when t==0, returns b when t==1
    # and linearly interpolates for values inbetween
    return (a * (1 - t)) + (b * t)


def lerp2(a, b, t):
    # 2-d linear interpolation function
    return lerp(a[0], b[0], t), lerp(a[1], b[1], t)


def bezier(p0, p1, p2, p3, t):
    # calculate coordinates for point t on the bezier defined by p1-p4
    c1 = lerp2(p1, p2, t)
    c2 = lerp2(p0, c1, t)
    c3 = lerp2(c1, p3, t)
    c4 = lerp2(c2, c3, t)

    return c4


def stepturtle(turtle, x, y):
    # step turtle so it ends at x/y

    while turtle.distance(x, y)>0.5:
        rotdif = turtle.towards(x, y)  # see how much we need to turn
        turn = rotdif - turtle.heading()
        if turn > 180:
            turtle.left(turn-360)
        elif turn < -180:
            turtle.left(turn+360)
        else:
            turtle.left(turn)  # turn

        distance = turtle.distance(x, y)  # see how far we need to go
        turtle.forward(distance)  # go


def turtle_bezier(turtle, p0, p1, p2, p3):
    # walk the turtle along a bezier
    t = 0
    while t < 1:
        t += 0.001
        x, y = bezier(p0, p1, p2, p3, t)  # calculate position for that point on the bezier

        # only step if the distance is bigger than one pixel.
        if turtle.distance(x, y) >= 1:
            stepturtle(turtle, x, y)  # move turtle to position
            
#turtle_bezier(t, (0,25), (25, 50), (0, 75))


def parse_instruction(inst):
    code = inst[0]
    inst = inst[1:]
    points = inst.split()
    coords = []
    if not len(points) % 2 == 0:
        print("Odd number of points given to instruction :////")
        return
    while not len(points) == 0:
        coords.append([int(points.pop()), int(points.pop())])
    return code, coords


cached_x, cached_y = 0, 0
def complete_instruction(inst):
    code, points = parse_instruction(inst)
    if code == "M":
        x, y = points[0][0], points[0][1]
        cached_x, cached_y = x, y
        t.penup()
        t.goto(x, y)
        t.pendown()
    elif code == "m":
        x, y = points[0][0], points[0][1]
        t.penup()
        t.goto( t.pos() + (x ,y) )
        t.pendown()
    elif code == "L":
        x, y = points[0][0], points[0][1]
        t.goto(x, y)
    elif code == "l":
        x, y = points[0][0], points[0][1]
        t.goto( t.pos() + (x ,y) )
    elif code == "c":
        p0x, p0y = int(t.xcor()), int(t.ycor())
        p1x, p1y = p0x + points[0][0], p0y + points[0][1]
        p2x, p2y = p0x + points[1][0], p0y + points[1][1]
        p3x, p3y = p0x + points[2][0], p0y + points[2][1]
        turtle_bezier(t, (p0x, p0y), (p1x, p1y), (p2x, p2y), (p3x, p3y))
    elif code.lower == "z":
        t.penup()
        t.goto(cached_x, cached_y)
        t.pendown()

##if __name__ == "__main__":
##    for path in paths:
##        instructions = parse_path(path)
##        for inst in instructions:
##            print(inst)
##            complete_instruction(inst)


# In case the SVG parsing isn't done in time. I am heartbroken
t.penup()
t.left(90)
t.back(300)
t.right(90)
t.pendown()
t.circle(300)
t.penup()
t.left(90)
t.forward(450)
t.left(90)
t.forward(80)
t.pendown()
t.circle(80)
t.penup()
t.right(180)
t.forward(160)
t.pendown()
t.circle(80)
t.penup()
t.right(90)
t.forward(200)
t.left(90)
t.pendown()
t.forward(50)
t.left(45)
t.forward(200)
t.left(45)
t.forward(50)
