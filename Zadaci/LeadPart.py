from constraint import *

if name == 'main':

    problem = Problem(BacktrackingSolver())

    members={}
    leaders={}
    total_members = int(input())

    for i in range(total_members):
        string = input().split(" ")
        members[float(string[0])] = string[1]
    total_leaders = int(input())

    for j in range(total_leaders):
        string = input().split(" ")
        leaders[float(string[0])] = string[1]

    leader = leaders.keys()
    member = members.keys()
    #print(leader)
    problem.addVariable(1, Domain(leader))
    problem.addVariables(range(2,7), Domain(member))
    lista = [1,2,3,4,5,6]
    problem.addConstraint(MaxSumConstraint(100), lista)
    problem.addConstraint(AllDifferentConstraint(), lista)

    solutions = problem.getSolutions()
    solutions.sort(key=lambda e: sum(e.values()), reverse=True)
    sol = solutions[0]
    print(f'Total score: {round(sum(sol.values()), 1)}')
    for k in sol:
        if k==1:
            print(f"Team leader: {leaders[sol[k]]}")
        else:
            print(f"Participant {k-1}: {members[sol[k]]}")