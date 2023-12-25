#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lis_bottom_up(a):
    n = len(a)
    d = [0]*n
    for i in range(1, n):
        d[i] = 1
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    ans = max(d)
    return ans


def lis_bottom_up2(a):
    def restore_with_prev(m_index):
        l = []
        while True:
            l.append(m_index)
            if prev[m_index] == -1:
                break
            m_index = prev[m_index]

        l.reverse()
        return l

    def restore_without_prev(ans, m_index):
        l = []
        while True:
            l.append(m_index)
            if ans == 1:
                break
            ans -= 1
            while True:
                m_index -= 1
                if d[m_index] == ans and a[m_index] < a[l[-1]]:
                    break
        l.reverse()
        return l

    n = len(a)
    d, prev = [0]*n, [0]*n

    for i in range(1, n):
        d[i] = 1
        prev[i] = -1
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j

    ans, max_index = 0, 0
    for i, item in enumerate(d):
        if ans < item:
            ans, max_index = item, i

    return ans, restore_with_prev(max_index), restore_without_prev(ans, max_index)


if __name__ == "__main__":
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    print(lis_bottom_up(a))
    print(lis_bottom_up2(a))
