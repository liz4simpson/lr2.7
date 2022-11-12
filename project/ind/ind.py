#usr/bin/env python3
# -*- coding: utf-8 -*-
#Определить результат выполнения операций над множествами:

if __name__ == "__main__":

    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"c", "d", "k", "l", "m", "z"}
    b = {"b", "c", "d", "n","w"}
    c = {"m", "n", "y"}
    d = {"b", "j", "l", "r", "s", "w","x"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    cn = u.difference(c)
    bn = u.difference(b)

    y = (a.difference(d)).union(cn.difference(bn))
    print(f"y = {y}")