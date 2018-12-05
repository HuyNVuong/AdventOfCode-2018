import datetime
import operator
from collections import Counter

'''
Part 1. Find guard that have longest nap, assume that each nap is no longer
than 60 minutes
'''
def guard_list(shifts):
    dict = {}
    for i in range (len(shifts)):
        activity = str(shifts[i][1])
        if activity.strip() == 'wakes up':
            if aSleep is True:
                time_slept = (shifts[i][0].minute, shifts[i - 1][0].minute)
                if (guard_id not in dict.keys()):
                    dict.setdefault(guard_id, [])
                    dict[guard_id].append(time_slept)
                else:
                    dict[guard_id].append(time_slept)
            aSleep = False
        elif activity.strip() == 'falls asleep':
            aSleep = True
        else :
            guard_id =  [int(s) for s in activity.replace('#', '').split() if s.isdigit()][0]
            aSleep = False
    return dict

def find_spleepiest_guard(guardList):
    longestNap = []
    guard_id_max = []
    for guard_id, naps in guardList.items():
        napTime = sum([nap[0] - nap[1] for nap in naps])
        if longestNap == []:
            longestNap.append(napTime)
            guard_id_max.append(guard_id)
        elif napTime > max(longestNap):
            longestNap.append(napTime)
            guard_id_max.append(guard_id)
    return guard_id_max[len(guard_id_max) - 1]

def find_sleepiest_interval(sleepiestGuard_id, guardList):
    minutes = Counter()
    for nap in guardList[sleepiestGuard_id]:
        for minute in range(nap[1], nap[0]):
            minutes[minute] += 1
    [(sleepiestMin, count)] = minutes.most_common(1)
    # return sleepiestMin
    # Modified for part 2
    return [(sleepiestMin, count)]

'''
Part 2. In this case, we assume every one are sleepiest,
then we find the most sleepist time among each inividual, then return the total
'''
def find_sleepiest_minute(guardList):
    curr_count = 0
    sleepiestMin = []
    for guard_id in guardList.keys():
        if curr_count < find_sleepiest_interval(guard_id, guardList)[0][1]:
            curr_count = find_sleepiest_interval(guard_id, guardList)[0][1]
            sleepiestMin.append(guard_id)
            sleepiestMin.append(find_sleepiest_interval(guard_id, guardList))
    return sleepiestMin[(len(sleepiestMin) - 2):(len(sleepiestMin))]

with open('day_4.in') as f:
    allStrings = [line.strip() for line in f]
    sortedShifts = []
    aSleep = False
    for string in allStrings:
        stringSplit = string.split(']')
        timeStampsStr = stringSplit[0].strip('[')
        date = datetime.datetime.strptime(timeStampsStr, '%Y-%m-%d %H:%M')
        activity = stringSplit[1]
        sortedShifts.append((date, activity))
        sortedShifts.sort(key=lambda x: x[0])

guardList = guard_list(sortedShifts)
sleepiestGuard = find_spleepiest_guard(guardList)
sleepiestInterval = find_sleepiest_interval(sleepiestGuard, guardList)
print(sleepiestGuard)
# print(sleepiestGuard * sleepiestInterval)
sleepiestMinuteAmongAll = find_sleepiest_minute(guardList)
print(sleepiestMinuteAmongAll)
print(sleepiestMinuteAmongAll[0] * sleepiestMinuteAmongAll[1][0][0]) #Yuck, use a class!

'''
Unit testing
'''

TEST_1 = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift'
]

# assert find_spleepiest_guard(TEST_1) == 10
