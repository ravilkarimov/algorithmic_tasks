class SnakesLadders():

    def __init__(self):
        self.positions = [0, 0] # players positions
        self.next = 0 # 0 - player #1, 1 - player #2
        self.ladders = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            78: 98,
            87: 94
        }
        self.snakes = {
            16: 6,
            46: 25,
            49: 11,
            62: 19,
            64: 60,
            74: 53,
            89: 68,
            92: 88,
            95: 75,
            99: 80
        }


    def __str__(self):
        return "positions: {}, next: {}".format(self.positions, self.next)


    def change_player(self):
        if self.next == 0:
            self.next = 1
        else:
            self.next = 0 


    def play(self, die1, die2):

        if 100 in self.positions:
            return "Game over!"

        current_position = self.positions[self.next]
        step = die1 + die2
        next_position = current_position + step

        response = ""

        if next_position > 100:
            next_position = 100 - (step - (100 - current_position))
        
        if next_position == 100:
            response = "Player {} Wins!".format(self.next + 1)
        else:
            if self.ladders.get(next_position) != None:
                next_position = self.ladders[next_position]
            elif self.snakes.get(next_position) != None:
                next_position = self.snakes[next_position]
            response = "Player {} is on square {}".format(self.next + 1, next_position)

        self.positions[self.next] = next_position

        if die1 != die2:
            self.change_player()

        return response


game = SnakesLadders()
# print(game.play(1, 1))
# print(game.play(1, 2))
# print(game)
print(game.play(50, 46))
print(game.play(1, 6))
print(game.play(1, 2))
# assert(game.play(1, 1) == "Player 1 is on square 38")
# assert(game.play(1, 5) == "Player 1 is on square 44")
# assert(game.play(50, 46) == "Player 2 is on square 96")
# assert(game.play(1, 6) == "Player 2 is on square 97")