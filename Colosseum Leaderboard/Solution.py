# n -> total number of events
# winners array -> ith element denotes winner of ith event
# teams are represented with numbers and the SASTRA is represented as 1 always
# find the rank of SASTRA in the Leaderboard by counting the number of victories for each team



def solution(n, winners):
    # Write your code here
    dictt = defaultdict(int)
    for i in winners:
        dictt[i] += 1
    leaderboard = sorted(dictt.values(),reverse= True)
    for i in range(0,len(leaderboard)):
        if leaderboard[i] == dictt[1]:
            return i + 1
