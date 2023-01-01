# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        
        for path in paths:
            directories = path.split()
            root = directories[0]
            
            for direct in directories[1:]:
                file_name, content = direct.split('(')
                dic[content].append(root + '/' + file_name)
                
        return [x for x in dic.values() if len(x) > 1]
