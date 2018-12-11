# 375465
import time

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
            num = trackList.pop(curr_index)
            players[curr_player] += num
        else:
            if curr_index == len(trackList) - 1:
                curr_index = 1
            else:
                curr_index += 2
            trackList.insert(curr_index, i)
        if curr_player == numPlayers - 1:
            curr_player = 0
        else:
            curr_player += 1
    return max(players.values())

'''
We need to create an array with fixed size to handle resizing at each insert
Insert: O(n)
getItem: O(1)
'''
def play_large(numPlayers, numMarbles):
    players = {}
    for i in range(numPlayers):
        player = i
        players[player] = 0
    trackList = [0, 2, 1, 3]
    for i in range (4, numMarbles):
        trackList.append(-1)
    print('Initiaize complete')
    curr_index = 3
    curr_player = 3
    print('Getting all sums....')
    curr_length = 3
    for i in range(4, numMarbles):
        if trackList[i] == -2:
            curr_index += 1
        if i % 23 == 0:
            players[curr_player] += i
            curr_index = (curr_index - 7) % curr_length
            num = trackList[i]
            trackList[i] = -2
            curr_index += 1
            players[curr_player] += num
        else:
            if curr_index == 3:
                curr_index = 1
            else:
                curr_index += 2
            trackList[curr_index] = i
        if curr_player == numPlayers - 1:
            curr_player = 0
        else:
            curr_player += 1
        curr_length += 1
    return max(players.values())
    
print(play(478, 71240))
start_time = time.time()
print(play_large(478, 71240))
print("--- %s seconds ---" % (time.time() - start_time))
'''
3037741441
2311699176
'''
# print(play(478, 7124000))
assert (play(9, 26) == 32)
assert (play(10, 1618) == 8317)
assert (play(21, 6111) == 54718)
# assert (play(17, 1104) == 2764)
assert (play(13, 7999) == 146373)
assert (play(30, 5807) == 37305)
