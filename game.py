class GameBoard:
    def __init__(self):
        self.game_map = [[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0]]

    def drop_piece(self, player_num, col):
        if col > len(self.game_map) or col < 0:
            raise Exception("input column out of range (0-6)")

        if self.game_map[0][col] != 0:
            raise Exception("selected column({}) is full".format(col))

        for i in range(len(self.game_map)):
            if self.game_map[i][col] == 0:
                continue
            else:
                self.game_map[i-1][col] = player_num
                return

        self.game_map[len(self.game_map) - 1][col] = player_num

    def check_win(self, player_num):
        if type(player_num) != int:
            raise Exception("input type is not int in check_win()")

        gm = self.game_map

        # check horizontal
        for row in gm:
            for i in range(len(row) - 3):
                if row[i] != player_num:
                    continue
                elif row[i+1] == player_num and row[i+2] == player_num and row[i+3] == player_num:
                    return True

        # check vertical
        for x in range(len(gm[0])):
            for y in range(len(gm) - 3):
                if gm[y][x] != player_num:
                    continue
                elif gm[y+1][x] == player_num and gm[y+2][x] == player_num and gm[y+3][x] == player_num:
                    return True

        # check Diagonal
        for x in range(len(gm[0]) - 3):
            for y in range(len(gm) - 3):
                if gm[y][x] != player_num:
                    continue
                elif gm[y+1][x+1] == player_num and gm[y+2][x+2] == player_num and gm[y+3][x+3] == player_num:
                    return True

        for x in range(3, len(gm[0])):
            for y in range(len(gm) - 3):
                if gm[y][x] != player_num:
                    continue
                elif gm[y+1][x-1] == player_num and gm[y+2][x-2] == player_num and gm[y+3][x-3] == player_num:
                    return True

        return False

    def print_map(self):
        for row in self.game_map:
            print(row)
