# 375465
import time
'''
Almost 2.5 * 10^13 iteration for part 2.
'''
def play(numPlayers, numMarbles):
    players = {}
    for i in range(numPlayers):
        player = i
        players[player] = 0
    trackList = [0, 2, 1, 3]
    curr_index = 3
    curr_player = 3
    print('Getting all sums....')
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
    print('Done')
    print(max(players.values()))
    return max(players.values())


start_time = time.time()
print(play(478, 71240))
print("--- %s seconds ---" % (time.time() - start_time))
'''
Almost 26020901607000 iteration for part 2.
10254 times slower than part 1 -> around 1h30 min of running?
'''
# print(play(478, 7124000))
assert (play(9, 26) == 32)
assert (play(10, 1618) == 8317)
assert (play(21, 6111) == 54718)
assert (play(17, 1104) == 2764)
assert (play(13, 7999) == 146373)
assert (play(30, 5807) == 37305)
