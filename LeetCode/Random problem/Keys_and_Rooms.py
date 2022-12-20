# https://leetcode.com/problems/keys-and-rooms/

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]

        while stack:
            node = stack.pop()
            for key in rooms[node]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        return False not in (visited)
