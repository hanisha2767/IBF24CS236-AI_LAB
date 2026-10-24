
from collections import deque

seq = []
state = None
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def UPDATE_STATE(state, percept):
    return tuple(percept)


def FORMULATE_GOAL(state):
    return goal


def FORMULATE_PROBLEM(state, goal):
    return (state, goal)


def SEARCH(problem):
    initial, goal = problem
    queue = deque([(initial, [])])
    visited = {initial}

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        zero = current.index(0)
        row, col = divmod(zero, 3)

        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]

        for dr, dc, action in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_pos = nr * 3 + nc
                board = list(current)
                board[zero], board[new_pos] = (
                    board[new_pos], board[zero]
                )
                new_state = tuple(board)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(
                        (new_state, path + [action])
                    )

    return None


def FIRST(seq):
    return seq[0]


def REST(seq):
    return seq[1:]


def SIMPLE_PROBLEM_SOLVING_AGENT(percept):
    global seq, state

    state = UPDATE_STATE(state, percept)

    if state == goal:
        return "GOAL REACHED"

    if not seq:
        goal_state = FORMULATE_GOAL(state)
        problem = FORMULATE_PROBLEM(state, goal_state)
        seq = SEARCH(problem)

        if seq is None:
            return "NO SOLUTION"

        if not seq:
            return "GOAL REACHED"

    action = FIRST(seq)
    seq = REST(seq)
    return action


def apply_action(board, action):
    board = list(board)
    zero = board.index(0)
    row, col = divmod(zero, 3)

    moves = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1)
    }

    dr, dc = moves[action]
    new_pos = (row + dr) * 3 + (col + dc)

    board[zero], board[new_pos] = (
        board[new_pos], board[zero]
    )
    return tuple(board)


# Main program
initial = (1, 2, 3, 4, 0, 6, 7, 5, 8)
state = initial

print("Initial State:")
for i in range(0, 9, 3):
    print(state[i:i + 3])

while state != goal:
    action = SIMPLE_PROBLEM_SOLVING_AGENT(state)

    if action in ("NO SOLUTION", "GOAL REACHED"):
        print(action)
        break

    print("\nAction:", action)
    state = apply_action(state, action)

    for i in range(0, 9, 3):
        print(state[i:i + 3])

print("\nGoal Reached!")
