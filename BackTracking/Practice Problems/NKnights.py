class NKnights:
    def knight(self, board, row, col, knights):
        if knights == 0:
            self.display(board)

    def display(self, Board: List[List[bool]]):
        for row in Board:
            for element in row:
                if element:
                    print('Q', end='')
                else:
                    print('.', end='')

            print()
