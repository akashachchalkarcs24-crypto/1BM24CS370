def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def get_input(name):
    print("Enter", name, "state:")
    return list(map(int, input("Enter 9 numbers: ").split()))

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

def dls(state, goal, depth, path, moves, visited):

    if state == goal:
        return path, moves

    if depth == 0:
        return None, None

    visited.add(tuple(state))

    for move, new_pos in get_moves(state):

        new_state = state.copy()
        zero = new_state.index(0)

        new_state[zero], new_state[new_pos] = \
            new_state[new_pos], new_state[zero]

        if tuple(new_state) not in visited:

            result_path, result_moves = dls(
                new_state,
                goal,
                depth - 1,
                path + [new_state],
                moves + [move],
                visited
            )

            if result_path is not None:
                return result_path, result_moves

    visited.remove(tuple(state))

    return None, None


def iddfs(start, goal):

    depth = 0

    while True:

        print("\nSearching at depth:", depth)

        path, moves = dls(
            start,
            goal,
            depth,
            [start],
            [],
            set()
        )

        if path is not None:
            return path, moves

        depth += 1

start = get_input("INITIAL")
goal = get_input("GOAL")

print("\nINITIAL STATE:")
show(start)

path, moves = iddfs(start, goal)


print("       SOLUTION FOUND")

print("Total Steps:", len(moves))

for i in range(len(path)):

    print("\nStep", i)

    if i > 0:
        print("Move:", moves[i-1])

    show(path[i])

print("Goal State Reached!")