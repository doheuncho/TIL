# https://leetcode.com/problems/kill-process/

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child_map = collections.defaultdict(list)
        queue = [kill]
        result = []
        
        for i in range(len(pid)):
            if ppid[i] != 0:
                child_map[ppid[i]].append(pid[i])
        
        while queue:
            cur_process = queue.pop()
            result.append(cur_process)
            if cur_process in child_map:
                while child_map[cur_process]:
                    queue.append(child_map[cur_process].pop())
        
        return result
                