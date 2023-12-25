#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def edit_dist_td(a, b, i, j, d):
    if d[i][j] == -1:
        if i == 0:
            d[i][j] = j
        elif j == 0:
            d[i][j] = i
        elif a[i - 1] == b[j - 1]:
            d[i][j] = edit_dist_td(a, b, i - 1, j - 1, d)
        else:
            insert_cost = 1 + edit_dist_td(a, b, i, j - 1, d)
            delete_cost = 1 + edit_dist_td(a, b, i - 1, j, d)
            replace_cost = 1 + edit_dist_td(a, b, i - 1, j - 1, d)
            d[i][j] = min(insert_cost, delete_cost, replace_cost)
    return d[i][j]


def initialize_matrix(n, m):
    return [[-1 for _ in range(m)] for _ in range(n)]


def edit_dist_bu(a, b):
    n = len(a)
    m = len(b)
    d = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1):
        d[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i - 1] == b[j - 1]:
                d[i][j] = d[i-1][j-1]
            else:
                insert_cost = 1 + d[i][j-1]
                delete_cost = 1 + d[i-1][j]
                replace_cost = 1 + d[i-1][j-1]
                d[i][j] = min(insert_cost, delete_cost, replace_cost)

    return d[n][m]


if __name__ == "__main__":
    a = "kitten"
    b = "sitting"
    n = len(a)
    m = len(b)
    d = initialize_matrix(n + 1, m + 1)
    print("Динамическое программирование сверху вниз:", edit_dist_td(a, b, n, m, d))
    print("Динамическое программирование снизу вверх:", edit_dist_bu(a, b))
