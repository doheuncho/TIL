# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def dfs(invalid: str, idx: int, valid: str) -> None:
            if idx > 4:
                return
            if idx == 4 and not invalid:
                result.append(valid[:-1])
                return
                
            for i in range(1, len(invalid)+1):
                if invalid[:i] == '0' or (0 < int(invalid[:i]) < 256 and invalid[0] != '0'):
                    dfs(invalid[i:], idx + 1, valid + invalid[:i] + ".")

        dfs(s, 0, "")
        return result
    