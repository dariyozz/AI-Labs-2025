from enum import Enum

from searching_framework import *

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Moves(Enum):
    MOVE_RIGHT = (1, 0)
    MOVE_LEFT = (-1, 0)
    MOVE_UP = (0, 1)
    MOVE_DOWN = (0, -1)


def is_valid_move(state, red_coordinates):
    head = state[0][-1]
    if head in state[0][:-1]: return False
    if head in red_coordinates: return False
    return 0 <= head[0] < 10 and 0 <= head[1] < 10

# state = ( {site koordinati na zmijata}, {direction} , {koordinati na zeleni jabuki}
def move_left(state, red_coordinates):
    snake_body = list(state[0])
    snake_head = state[0][-1]
    green_coordinates = list(state[-1])
    offset, new_dir = None, None

    if state[1] == Direction.DOWN.value:
        new_dir = Direction.RIGHT.value
        offset = Moves.MOVE_RIGHT.value

    elif state[1] == Direction.UP.value:
        new_dir = Direction.LEFT.value
        offset = Moves.MOVE_LEFT.value

    elif state[1] == Direction.RIGHT.value:
        new_dir = Direction.UP.value
        offset = Moves.MOVE_UP.value

    elif state[1] == Direction.LEFT.value:
        new_dir = Direction.DOWN.value
        offset = Moves.MOVE_DOWN.value

    new_head = tuple(a + b for a, b in zip(snake_head, offset))

    if new_head in green_coordinates:
        green_coordinates.remove(new_head)
    else:
        snake_body = snake_body[1:]
    snake_body.append(new_head)
    new_state = (tuple(snake_body), new_dir, tuple(green_coordinates))
    return new_state


def keep_straight(state, red_coordinates):
    snake_body = list(state[0])
    snake_head = state[0][-1]
    green_coordinates = list(state[-1])

    current_dir = state[1]

    offset_map = {
        Direction.UP.value: Moves.MOVE_UP.value,
        Direction.RIGHT.value: Moves.MOVE_RIGHT.value,
        Direction.DOWN.value: Moves.MOVE_DOWN.value,
        Direction.LEFT.value: Moves.MOVE_LEFT.value
    }

    offset = offset_map[current_dir]
    new_head = tuple(a + b for a, b in zip(snake_head, offset))

    # ako ne se griznala ima 2 opcii, novo pole e jabolko, i novo pole ne e jabolko
    if new_head in green_coordinates:
        green_coordinates.remove(new_head)
    else:
        snake_body = snake_body[1:]
    snake_body.append(new_head)
    new_state = (tuple(snake_body), current_dir, tuple(green_coordinates))
    return new_state

def move_right(state, red_coordinates):
    snake_body = list(state[0])
    snake_head = state[0][-1]
    green_coordinates = list(state[-1])
    offset, new_dir = None, None

    if state[1] == Direction.DOWN.value:
        new_dir = Direction.LEFT.value
        offset = Moves.MOVE_LEFT.value

    elif state[1] == Direction.UP.value:
        new_dir = Direction.RIGHT.value
        offset = Moves.MOVE_RIGHT.value

    elif state[1] == Direction.RIGHT.value:
        new_dir = Direction.DOWN.value
        offset = Moves.MOVE_DOWN.value

    elif state[1] == Direction.LEFT.value:
        new_dir = Direction.UP.value
        offset = Moves.MOVE_UP.value

    new_head = tuple(a + b for a, b in zip(snake_head, offset))
    if new_head in green_coordinates:
        green_coordinates.remove(new_head)
    else:
        snake_body = snake_body[1:]
    snake_body.append(new_head)
    new_state = (tuple(snake_body), new_dir, tuple(green_coordinates))
    return new_state


class SnakeProblem(Problem):
    def __init__(self, initial, red_coordinates, goal=None):
        super().__init__(initial, goal)
        self.red_coordinates = red_coordinates

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.

        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        successors = {}
        straight = keep_straight(state, self.red_coordinates)
        left = move_left(state, self.red_coordinates)
        right = move_right(state, self.red_coordinates)
        func_names = ["ProdolzhiPravo", "SvrtiLevo", "SvrtiDesno"]

        for move, func_name in zip([straight, left, right], func_names):
            if is_valid_move(move, red_coordinates):
                successors[func_name] = move

        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return len(state[-1]) == 0

if __name__ == '__main__':
    # print("Read the input, create an instance of your problem class and use the searching algorithms here")
    green_coordinates = []
    red_coordinates = []
    num_green = int(input())
    for _ in range (num_green):
        input_ = [int(num) for num in input().split(",")]
        green_coordinates.append(tuple(input_))
    num_red = int(input())
    for _ in range (num_red):
        input_ = [int(num) for num in input().split(",")]
        red_coordinates.append(tuple(input_))

    snake_body = ((0,9), (0,8), (0,7))
    initial_state = (snake_body, Direction.DOWN.value, tuple(green_coordinates))
    # state = ( {site koordinati na zmijata}, {direction} , {koordinati na zeleni jabuki}
    s = SnakeProblem(initial_state, red_coordinates)
    solution = breadth_first_graph_search(s)
    if solution is not None:
        print(solution.solution())