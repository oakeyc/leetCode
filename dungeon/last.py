class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        find the least negative path from top left (0,0) to bottom right (m,n)
        find the path that has at one point the least amount of accumulated cost
        knight can only move +1 row or +1 col each move
        """
        memioz = []
        for row in dungeon:
            row_list = []
            for col in row:
                row_list.append(None)
            memioz.append(row_list)
        
        self.mem = memioz
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
            if get(self.mem, right_pos) is None:
                move_right = self.helper_min(d, right_pos, health + curr_val, min(health + curr_val, acc_min))
            else:
        
        if len(d) > down_pos[0]:
            curr_val = d[down_pos[0]][down_pos[1]]
            if get(self.mem, down_pos) is None:
                move_down = self.helper_min(d, down_pos, health + curr_val, min(health + curr_val, acc_min))
            else:
                move_down = get(self.mem, down_pos)

        if move_right is None:
            setmat(self.mem, position, move_down)
            return move_down
        if move_down is None:
            setmat(self.mem, position, move_right)
            return move_right
        elif move_right < move_down: # bc things are negative
            setmat(self.mem, position, move_down)
            return move_down
        else:
            setmat(self.mem, position, move_right)
            return move_right


def evalResult(minimum, health):
    if minimum < health:
        return minimum
    elif health < 0:
        return health
    else:
        return 1

def get(matrix, pos):
    return matrix[pos[0]][pos[1]]

def setmat(matrix, pos, val):
    matrix[pos[0]][pos[1]] = val


def printmat(mat):
    for row in mat:
        print(row)

sol = Solution()
print("answer: ", sol.calculateMinimumHP([[1,-4,5,-99],[2,-2,-2,-1]]))

printmat(sol.mem)