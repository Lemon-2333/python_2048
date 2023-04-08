import random

num = [
    [2, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
# num = [
#    [1, 2, 1, 2,1],
#    [2, 1, 2, 1,2],
#    [1, 2, 1, 2,1],
#    [2, 1, 2, 1,2],
#    [1, 2, 1, 2,1]
# ]

Y = len(num)
X = len(num[0])


def print_num():
    for y in range(len(num)):
        print(num[y])
    print("-"*X*3)


def add(Mode):  # 主要是相加动作
    if Mode == "up":
        add_up()
    elif Mode == "right":
        add_right()
    elif Mode == "down":
        add_down()
    elif Mode == "left":
        add_left()


def add_up():
    for y in range(Y):
        for x in range(X):
            if (y+1 != Y):
                if (num[y][x] == num[y+1][x]):
                    num[y][x] += num[y+1][x]
                    num[y+1][x] = 0


def add_right():
    for y in range(Y):
        for x in range(X)[::-1]:  # 取逆序x坐标
            if (x != 0):
                if (num[y][x] == num[y][x-1]):
                    num[y][x] += num[y][x-1]
                    num[y][x-1] = 0


def add_down():
    for y in range(Y)[::-1]:  # 取逆序
        for x in range(X):
            if (y != 0):
                if (num[y][x] == num[y-1][x]):
                    num[y][x] += num[y-1][x]
                    num[y-1][x] = 0


def add_left():
    for y in range(Y):
        for x in range(X):
            if (x+1 != X):
                if (num[y][x] == num[y][x+1]):
                    num[y][x] += num[y][x+1]
                    num[y][x+1] = 0


def move(Mode, log=1):  # 主要是位移动作
    if Mode == "up":
        move_up(log=log)
    elif Mode == "right":
        move_right(log=log)
    elif Mode == "down":
        move_down(log=log)
    elif Mode == "left":
        move_left(log=log)


def move_up(log=1):
    for t in range(Y):
        print_num() if log else 0
        for y in range(Y):
            for x in range(X):
                if (y+1 != Y):
                    if num[y][x] == 0:
                        num[y][x] = num[y+1][x]
                        num[y+1][x] = 0


def move_right(log=1):
    for t in range(X):
        print_num() if log else 0
        for y in range(Y):
            for x in range(X)[::-1]:  # 取逆序x坐标
                if (x != 0):
                    if num[y][x] == 0:
                        num[y][x] = num[y][x-1]
                        num[y][x-1] = 0


def move_down(log=1):
    for t in range(Y):
        print_num() if log else 0
        for y in range(Y)[::-1]:  # 取Y轴逆序坐标
            for x in range(X):
                if (y != 0):
                    if num[y][x] == 0:
                        num[y][x] = num[y-1][x]
                        num[y-1][x] = 0


def move_left(log=1):
    for t in range(X):
        print_num() if log else 0
        for y in range(Y):
            for x in range(X):
                if (x+1 != X):
                    if num[y][x] == 0:
                        num[y][x] = num[y][x+1]
                        num[y][x+1] = 0


def put_random_num():
    temp = 1
    times = 0
    while temp and times < 10:
        for y in range(Y):
            for x in range(X):
                if random.randint(0, 1):
                    if num[y][x] == 0:
                        num[y][x] = random.choice([2, 4])
                        temp = 0
                        break
            if not temp:
                break
        times += 1


def check(log=1):  # 检查是否游戏结束
    """检测思路：
    如：有
    a,b,b,b
    b,0,0,0
    b,0,0,0
    b,0,0,0
    那么就检测a周围的是否和a相等
    0,b,0,0
    b,a,b,b
    0,b,0,0
    0,b,0,0
    那么一次类推也是如此，已知道这种方案对于4x4(后发现再大的不够，会出错，所以直接2个for循环遍历每一个周围的4个格子)的格子来说是够用的，更多的未经过测试
    还可以利用短路，来减少判断次数，即只有a周围4个才能相加，所以其他地方的b可以省去
    0,b,0,0
    b,a,b,0
    0,b,0,0
    并且只要有一个为空-0，那么游戏就不会结束，所以只要检测到0后直接return 1
    """
    for i in num:
        if 0 in i:
            return 1
    for y in range(Y):
        for x in range(X):
            print(f"checking-{num[y][x]}-{y},{x}") if log else 0
            for xx in (range(x, X) if x else range(X)):
                print(f"now is:{num[y][xx]}-{y},{xx}") if log else 0
                if xx == x: # 跳过，防止自己与自己判断
                    print("skip") if log else 0
                    continue
                if num[y][xx] != num[y][x]: # 如果当前判断位置与原需要判断的位置的值不一样就说明无法进行相加。
                    if xx < x: # 防止当判断位置的左边不行时直接跳过右边判断
                        print("xx < x continue") if log else 0
                        continue
                    print("xx > x break") if log else 0
                    break
                elif num[y][xx] == num[y][x]: # 如果相等就直接返回，不进行继续判断
                    return 1
            for yy in (range(y, Y) if y else range(Y)):
                print(f"now is:{num[yy][x]}-{yy},{x}") if log else 0
                if yy == y:
                    print("skip") if log else 0
                    continue
                if num[yy][x] != num[y][x]:
                    if yy < y:
                        print("yy < y continue") if log else 0
                        continue
                    print("yy > y break") if log else 0
                    break
                elif num[yy][x] == num[y][x]:
                    return 1
    return 0


def main():
    while check(0):
        put_random_num()
        print_num()
        common = input("please input up/right/left/down:\n")
        move(common, 0)
        add(common)
        move(common, 0)


main()