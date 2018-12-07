# coding:utf-8

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])  # 要覆盖的州

stations = dict()  # 可选择的广播台清单
stations["kone"] = set(['id', 'nv', 'ut'])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()   # 存储最终选择的广播台

while states_needed:

    best_station = None     # 覆盖了最多的未覆盖州的广播台
    states_covered = set()    # 该广播台覆盖的所有覆盖的州

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    states_needed -= states_covered
print(final_stations)
