states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = {"k1": {"id", "nv", "ut"}, "k2": {"wa", "id", "mt"}, "k3": {"or", "nv", "ca"}, "k4": {"nv", "ut"},
            "k5": {"ca", "az"}}
final_stations = set()

while states_needed:
    best_stations = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_stations = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_stations)

print(final_stations)

