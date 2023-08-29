from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
        output = []
        visited = set()
        def dfs(current, cur):
            if len(cur) == current:
                output.append(cur.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    cur.append(nums[i])
                    dfs(current + 1, cur)
                    visited.remove(nums[i])
                    cur.pop()
        for i in range(len(nums)):
            dfs(i, [])
        return output

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets(nums))