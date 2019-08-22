from typing import List
from functools import total_ordering


@total_ordering
class Participant:
    def __init__(self, team, main_rate, extra_rate):
        self.team = team
        self.main_rate = main_rate
        self.extra_rate = extra_rate
        self.counter = 0

    def __lt__(self, other):
        if self.main_rate == other.main_rate:
            if self.extra_rate == other.extra_rate:
                return self.team > other.team
            return self.extra_rate < other.extra_rate
        else:
            return self.main_rate < other.main_rate

    def __eq__(self, other):
        if self.main_rate == other.main_rate and self.extra_rate == other.extra_rate:
            return True
        return False


def rate_all_que(matrix: List[str]):
    rating_que = []
    for j in range(len(matrix[0])):
        rating_que.append(sum([1 if matrix[i][j] == '-' else 0 for i in range(len(matrix))])+1)
    return rating_que


def team_rate(i, matrix: List[str], ques_rate: List):
    main_rate = sum([1 if matrix[i][j] == '+' else 0 for j in range(len(matrix[0]))])
    extra_rate = 0
    for j in range(len(matrix[0])):
        extra_rate += ques_rate[j] * (1 if matrix[i][j] == '+' else 0)
    return main_rate, extra_rate


n, k = [int(i) for i in input().split()]
if n > 0:
    matrix, teams = [], []
    ratings = []
    for i in range(n):
        team_info = input().split()
        teams.append(team_info[0])
        matrix.append("".join(team_info[1:]))

    que_rates = rate_all_que(matrix)
    participates = sorted([Participant(teams[i], *team_rate(i, matrix, que_rates)) for i in range(n)], reverse=True)

    flag, place_range = False, None
    i = 0
    for i in range(n):
        for j in range(n):
            if i != j and participates[i]  == participates[j]:
                participates[i].counter += 1
            elif j > i and participates[i] > participates[j]:
                break

    for num, participate in enumerate(participates):
        if participate.counter == 0:
            flag = False
            print(num+1, participate.team)
        elif not flag:
            place_range = "{0}-{1}".format(num+1, num+1+participate.counter)
            flag = True
            print(place_range, participate.team)
        else:
            print(place_range, participate.team)