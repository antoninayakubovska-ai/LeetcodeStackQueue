from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        time = 0

        while queue:
            person_idx = queue.popleft()

            tickets[person_idx] -= 1
            time += 1

            if person_idx == k and tickets[person_idx] == 0:
                return time

            if tickets[person_idx] > 0:
                queue.append(person_idx)
        