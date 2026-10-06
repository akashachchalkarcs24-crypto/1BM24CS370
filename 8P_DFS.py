def show(state):
    for i in range(0,9,3):
        print(state[i], state[i+1], state[i+2])
    print()

def get_input(name):
    print("Enter", name, "state:")
    state = list(map(int, input("Enter 9 numbers separated by space: ").split()))
    return state

def get_moves(state):
    moves = []
    pos = state.index(0)

    row = pos // 3
    col = pos % 3

    if row > 0:
        moves.append(("UP", pos - 3))

    if row < 2:
        moves.append(("DOWN", pos + 3))

    if col > 0:
        moves.append(("LEFT", pos - 1))

    if col < 2:
        moves.append(("RIGHT", pos + 1))

    return moves

def dfs(start, goal):

    stack = [(start, [], [])]
    visited = set()

    while stack:

        state, path, moves = stack.pop()

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        if state == goal:
            return path + [state], moves

        for move, new_pos in get_moves(state):

            new_state = state.copy()
            zero = new_state.index(0)

            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]

            stack.append((
                new_state,
                path + [state],
                moves + [move]
            ))

    return None, None




start = get_input("INITIAL")
goal = get_input("GOAL")

print("\nInitial State:")
show(start)

path, moves = dfs(start, goal)

if path is None:
    print("No solution found!")

else:
    print("Solution Found!")
    print("Total Steps:", len(moves))

    for i in range(len(path)):
        print("Step", i)

        if i > 0:
            print("Move:", moves[i-1])

        show(path[i])

    print("Goal State Reached!")