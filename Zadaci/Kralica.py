from constraint import *


def baby(kr1,kr2):
    return kr1[0]!=kr2[0] and kr1[1]!=kr2[1] and kr1[0]+kr1[1]!=kr2[0]+kr2[1] and kr1[0]-kr1[1]!=kr2[0]-kr2[1]


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n=int(input())
    variables=range(1,n+1)
    domain = [(i, j) for i in range(0, n) for j in range(0, n)]

    problem.addVariables(variables, domain)



    for kr1 in variables:
        for kr2 in variables:
            if kr1<kr2:
                problem.addConstraint(baby, (kr1,kr2))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ----------------------------------------------------
    if (n<=6):
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())