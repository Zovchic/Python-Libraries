import os
import time



class FieldException(Exception):
    pass


class ObjectException(Exception):
    pass


global A
global width
global height
global objs
objs = []
global border


def clc():
    os.system("clear")


def clcw():
    os.system("cls")


def canvas(width, height, border=True):
    A = ["."] * width
    for i in range(width):
        A[i] = ["."] * height
    return A, width, height


def create(lst, sym, lx, ly, objName, layer=1):
    idx = -1
    try:
        idx = objs.index(objName)
    except:
        pass
    if idx == -1:
        if sym != ".":
            lst[ly][lx] = sym
            objs.append(objName)
            objs.append(lx)
            objs.append(ly)
            objs.append(sym)
            objs.append(layer)
        else:
            raise FieldException("You cannot create an empty space. Note: '.' means empty space")
    else:
        raise ObjectException(f"Name '{objName}' is already taken")


def ers(lst, objName):
    idx = -1
    try:
        idx = objs.index(objName)
    except:
        pass
    if idx != -1:
        lst[objs[idx + 2]][objs[idx + 1]] = "."
        del(objs[idx], objs[idx + 1])
        del(objs[idx])
        del(objs[idx])
        del(objs[idx])
    else:
        raise ObjectException(f"Object '{objName}' not found")


def move(lst, objName, movex, movey):
    idx = -1
    try:
        idx = objs.index(objName)
    except:
        pass
    if idx != -1:
        if movex != 0 or movey != 0:
            sym = lst[objs[idx + 2]][objs[idx + 1]]
            lst[objs[idx + 2] + movey][objs[idx + 1] + movex] = sym
            lst[objs[idx + 2]][objs[idx + 1]] = "."
            objs[idx + 1] += movex
            objs[idx + 2] += movey
    else:
        raise ObjectException(f"Object '{objName}' not found")


def prfld(lst):
    for i in range(len(lst)):
        print(*lst[i])


def frame(lst, delay=1.0, system="w"):
    if system == "w":
        clcw()
        prfld(lst)
    elif system == "l":
        clc()
        prfld(lst)
    time.sleep(delay)


def coords(objName):
    idx = -1
    try:
        idx = objs.index(objName)
    except:
        pass
    if idx != -1:
        return [objs[idx + 1], objs[idx + 2]]


def fobj(objName):
    idx = -1
    try:
        idx = objs.index(objName)
    except:
        pass
    if idx == -1:
        idx = 0
    else:
        idx = 1
