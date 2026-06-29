class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            valid_num = set("123456789")
            for element in row:
                if element != ".":
                    try:
                        valid_num.remove(element)
                    except KeyError:
                        print("row", element, row)
                        return False

        for i in range(9):
            valid_num = set("123456789")
            for j in range(9):
                element = board[j][i]
                if element != ".":
                    try:
                        valid_num.remove(element)
                    except KeyError:
                        print("Col", element,j,i)
                        return False

        for box_i in range (3):
            for box_j in range (3):
                valid_num = set("123456789")
                for j in range(3):
                    for k in range(3):
                        element = board[box_i*3+j][box_j*3+k]
                        if element != ".":
                            try:
                                valid_num.remove(element)
                            except KeyError:
                                print("box", element, box_i,box_j)
                                return False
        return True
                    


        