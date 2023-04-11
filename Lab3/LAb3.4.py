from constraint import *

def is_simona_present(simona):
    return simona == 1

def is_valid_time_for_marija(marija, time):
    if marija == 1 and time not in [14, 15, 18]:
        return False
    return True

def is_valid_time_for_petar(petar, time):
    if petar == 1 and time not in [12, 13, 16, 17, 18, 19]:
        return False
    return True

def is_valid_time_for_simona(simona, time):
    if simona == 1 and time not in [13, 14, 16, 19]:
        return False
    return True

def is_valid_combination(simona, marija, petar, time):
    if not is_simona_present(simona):
        return False
    if not is_valid_time_for_marija(marija, time):
        return False
    if not is_valid_time_for_petar(petar, time):
        return False
    if not is_valid_time_for_simona(simona, time):
        return False
    if simona == 1 and (marija == 1 or petar == 1):
        return False
    return True

if __name__ == 'main':
    problem = Problem(BacktrackingSolver())
    # ---Add the variables and their domains-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 21))
    # ----------------------------------------------------

    # ---Add the constraints------------------
    problem.addConstraint(is_valid_combination, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]
