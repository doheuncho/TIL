# https://leetcode.com/problems/robot-room-cleaner/

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, (0, 0), (0, 1), set())
    
    def dfs(self, robot, position, derection, visited):
        robot.clean()
        visited.add(position)
            
        for _ in range(4):
            next_position = (position[0] + derection[0], position[1] + derection[1])
            if next_position not in visited and robot.move():
                self.dfs(robot, next_position, derection, visited)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            robot.turnRight()
            derection = (-derection[1], derection[0])
        