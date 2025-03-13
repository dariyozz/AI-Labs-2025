
from searching_framework import Problem, breadth_first_graph_search



def is_around_obstacle(pos_ball, obstacles):
    for obstacle in obstacles:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if pos_ball[0] == obstacle[0] + i and pos_ball[1] == obstacle[1] + j:
                    return True

def check_valid(state, obstacles):
    if state[0] in obstacles or state[1] in obstacles:
        return False
    if is_around_obstacle(state[1], obstacles):
        return False
    return 0 <= state[0][0] < 8 and 0 <= state[0][1] < 6 and \
        0 <= state[1][0] < 8 and 0 <= state[1][1] < 6



class FootballProblem(Problem):
    # state : ({pos_player}, {pos_ball})
    def __init__(self, initial, obstacles, goal_, goal=None):
        super().__init__(initial, goal)
        self.obstacles_coord = obstacles
        self.goal_coord = goal_

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
        pos_player = state[0]
        pos_ball = state[1]
        successors = {}

        all_moves = [(0, 1) ,(0, -1) ,(1, 0), (1 ,1) ,(1 ,-1)]
        move_names = [
            "gore",
            "dolu",
            "desno",
            "gore-desno",
            "dolu-desno"
        ]

        for i in range(len(all_moves)):
            is_ball = False
            new_pos_player = (pos_player[0] + all_moves[i][0] ,pos_player[1] + all_moves[i][1])
            if new_pos_player == pos_ball:
                new_pos_ball = (pos_ball[0] + all_moves[i][0], pos_ball[1] + all_moves[i][1])
                is_ball = True
                new_state = (new_pos_player, new_pos_ball)
            else:
                new_state = (new_pos_player, pos_ball)

            if check_valid(new_state, self.obstacles_coord):
                action_name = "Turni topka " if is_ball else "Pomesti coveche "
                action_name += move_names[i]
                successors[action_name] = new_state

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
        return state[1] in self.goal_coord

if __name__ == '__main__':
    pos_player = tuple([int(n) for n in input().split(",")])
    pos_ball = tuple([int(n) for n in input().split(",")])
    obstacles = ((3 ,3), (5 ,4))
    goal = ((7 ,2), (7 ,3))
    initial_state = (pos_player, pos_ball)
    p = FootballProblem(initial_state, obstacles, goal)
    solution = breadth_first_graph_search(p)
    print(solution.solution() if solution is not None else "No Solution!")