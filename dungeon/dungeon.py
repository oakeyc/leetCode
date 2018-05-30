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
            
        acc, health = self.helper_min(dungeon, (0, 0), dungeon[0][0], dungeon[0][0], memioz)
        result = min(acc, health) 
        # printmat(memioz)
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
        
        
    def helper_min(self, d, position, health, acc_min, mem):
        if (position == (len(d) - 1, len(d[0]) - 1)):
            # print("Acc: " + str(acc_min) + " and Health: " + str(health))
            ret_health = health + get(d, position)
            ret_acc_min = min(ret_health, acc_min)
            return ret_health, ret_acc_min
    
        move_right = None
        move_down = None

        right_pos = (position[0], position[1] + 1)
        down_pos = (position[0] + 1, position[1])
        pos_val = get(d, position)

        if len(d[right_pos[0]]) > right_pos[1]:  # if in bounds

            if get(mem, right_pos) is None:  # if not called, call it
                right_acc, right_health = self.helper_min(d, right_pos, health, acc_min, mem)
                move_right = min(right_acc, right_health)
            else:
                right_acc = get(mem, right_pos)[0] + acc_min
                right_health = get(mem, right_pos)[1] + health
                move_right = min(right_health, min(right_acc, acc_min))
        
        if len(d) > down_pos[0]:

            if get(mem, down_pos) is None:
                down_acc, down_health = self.helper_min(d, down_pos, health, acc_min, mem)
                move_down = min(down_acc, down_health)
            else:
                down_acc = get(mem, down_pos)[0] + acc_min
                down_health = get(mem, down_pos)[1] + health
                move_down = min(down_health, min(down_acc, acc_min))
        
        if move_right is None:
            setmat(mem, position, (down_acc, down_health))
            # printmat(mem)
            return (down_acc, down_health)

        if move_down is None:
            setmat(mem, position, (right_acc, right_health))
            # printmat(mem)
            return (right_acc, right_health)

        elif move_right < move_down: # bc things are negative
            setmat(mem, position, (down_acc, down_health))
            # printmat(mem)
            return (down_acc, down_health)

        else:
            setmat(mem, position, (right_acc, right_health))
            # printmat(mem)
            return (right_acc, right_health)
        
def get(matrix, pos):
    return matrix[pos[0]][pos[1]]

def setmat(matrix, pos, val):
    matrix[pos[0]][pos[1]] = val

def printmat(mat):
    for row in mat:
        print(row)

sol = Solution()
print("answer: ", sol.calculateMinimumHP([[1,-4,5,-99],[2,-2,-2,-1]]), str(3))
assert(sol.calculateMinimumHP([[0,0]]) == 1)
assert(sol.calculateMinimumHP([[100]]) == 1)

