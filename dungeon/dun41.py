class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        find the least negative path from top left (0,0) to bottom right (m,n)
        find the path that has at one point the least amount of accumulated cost
        knight can only move +1 row or +1 col each move
        """
        # for row in dungeon:
        #     print(row)
        result = self.helper_min(dungeon, (0, 0), dungeon[0][0], dungeon[0][0])
        # print(result)
        if result is not None:
            if result > 0:
                return 1
            else:
                return abs(result) + 1
        else:
            val = dungeon[0][0]
            if val > 0:
                return 1
            else:
                return abs(val) + 1
        
    def helper_min(self, d, position, health, acc_min):
        if (position == (len(d) - 1, len(d[0]) - 1)):
            # print("Acc: " + str(acc_min) + " and Health: " + str(health))
            return acc_min if health >= 0 or health > acc_min else health
    
        move_right = None
        move_down = None

        right_pos = (position[0], position[1] + 1)
        down_pos = (position[0] + 1, position[1])
        
        if len(d[right_pos[0]]) > right_pos[1]:
            curr_val = d[right_pos[0]][right_pos[1]]
            move_right = self.helper_min(d, right_pos, health + curr_val, min(health + curr_val, acc_min))
        
        if len(d) > down_pos[0]:
            curr_val = d[down_pos[0]][down_pos[1]]
            move_down = self.helper_min(d, down_pos, health + curr_val, min(health + curr_val, acc_min))
        
        if move_right is None:
            return move_down
        if move_down is None:
            return move_right
        elif move_right < move_down: # bc things are negative
            return move_down
        else:
            return move_right