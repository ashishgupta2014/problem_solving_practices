def canCompleteCircuit(gas, cost) -> int:
    if (sum(gas) < sum(cost)): return -1
    n = len(gas)
    total_tank, curr_tank = 0, 0  # only total_tank is enough if we want to know we make cycle or not ## curr_tank is for determinig start position
    starting_station = 0
    for i in range(n):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]

        # print( curr_tank, total_tank )

        # If one couldn't get here,
        if curr_tank < 0:
            # Pick up the next station as the starting one.
            starting_station = i + 1
            # Start with an empty tank with next i, starting position
            curr_tank = 0
    return starting_station if total_tank >= 0 else -1


print(canCompleteCircuit([3,3,4],[3,4,4]))