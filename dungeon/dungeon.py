class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        find the least negative path from top left (0,0) to bottom right (m,n)
        find the path that has at one point the least amount of accumulated cost
        knight can only move +1 row or +1 col each move
        """
        self.d = dungeon
 
        memioz = []
        for row in self.d:
            row_list = []
            for col in row:
                row_list.append(None)
            memioz.append(row_list)
               
        self.mem = memioz

        # start at the top right, and with 0 health, 0 min
        helper = self.helper_min((0, 0))
        
        result = min(helper)

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
        
    def try_direction(self, curr_health, position):

        if get(self.mem, position) is None:  # have we done this before
            return_tup = self.helper_min(position)
            setmat(self.mem, position, return_tup)

        else:
            return_tup = get(self.mem, position)

        pos_min, health = return_tup

        return_tup = (min(pos_min + curr_health, curr_health), health + curr_health)

        return min(return_tup), return_tup

    def helper_min(self, position):
        if (position == (len(self.d) - 1, len(self.d[0]) - 1)):  # base case
            return setmat(self.mem, position, (get(self.d, position), get(self.d, position)))
 
        move_right = None
        move_down = None

        right_pos = (position[0], position[1] + 1)
        down_pos = (position[0] + 1, position[1])
        curr_health = get(self.d, position)

        if len(self.d[right_pos[0]]) > right_pos[1]:
            move_right, right_tup = self.try_direction(curr_health, right_pos)
           
        if len(self.d) > down_pos[0]:
            move_down, down_tup = self.try_direction(curr_health, down_pos)

        if move_right is None:
            return down_tup
        if move_down is None:
            return right_tup
        elif move_right < move_down:
            return down_tup
        else:
            return right_tup

def get(matrix, pos):
    return matrix[pos[0]][pos[1]]

def setmat(matrix, pos, val):
    matrix[pos[0]][pos[1]] = val
    return val