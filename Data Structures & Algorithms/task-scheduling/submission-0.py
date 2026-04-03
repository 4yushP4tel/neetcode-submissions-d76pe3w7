from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        We want to note that we should always be doing the most frequent task first, since
        doing one with less time makes no sense, and would not allow to minimize
        time.
        """
        min_num_cycles = 0
        counts = Counter(tasks)

        max_heap = [-v for v in counts.values()]
        heapq.heapify(max_heap)

        clk = 0
        queue = deque()
        while queue or max_heap:
            clk += 1
            if max_heap:
                processed_task = heapq.heappop(max_heap)
                processed_task += 1
                if processed_task:
                    queue.append((clk+n, processed_task))
            
            if queue and queue[0][0] == clk:
                time, remaining_task = queue.popleft()
                heapq.heappush(max_heap, remaining_task)

        return clk




    




        