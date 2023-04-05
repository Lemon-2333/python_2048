num = [
    [2, 0, 0, 0],
    [2, 2, 0, 0],
    [0, 2, 2, 0],
    [0, 0, 2, 2]
]

Y = len(num)
X = len(num[0])


def print_num():
    for y in range(len(num)):
        print(num[y])
    print("-"*X*3)


def pull(Mode):  # 主要是相加动作
    if Mode == "up":
        pull_up()
    elif Mode == "right":
        pull_right()
    elif Mode == "down":
        pull_down()
    elif Mode == "left":
        pull_left()


def pull_up():
    for y in range(Y):
        for x in range(X):
            if (y+1 != Y):
                if (num[y][x] == num[y+1][x]):
                    num[y][x] += num[y+1][x]
                    num[y+1][x] = 0

def pull_right():
    for y in range(Y):
        for x in range(X)[::-1]: #取逆序x坐标
            if (x != 0):
                if (num[y][x] == num[y][x-1]):
                    num[y][x] += num[y][x-1]
                    num[y][x-1] = 0

def pull_down():
    for y in range(Y)[::-1]: # 取逆序
        for x in range(X):
            if (y != 0):
                if (num[y][x] == num[y-1][x]):
                    num[y][x] += num[y-1][x]
                    num[y-1][x] = 0

def pull_left():
    for y in range(Y):
        for x in range(X):
            if (x+1 != X):
                if (num[y][x] == num[y][x+1]):
                    num[y][x] += num[y][x+1]
                    num[y][x+1] = 0

def check(Mode,log=1):  #主要是位移动作
    if Mode == "up" :
        check_up(log=log)
    elif Mode == "right" :
        check_right(log=log)
    elif Mode == "down":
        check_down(log=log)
    elif Mode == "left":
        check_left(log=log)

def check_up(log):
    for t in  range(Y):
        if log:
            print_num()
        for y in range(Y):
            for x in range(X):
                if (y+1 != Y):
                    if num[y][x] == 0:
                        num[y][x] = num[y+1][x]
                        num[y+1][x]=0

def check_right(log):
    for t in  range(X):
        if log:
            print_num()
        for y in range(Y):
            for x in range(X)[::-1]:  #取逆序x坐标
                if (x != 0):
                    if num[y][x] == 0:
                        num[y][x] = num[y][x-1]
                        num[y][x-1]=0

def check_down(log):
    for t in  range(Y): 
        if log:
            print_num()
        for y in range(Y)[::-1]: #    取Y轴逆序坐标
            for x in range(X):
                if (y != 0):
                    if num[y][x] == 0:
                        num[y][x] = num[y-1][x]
                        num[y-1][x]=0

def check_left(log):
    for t in  range(X):
        if log:
            print_num()
        for y in range(Y):
            for x in range(X):  
                if (x+1 != X):
                    if num[y][x] == 0:
                        num[y][x] = num[y][x+1]
                        num[y][x+1]=0

print_num()
check("down")
pull("down")
print_num()
