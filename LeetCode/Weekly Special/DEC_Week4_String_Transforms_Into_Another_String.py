# https://leetcode.com/problems/string-transforms-into-another-string/submissions/

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        # 만약 str1과 str2이 다르고, str2가 a ~ z의 모든 알파벳으로 구성되어 있다면 conversion mapping이 불가능하다.(loop가 생김)
        elif len(set(str2)) == 26:
            return False
        
        str_map = {}
        
        # str1의 character와 str2의 character를 mapping하면서 conversion이 가능한지 확인
        for i in range(len(str1)):
            if str1[i] not in str_map:
                str_map[str1[i]] = str2[i]
            elif str_map[str1[i]] != str2[i]:
                return False
        
        return True
