# A* Algorithm for 8-Puzzle Problem

import heapq

class PuzzleAStar:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def heuristic(self, state):
        return sum(s != g for s, g in zip(state, self.goal))

    def get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)
        row, col = divmod(zero_index, 3)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(tuple(new_state))
        return neighbors

    def a_star(self):
        heap = []
        heapq.heappush(heap, (0, self.start, []))
        visited = set()

        while heap:
            cost, state, path = heapq.heappop(heap)

            if state == self.goal:
                return path

            if state in visited:
                continue
            visited.add(state)

            for neighbor in self.get_neighbors(state):
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + self.heuristic(neighbor), neighbor, path + [neighbor]))

start_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
puzzle_astar = PuzzleAStar(start_state, goal_state)
print("A* Solution:", puzzle_astar.a_star())
