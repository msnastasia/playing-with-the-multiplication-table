import random


def math():
    x = random.randint(2, 12)
    y = random.randint(2, 12)
    return [x, y, x * y]


def multiplication():
    finish = []
    for i in range(5):
        z = math()
        while 1:
            if z[2] not in finish:
                print('%s * %s = __' % (z[0], z[1]))
                break
            else:
                z = math()

        finish.append(z[2])



def division():
    finish1 = []
    for i in range(5):
        z = math()
        while 1:
            if z[2] not in finish1:
                print('%s : %s = __' % (z[2], z[1]))
                break
            else:
                z = math()
        finish1.append(z[2])


multiplication()
division()