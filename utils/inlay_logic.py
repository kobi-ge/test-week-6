def find_the_furthest(soldiers_list):
    furthest_soldier = soldiers_list[0]
    for soldier in range(len(soldiers_list)):
        if soldiers_list[soldier][5] > furthest_soldier[5]:
            furthest_soldier = soldiers_list[soldier]
    return furthest_soldier

def order_by_distance(soldiers):
    soldiers_copy = soldiers[:]
    ordered_list = []
    for soldier in range(len(soldiers)):
        furthest = find_the_furthest(soldiers_copy)
        ordered_list.append(furthest)
        soldiers_copy.remove(furthest)
    return ordered_list



s = [12,23,34,4532,234]
print(order_by_distance(s))
