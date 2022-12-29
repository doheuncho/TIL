# https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_queue = []
        result = []
        
        sort_by_euqueue = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        sort_by_euqueue.sort()
        
        n = len(tasks)
        cur_time = task_index = 0
        
        while task_index < n or task_queue:
            if not task_queue and cur_time < sort_by_euqueue[task_index][0]:
                cur_time = sort_by_euqueue[task_index][0]
            
            while task_index < n and cur_time >= sort_by_euqueue[task_index][0]:
                _, process_time, original_index = sort_by_euqueue[task_index]
                heapq.heappush(task_queue, (process_time, original_index))
                task_index += 1
            
            process_time, cur_index = heapq.heappop(task_queue)
            
            cur_time += process_time
            result.append(cur_index)
        
        return result
