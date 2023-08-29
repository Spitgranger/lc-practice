from typing import List
# This is similar to combination sum 1 except we use a while loop to eliminate duplicates and only use the elements once

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    array = sorted(candidates)
    output = []
    cur = []
    visited = set()
    def dfs(current, currentSum):
        if currentSum == target:
            output.append(cur.copy())
            return
        if current >= len(candidates) or currentSum > target:
            return
        cur.append(array[current])
        dfs(current + 1, currentSum + array[current])
        cur.pop()
        while current + 1 < len(array) and array[current] == array[current + 1]:
            current += 1
        dfs(current + 1, currentSum)
    dfs(0, 0)
    return output

if __name__ == "__main__":
    print(combinationSum2([10,1,2,7,6,1,5], 8))