# 375465
def play(numPlayers, numMarbles):
    players = {}
    for i in range(numPlayers):
        player = i
        players[player] = 0
    trackList = [0, 2, 1, 3]
    curr_index = 3
    curr_player = 3
    for i in range(4, numMarbles):
        if i % 23 == 0:
            players[curr_player] += i
            curr_index = (curr_index - 7) % len(trackList)
            #print(players[curr_player], trackList[curr_index - 1:curr_index + 1])
            num = trackList.pop(curr_index)
            players[curr_player] += num
            #print(trackList[curr_index])
        else:
            if curr_index == len(trackList) - 1:
                curr_index = 1
            # elif curr_index == len(trackList) - 2 and shifted % 2 != 0:
            #     curr_index = 0
            else:
                curr_index += 2
            trackList.insert(curr_index, i)
        if curr_player == numPlayers - 1:
            curr_player = 0
        else:
            curr_player += 1
        # print(len(trackList))
    print(max(players.values()))
    return max(players.values())

numPlayers = 478
numMarbles = 71241

print(play(478, 7124000))
assert (play(9, 26) == 32)
assert (play(10, 1618) == 8317)
assert (play(21, 6111) == 54718)
assert (play(17, 1104) == 2764)
assert (play(13, 7999) == 146373)
assert (play(30, 5807) == 37305)
