import random


def bubble_sorting(a):
    for j in range(0, len(a) - 1):
        for k in range(0, len(a) - 1):
            if a[k] > a[k+1]:
                a[k] = a[k+1]
                z = a[k+1]
                a[k+1] = z
    return a


def sorting_choice(b):
    for i in range(0, len(b) - 1):
        min_element = b[i]
        k = i
        for j in range(i+1, len(b)):
            if b[j] < min_element:
                k = j
                min_element = b[j]
        b[k] = b[i]
        b[i] = min_element
    return b


def quick_sorting(c):
    if len(c) <= 1:
        return c
    else:
        element = random.choice(c)
        c_1 = []
        c_2 = []
        c_3 = []
        for i in c:
            if i < element:
                c_1.append(i)
            elif i > element:
                c_2.append(i)
            else:
                c_3.append(i)
        return quick_sorting(c_1) + c_3 + quick_sorting(c_2)


def check(d):
    for i in range(1, len(d)):
        if d[i - 1] > d[i]:
            return False
    return True
