import entities.soldier as sol
import handling_csv_file

def create_soldiers(soldiers_list):
    obj_soldiers = []
    for soldier in soldiers_list:
        current_soldier = sol.Soldier(soldier)
        obj_soldiers.append(current_soldier)

    return obj_soldiers