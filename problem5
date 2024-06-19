# HELPER FUNCTIONS
# Use these functions to quickly get your inputs from your input file,
# and write your outputs to an output file.

# The name of your input file.
file_input_name = "input.txt"
# The name of your output file.
file_output_name = "output.txt"

IGNORE_ME_file_input = open(file_input_name, 'r')
IGNORE_ME_file_output = open(file_output_name, 'w')
IGNORE_ME_file_output_storage = []

# Get the next line from your input file.
# You may optionally pass a string argument for debug print statements. This parameter can be skipped.
# Example:
# cases = input()
# length = input("Length of the box")
def input(ignored=None):
    if ignored != None:
        print("Reading {}".format(ignored))
    return IGNORE_ME_file_input.readline().strip()

# Write a string to your output file.
# You must pass a string argument to be written to the file.
# Example:
# output("Case #{}: {}".format(case, result))
def output(output):
    print("Writing line: {}".format(output))
    IGNORE_ME_file_output_storage.append(output + "\n")

# Saves your output file and makes it ready for submission.
# You must put this at the end of your code.
# Do not pass any arguments.
def submit():
    IGNORE_ME_file_output_storage[-1] = IGNORE_ME_file_output_storage[-1].strip()
    IGNORE_ME_file_output.writelines(IGNORE_ME_file_output_storage)
    IGNORE_ME_file_output.close()
    print("Saved and finished! Send your output file called {}".format(file_output_name))
#
# Good luck!
# ----------------------------------------------------
import heapq
from heapq import heappop, heappush

class Island():
    def __init__(self, id):
        self.id = id
        self.bridges = []
    def __repr__(self):
        return str(self.id)
    def add_bridge(self, bridge):
        self.bridges.append(bridge)

class Bridge():
    def __init__(self, start, end, time, price=0):
        self.start = start
        self.end = end
        self.time = time
        self.price = price
    def __repr__(self):
        return "bridge = Bridge({}, {}, {}, {})".format(self.start, self.end, self.time, self.price)

def find_fastest_path(islands, start_id, end_id, budget):
    distances = {island.id: float('inf') for island in islands}
    predecessors = {island.id: None for island in islands}
    distances[start_id] = 0
    pq = [(0, start_id)]  # (distance, island_id)
    while pq:
        curr_distance, curr_island_id = heapq.heappop(pq)
        if curr_distance > distances[curr_island_id]:
            continue
        curr_island = next(island for island in islands if island.id == curr_island_id)
        for bridge in curr_island.bridges:
            neighbor_id = bridge.end
            neighbor_distance = distances[curr_island_id] + bridge.time
            if bridge.price <= budget:
                # Update if shorter path found
                if neighbor_distance < distances[neighbor_id]:
                    distances[neighbor_id] = neighbor_distance
                    predecessors[neighbor_id] = (curr_island_id, bridge.time)  # Store the time taken
                    heapq.heappush(pq, (neighbor_distance, neighbor_id))
    path = []
    curr_id = end_id
    while curr_id is not None:
        path.insert(0, curr_id)
        curr_id, time_taken = predecessors[curr_id]
    total_time = distances[end_id]
    total_money_used = sum(bridge.price for bridge in curr_island.bridges if bridge.end in path)
    
    return path, total_time, total_money_used
    
cases = int(input())
for case in range(cases):
    n_islands, n_free, n_paid, budget = [int(x) for x in input().split(" ")]
    #print("{} islands, {} free bridges, {} paid bridges, {} budget".format(n_islands, n_free, n_paid, budget))
    islands = []
    bridges = []
    for island in range(n_islands):
        islands.append(Island(island))
    for free in range(n_free):
        start, end, time = [int(x) for x in input().split(" ")]
        #print("start {}, end {}, time {}".format(start, end, time))
        bridge = Bridge(start, end, time)
        islands[start].add_bridge(bridge)
        #island[end].add_bridge(bridge)
        bridges.append(bridge)
    for paid in range(n_paid):
        start, end, time, cost = [int(x) for x in input().split(" ")]
        #print("start {}, end {}, time {}, cost {}".format(start, end, time, cost))
        bridge = Bridge(start, end, time, cost)
        islands[start].add_bridge(bridge)
        #island[end].add_bridge(bridge)

    print(islands)
    for bridge in bridges:
        print(bridge)
    shortest_path = find_fastest_path(islands, 0, 11, budget)
    print(shortest_path)
    #output("Case #{}: {}".format(case + 1, result))
#submit()
