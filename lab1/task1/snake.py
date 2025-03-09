from searching_framework import Problem, breadth_first_graph_search


class SnakeProblem(Problem):
    def __init__(self, initial, goal=None, grid_size=10):
        super().__init__(initial, goal)
        self.grid_size = grid_size

    def successor(self, state):
        successors = {}
        head, direction, body, green_apples = state

        # Define movement vectors for (right, down, left, up)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up

        # Define possible moves (continue moving in the current direction, turn right, turn left)
        possible_moves = [
            ("ProdolzhiPravo", direction),  # Continue moving in the current direction
            ("SvrtiDesno", (direction + 1) % 4),  # Turn right
            ("SvrtiLevo", (direction - 1) % 4)  # Turn left
        ]

        for action, new_direction in possible_moves:
            dx, dy = directions[new_direction]  # Get direction change based on new_direction
            new_head = (head[0] + dx, head[1] + dy)  # Calculate the new head position

            # Check if the new position is within bounds and not colliding with the body
            if 0 <= new_head[0] < self.grid_size and 0 <= new_head[1] < self.grid_size:
                if new_head not in body:  # Check if the snake collides with its body
                    # If the snake eats an apple, it doesn't lose its tail
                    if new_head in green_apples:
                        new_body = [new_head] + list(body)  # Grow the snake
                        new_green_apples = tuple(a for a in green_apples if a != new_head)  # Remove the eaten apple
                    else:
                        new_body = [new_head] + list(body[:-1])  # Regular move, tail is removed
                        new_green_apples = green_apples

                    # Store the successor state
                    successors[action] = (new_head, new_direction, tuple(new_body), new_green_apples)

        # If no valid actions, return an empty dictionary (indicating no moves)
        return successors if successors else {}

    def actions(self, state):
        valid_actions = list(self.successor(state).keys())

        # If there are no valid actions, return an empty list
        return valid_actions if valid_actions else []

    def result(self, state, action):
        # Safely get the resulting state for the given action
        successors = self.successor(state)
        if action in successors:
            return successors[action]
        return state  # Return the same state if action is invalid (should not happen)

    def goal_test(self, state):
        return len(state[3]) == 0  # Goal: No green apples left


if __name__ == '__main__':
    # Read input
    N = int(input())  # Number of green apples
    green_apples = tuple(tuple(map(int, input().split(','))) for _ in range(N))
    M = int(input())  # Number of red apples (though they're not used in the logic)
    red_apples = set(tuple(map(int, input().split(','))) for _ in range(M))

    # Initial state (head, direction, body, green apples)
    # The snake starts at (0, 0), (0, 1), (0, 2) and moves to the right (direction = 0)
    initial_state = ((0, 2), 0, ((0, 1), (0, 0)), green_apples)

    # Create problem instance
    problem = SnakeProblem(initial_state, goal=())

    # Solve the problem using breadth-first search
    solution = breadth_first_graph_search(problem)

    # Print the solution (sequence of actions)
    if solution:
        print(solution.solution())
