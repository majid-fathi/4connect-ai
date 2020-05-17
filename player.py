class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_drop_input(self, game_map):
        pass


class Person(Player):
    def __init__(self, name, number):
        super().__init__(name, number)

    def get_drop_input(self, game_map):
        raise Exception("get_drop_input() called from Person class")


class AIPlayer(Player):
    def __init__(self, name, number):
        super().__init__(name, number)

    def get_drop_input(self, game_map):
        #  change this method
        for i in range(len(game_map[0])):
            if game_map[0][i] == 0:
                return i
