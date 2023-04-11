from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", ...)
    problem.addVariable("Simona_prisustvo", ...)
    problem.addVariable("Petar_prisustvo", ...)
    problem.addVariable("vreme_sostanok", ...)
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]