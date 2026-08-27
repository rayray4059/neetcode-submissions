class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = {}
        cube_set = {}

        for row_num, row in enumerate(board):
            row_set = set()
            for i in range(len(row)):
                if row[i] == ".": continue
                if row[i] in row_set: return False
                else: row_set.add(row[i])

                if i in col_set:
                    if row[i] in col_set[i]: return False
                    else: col_set[i].append(row[i])
                else:
                    col_set[i] = [row[i]]

                box_num  = (row_num//3) * 3 + (i // 3)
                if box_num in cube_set:
                    if row[i] in cube_set[box_num]: return False
                    else: cube_set[box_num].append(row[i])   
                else: 
                    cube_set[box_num] = [row[i]]
            
        return True
                
            
            



                 

