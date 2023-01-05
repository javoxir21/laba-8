#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = [int(i) for i in input().split()]
res = []
for i in range(len(a) - 1):
    if (a[i] > 0 and a[i + 1] > 0) or (a[i] < 0 and a[i + 1] < 0):
        res.append(a[i + 1])
        res.append(a[i + 1])
print(res[0], res[1])
