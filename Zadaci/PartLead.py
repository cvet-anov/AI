from constraint import *

if __name__ == '__main__':

    problem = Problem(BacktrackingSolver())


    NumberofParticipants = int(input())
    Participants = {}

    for i in range(NumberofParticipants):
        row = input().split(" ")
        Participants[float(row[0])] = row[1]

    NumberOfLeaders = int(input())
    Leaders = {}

    for i in range(NumberOfLeaders):
        row = input().split(" ")
        Leaders[float(row[0])] = row[1]

    leader_values = Leaders.keys()
    participant_values = Participants.keys()

    problem.addVariable(1, Domain(leader_values))
    problem.addVariables(range(2, 7), Domain(participant_values))

    mace=[1, 2, 3, 4, 5, 6]
    problem.addConstraint(MaxSumConstraint(100), mace)
    problem.addConstraint(AllDifferentConstraint(), mace)


    solutions = problem.getSolutions()
    solutions.sort(key=lambda e: sum(e.values()), reverse=True)
    solution = solutions[0]
    print(f'Total score: {round(sum(solution.values()), 1)}')
    for i in solution:
        if i == 1:
            print(f'Team leader: {Leaders[solution[i]]}')
        else:
            print(f'Participant {i - 1}: {Participants[solution[i]]}')

