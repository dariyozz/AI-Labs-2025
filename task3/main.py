import random
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, position):
        self.x, self.y = position


class Game:
    def __init__(self, width, height, field):
        self.width = width
        self.height = height
        self.field = field

    def is_valid_position(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width

    def has_dots(self):
        for row in self.field:
            if '.' in row:
                return True
        return False

    def eat_dot(self, x, y):
        if self.field[x][y] == '.':
            self.field[x][y] = '#'


class Pacman:
    def __init__(self, game):
        self.player = Player()
        self.game = game

    def play_game(self):
        if not self.game.has_dots():
            print("Nothing to do here")
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        while self.game.has_dots():
            x, y = self.player.x, self.player.y
            possible_moves = []

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.game.is_valid_position(nx, ny):
                    if self.game.field[nx][ny] == '.':
                        possible_moves.append((nx, ny))

            if not possible_moves:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if self.game.is_valid_position(nx, ny):
                        possible_moves.append((nx, ny))

            if possible_moves:
                next_move = random.choice(possible_moves)
                self.player.move(next_move)
                self.game.eat_dot(next_move[0], next_move[1])
                print(f"Player moved to ({self.player.x}, {self.player.y})")


if __name__ == "__main__":
    width = int(input().strip())
    height = int(input().strip())
    field = [list(input().strip()) for _ in range(height)]

    game = Game(width, height, field)
    pacman = Pacman(game)
    pacman.play_game()
