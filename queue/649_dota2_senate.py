from collections import deque

# This is my attempt at the solution it is essentially a simulation of what would happen. Senators will always ban anothers right so long as there is a opposing party.
# The front of the queue is the person's turn. Each turn check if there is an opposing party member and remove. Then add that person to the end of the queue and repeat.
# O(n^2) as we need to go through and check if there is a opposing member every single time.


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = deque()
        for s in senate:
            senators.append(s)
        while len(senators) > 1:
            curr = senators.popleft()
            if curr == 'R':
                for i in range(len(senators)):
                    if senators[i] == 'D':
                        senators.remove('D')
                        senators.append(curr)
                        break
            if curr == 'D':
                for i in range(len(senators)):
                    if senators[i] == 'R':
                        senators.remove('R')
                        senators.append(curr)
                        break
        return "Radiant" if senators.pop() == 'R' else "Dire"

    # This is the optimized solution. It is O(n). The idea is to maintain 2 queues, one storing the indices of R and the other of D. For each iteration we get the first element of each queue by poping
    # then we check which one came first. Who ever came first gets put to the end of the queue, adding len(senate) to its value to allow for cyclic comparisions. We do this until one queue is empty and return accordingly.
    def predictPartyVictoryOptimized(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)
        while (len(r) and len(d)):
            rad = r.popleft()
            dire = d.popleft()
            if rad > dire:
                d.append(dire + len(senate))
            else:
                r.append(rad + len(senate))
        return "Radiant" if len(r) else "Dire"
