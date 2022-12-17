from queue import PriorityQueue
from collections import deque, defaultdict

def find_max_pressure(valves):
    tick = 30
    paths = [('AA', 0, '')]
    visited = {}
    for t in range(1, tick+1):
        new_paths = []
        for valve, pressure, history in paths:
            
            k = (valve, history)
            if k in visited and visited[k] >= pressure:
                continue
            visited[k] = pressure

            flow_rate, neighbors = valves[valve]
            if (valve not in history or history=='') and flow_rate > 0:
                new_paths.append((valve, pressure+flow_rate*(tick-t), history+valve))
            
            for valve in neighbors:
                new_paths.append((valve, pressure, history))

        paths = new_paths
    print(max(pressure for _,pressure,_ in paths))
def find_max_pressure(valves):

V = {} 

for i,line in enumerate(open(0).read().splitlines()):
    valve_name = line.split()[1]
    valve_fr = int(line.split()[4].split('=')[1].replace(';',''))
    valve_nodes = [*map(lambda x:x.replace(',',''), line.split()[9:])]
    V[valve_name]=[valve_fr, valve_nodes]

find_max_pressure(V)


find_max_pressure_with_elephant(V)

