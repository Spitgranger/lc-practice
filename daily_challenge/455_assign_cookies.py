from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    # Sort both greed and cookie lists, start to see if each cookie will satisfied the kid.
    # If not, move to the next greater cookie, if yes, add to sastified and advance the pointer to kids and cookie
    satisfied = 0
    kids = sorted(g)
    cookies = sorted(s)
    i = 0
    j = 0
    while i < len(kids) and j < len(cookies):
        if kids[i] <= cookies[j]:
            satisfied += 1
        else:
            j += 1
            continue
        i += 1
        j += 1
    return satisfied
