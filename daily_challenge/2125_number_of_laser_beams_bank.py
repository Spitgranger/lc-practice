from typing import List


def numberOfBeams(self, bank: List[str]) -> int:
    count = 0
    ret = 0
    for row in bank:
        current = 0
        for cell in row:
            if cell == '1':
                current += 1
        if current == 0:
            continue
        ret += (count * current)
        count = current
    return ret
