#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n, func="TD"):

    def fib_td(n):
        if n <= 1:
            f[n] = n
        else:
            f[n] = fib_td(n - 1)+fib_td(n - 2)
        return f[n]

    def fib_bu(n):
        f = [0]*(n+1)
        f[0], f[1] = 0, 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]

    def fib_bu_i(n):
        if n <= 1:
            return n
        prev, curr = 0, 1
        for i in range(n - 1):
            prev, curr = curr, prev + curr
        return curr

    match func:
        case "TD":
            f = [-1] * (n + 1)
            return fib_td(n)
        case "BU":
            return fib_bu(n)
        case "BU_I":
            return fib_bu_i(n)


if __name__ == "__main__":
    n = 13
    print("Динамическое программирование назад: ", fib(n, 'TD'))
    print("Динамическое программирование вперёд: ", fib(n, 'BU'))
    print("Уменьшение памяти: ", fib(n, "BU_I"))

