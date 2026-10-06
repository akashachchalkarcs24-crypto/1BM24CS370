def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def get_input(name):
    print("Enter", name, "state:")
    return list(map(int, input("Enter 9 numbers: ").split()))

def heuristic(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            current_row = i // 3
            current_col = i % 3

            goal_pos = goal.index(state[i])
            goal_row = goal_pos // 3
            goal_col = goal_pos % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance

def get_moves(state):
    moves = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    if row > 0:
        moves.append(("UP", zero - 3))

    if row < 2:
        moves.append(("DOWN", zero + 3))

    if col > 0:
        moves.append(("LEFT", zero - 1))

    if col < 2:
        moves.append(("RIGHT", zero + 1))

    return moves

def astar(start, goal):

    open_list = [
        (heuristic(start, goal), 0, start, [], [])
    ]

    visited = set()

    while open_list:

        open_list.sort(key=lambda x: x[0])

        f, g, state, path, moves = open_list.pop(0)

        if state == goal:
            return path + [state], moves

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        for move, new_pos in get_moves(state):

            new_state = state.copy()

            zero = new_state.index(0)

            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]

            if tuple(new_state) not in visited:

                new_g = g + 1
                h = heuristic(new_state, goal)
                new_f = new_g + h

                open_list.append(
                    (
                        new_f,
                        new_g,
                        new_state,
                        path + [state],
                        moves + [move]
                    )
                )

    return None, None

start = get_input("INITIAL")
goal = get_input("GOAL")

print("\nINITIAL STATE:")
show(start)

path, moves = astar(start, goal)

if path is None:

    print("No solution found!")

else:

    
    print("       SOLUTION FOUND")
    
    print("Total Steps:", len(moves))

    for i in range(len(path)):

        print("\nStep", i)

        if i > 0:
            print("Move:", moves[i-1])

        show(path[i])

    print("Goal State Reached!")
