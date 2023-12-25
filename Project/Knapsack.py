#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def knapsack_bu(W, weight, cell):
    def knapsack_with_reps(W, weight, cell):
        d = [0]*(W+1)
        for w in range(1, W+1):
            for weight_i, cell_i in zip(weight, cell):
                if weight_i <= w:
                    d[w] = max(d[w], d[w - weight_i] + cell_i)
        return d[W]

    def knapsack_without_reps(W, weight, cell):
        def restore(d, weight_rev, cell_rev):
            sol = []
            w = W
            el = len(weight_rev)
            for weight_i, cell_i in zip(weight_rev, cell_rev):
                if d[w][el] == d[w - weight_i][el - 1] + cell_i:
                    sol.append(1)
                    w -= weight_i
                else:
                    sol.append(0)
                el -= 1
            sol.reverse()
            return sol

        d = [[0] for e in range(W+1)]
        d[0] = [0] * (len(weight) + 1)
        for weight_i, cell_i in zip(weight, cell):
            for w in range(1, W+1):
                d[w].append(d[w][-1])
                if weight_i <= w:
                    d[w][-1] = max(d[w][-1], d[w - weight_i][-2] + cell_i)

        sol = restore(d, weight[::-1], cell[::-1])

        return d[W][-1], sol

    return knapsack_with_reps(W, weight, cell), knapsack_without_reps(W, weight, cell)


if __name__ == "__main__":
    W = 10
    weight = [6, 3, 4, 2]
    cell = [30, 14, 16, 9]
    with_rep_bu, without_rep_bu = knapsack_bu(W, weight, cell)
    print(with_rep_bu)
    print(without_rep_bu)