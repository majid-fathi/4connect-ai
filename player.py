class Player:
    def __init__(self, number):
        self.number = number

    def get_drop_input(self, game_map):
        pass


class Person(Player):
    def __init__(self, number):
        super().__init__(number)

    def get_drop_input(self, game_map):
        raise Exception("get_drop_input() called from Person class")


def check_opponent_win(game_map, player_num):
    # vertical
    for x in range(len(game_map[0])):
        for y in range(len(game_map) - 2):
            if game_map[y][x] != player_num:
                continue

            elif game_map[y + 1][x] == player_num and game_map[y + 2][x] == player_num:
                if y - 1 > -1:
                    if game_map[y - 1][x] == 0:
                        return x

    # horizontal
    for x in range(len(game_map)):
        for y in range(len(game_map[0]) - 3):
            if game_map[x][y] != player_num:
                continue

            elif game_map[x][y + 1] == player_num and game_map[x][y + 2] == player_num:
                if y - 1 > -1:
                    if x == 5 and game_map[x][y - 1] == 0:
                        return y - 1

                    elif x < 5 and game_map[x + 1][y - 1] != 0 and game_map[x][y - 1] == 0:
                        return y - 1

                if y + 3 < 7:
                    if x == 5 and game_map[x][y + 3] == 0:
                        return y + 3

                    elif x < 5 and game_map[x + 1][y + 3] != 0 and game_map[x][y + 3] == 0:
                        return y + 3

            elif game_map[x][y + 1] == 0 and game_map[x][y + 2] == player_num and game_map[x][y + 3]:
                if x == 5:
                    return y + 1

                else:
                    if game_map[x + 1][y + 1] != 0:
                        return y + 1

            elif game_map[x][y + 1] == player_num and game_map[x][y + 2] == 0 and game_map[x][y + 3]:
                if x == 5:
                    return y + 2

                elif game_map[x + 1][y + 2] != 0:
                    return y + 2

    # check Diagonal
    for x in range(len(game_map[0]) - 3):
        for y in range(len(game_map) - 2):
            if game_map[y][x] != player_num:
                continue

            elif game_map[y + 1][x + 1] == player_num and game_map[y + 2][x + 2] == player_num:
                if y + 3 < 5 and x + 3 < 7:
                    if game_map[y + 4][x + 3] != 0 and game_map[y + 3][x + 3] == 0:
                        return x + 3

                if y + 3 == 5 and x + 3 < 7:
                    if game_map[y + 3][x + 3] == 0:
                        return x + 3

                if y - 1 >= 0 and x - 1 >= 0:
                    if game_map[y][x - 1] != 0 and game_map[y - 1][x - 1] == 0:
                        return x - 1

    for x in range(3, len(game_map[0])):
        for y in range(len(game_map) - 2):
            if game_map[y][x] != player_num:
                continue

            elif game_map[y + 1][x - 1] == player_num and game_map[y + 2][x - 2] == player_num:
                if y + 3 < 5 and x - 3 >= 0:
                    if game_map[y + 4][x - 3] != 0 and game_map[y + 3][x - 3] == 0:
                        return x - 3

                elif y + 3 == 5 and x - 3 >= 0:
                    if game_map[y + 3][x - 3] == 0:
                        return x - 3

                if y - 1 >= 0 and x + 1 <= 6:
                    if game_map[y][x + 1] != 0 and game_map[y - 1][x + 1] == 0:
                        return x + 1

    return -1


def win_check_ai(temp_map, player_num, game_map1, column_num):
    flag = 0

    if game_map1[0][column_num] == 0:
        for c in range(5, 0, -1):
            if game_map1[c - 1][column_num] == 0 and game_map1[c][column_num] == 0:
                flag = 1
                break
    else:
        return 1

    if flag == 0:
        return 0

    temp_map[c - 1][column_num] = player_num

    gm = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]
    for x in range(len(temp_map)):
        for y in range(len(temp_map[0])):
            gm[x][y] = temp_map[x][y]

    # check horizontal
    for row in gm:
        for i in range(len(row) - 3):
            if row[i] != player_num:
                continue
            elif row[i + 1] == player_num and row[i + 2] == player_num and row[i + 3] == player_num:

                return 1

    # check vertical
    for x in range(len(gm[0])):
        for y in range(len(gm) - 3):
            if gm[y][x] != player_num:
                continue
            elif gm[y + 1][x] == player_num and gm[y + 2][x] == player_num and gm[y + 3][x] == player_num:
                return 1

    # check Diagonal
    for x in range(len(gm[0]) - 3):
        for y in range(len(gm) - 3):
            if gm[y][x] != player_num:
                continue
            elif gm[y + 1][x + 1] == player_num and gm[y + 2][x + 2] == player_num and gm[y + 3][x + 3] == player_num:
                return 1

    for x in range(3, len(gm[0])):
        for y in range(len(gm) - 3):
            if gm[y][x] != player_num:
                continue
            elif gm[y + 1][x - 1] == player_num and gm[y + 2][x - 2] == player_num and gm[y + 3][x - 3] == player_num:
                return 1

    return 0


class AIPlayer(Player):
    def __init__(self, number):
        super().__init__(number)

    def win_check_3(self, game_map, player_num, opponent):
        if player_num == opponent:
            opp = self.number
        else:
            opp = opponent

        map2 = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]

        for v in range(len(game_map)):
            for y in range(len(game_map[0])):
                map2[v][y] = game_map[v][y]

        # vertical
        for x in range(len(game_map[0])):
            for y in range(len(game_map) - 1):
                if game_map[y][x] != player_num:
                    continue
                elif game_map[y + 1][x] == player_num:
                    if y - 1 > 0:
                        if game_map[y - 1][x] == 0 and win_check_ai(map2, opponent, game_map, x) == 0 and \
                                win_check_ai(map2, self.number, game_map, x) == 0:
                            return x

        # horizontal
        for x in range(len(game_map)):
            for y in range(len(game_map[0]) - 2):
                if game_map[x][y] != player_num:
                    continue

                elif game_map[x][y + 1] == player_num:
                    if y - 1 > 0 and y + 2 < 7:
                        if x == 5 and game_map[x][y - 1] == 0 and (
                                game_map[x][y + 2] != opp or game_map[x][y - 2] != opp):
                            if win_check_ai(map2, opponent, game_map, y - 1) == 0 and \
                                    win_check_ai(map2, self.number, game_map, y - 1) == 0:
                                return y - 1

                        elif x < 5 and game_map[x + 1][y - 1] != 0 and game_map[x][y - 1] == 0 and (
                                game_map[x][y + 2] != opp or game_map[x][y - 2] != opp):
                            if win_check_ai(map2, opponent, game_map, y - 1) == 0 and \
                                    win_check_ai(map2, self.number, game_map, y - 1) == 0:
                                return y - 1

                    if y + 2 < 6 and y - 1 > -1:
                        if x == 5 and game_map[x][y + 2] == 0 and (
                                game_map[x][y + 3] != opp or game_map[x][y - 1] != opp):
                            if win_check_ai(map2, opponent, game_map, y + 2) == 0 and \
                                    win_check_ai(map2, self.number, game_map, y + 2) == 0:
                                return y + 2

                        elif x < 5 and game_map[x + 1][y + 2] != 0 and game_map[x][y + 2] == 0 and (
                                game_map[x][y - 1] != opp or game_map[x][y + 3] != opp):
                            if win_check_ai(map2, opponent, game_map, y + 1) == 0 and \
                                    win_check_ai(map2, self.number, game_map, y + 1) == 0:
                                return y + 2

        # check Diagonal
        for x in range(len(game_map[0]) - 3):
            for y in range(len(game_map) - 2):
                if game_map[y][x] != player_num:
                    continue
                elif game_map[y + 1][x + 1] == player_num:
                    if y + 2 < 5 and x + 2 < 7:
                        if game_map[y + 3][x + 2] != 0 and game_map[y + 2][x + 2] == 0:
                            if win_check_ai(map2, opponent, game_map, x + 2) == 0 and \
                                    win_check_ai(map2, self.number, game_map, x + 2) == 0:
                                return x + 2

                    if y + 2 == 5 and x + 2 < 7:
                        if game_map[y + 2][x + 2] == 0:
                            if win_check_ai(map2, opponent, game_map, x + 2) == 0 and \
                                    win_check_ai(map2, self.number, game_map, x + 2) == 0:
                                return x + 2

                    if y - 1 >= 0 and x - 1 >= 0:
                        if game_map[y][x - 1] != 0 and game_map[y - 1][x - 1] == 0:
                            if win_check_ai(map2, opponent, game_map, x - 1) == 0 and \
                                    win_check_ai(map2, self.number, game_map, x - 1) == 0:
                                return x - 1

        for x in range(3, len(game_map[0])):
            for y in range(len(game_map) - 2):
                if game_map[y][x] != player_num:
                    continue

                elif game_map[y + 1][x - 1] == player_num:
                    if y + 2 < 5 and x - 2 >= 0:
                        if game_map[y + 3][x - 2] != 0 and game_map[y + 2][x - 2] == 0:
                            if win_check_ai(map2, opponent, game_map, x - 2) == 0 and \
                                    win_check_ai(map2, self.number, game_map, x - 2) == 0:
                                return x - 2

                    elif y + 2 == 5 and x - 2 >= 0:
                        if game_map[y + 2][x - 2] == 0:
                            if win_check_ai(map2, opponent, game_map, x - 2) == 0 and \
                                    win_check_ai(map2, self.number, game_map, x - 2) == 0:
                                return x - 2

                    if y - 1 >= 0 and x + 1 < 6:
                        if game_map[y][x + 1] != 0 and game_map[y - 1][x + 1] == 0:
                            if win_check_ai(map2, opponent, game_map, x + 1) == 0 and \
                                    win_check_ai(map2, self.number, game_map, x + 1) == 0:
                                return x + 1

        return -1

    def get_drop_input(self, game_map):

        if self.number == 1:
            opponent = 2

        else:
            opponent = 1

        res1 = check_opponent_win(game_map, self.number)
        res = check_opponent_win(game_map, opponent)

        if res1 != -1:
            return res1

        if res != -1:
            return res

        map2 = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]

        for v in range(len(game_map)):
            for y in range(len(game_map[0])):
                map2[v][y] = game_map[v][y]

        res3 = self.win_check_3(game_map, self.number, opponent)
        res4 = self.win_check_3(game_map, opponent, opponent)

        if res3 != -1:
            return res3

        if res4 != -1:
            return res4

        # 3

        for x in range(len(game_map)):
            for y in range(len(game_map[0])):
                map2[x][y] = game_map[x][y]

        check_list = [3, 4, 2, 5, 1, 0, 6]

        for c in range(len(check_list)):
            if win_check_ai(map2, opponent, game_map, check_list[c]) == 0 and\
                    win_check_ai(map2, self.number, game_map, check_list[c]) == 0:
                return check_list[c]

            for x in range(len(game_map)):
                for y in range(len(game_map[0])):
                    map2[x][y] = game_map[x][y]

        for b in range(len(check_list)):
            if game_map[0][check_list[b]] == 0:
                return check_list[b]

        return 1