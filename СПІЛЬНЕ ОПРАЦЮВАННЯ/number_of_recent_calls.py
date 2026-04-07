
from collections import deque
class RecentCounter:

    def __init__(self):
        self.__queue  = deque()


    def ping(self, t: int) -> int:
        self.__queue.append(t)

        while self.__queue[0] < t-3000:
            self.__queue.popleft()


        return len(self.__queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
