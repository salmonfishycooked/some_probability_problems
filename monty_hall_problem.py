# an experiment about Monty Hall problem
# by sharkie

import random

# the total of experiment times
expTimes = int(1e4)
# the success times if the participant changed door
sucChangeTimes = 0
# the success times if the participant did not change door
sucNoChangeTimes = 0
for i in range(0, expTimes):
    arr = []
    car = -1
    # generate a series of numbers as an initial condition
    for j in range(0, 3):
        num = random.randint(0, 1)
        if num == 1:
            car = j
            arr.append(1)
            while len(arr) <= 2:
                arr.append(0)
            break
        if len(arr) == 2 and num == 0:
            car = 2
            num = 1
        arr.append(num)

    # the participant chooses a door
    choice = random.randint(0, 2)

    # host open a door which is a sheep (he knows the results behind every door)
    # there are three conditions
    # it is guaranteed that the value of opened is different from the value of choice
    opened = -1
    if arr[choice] == 0:
        for idx, v in enumerate(arr):
            if choice != idx and v == 0:
                opened = idx
    else:
        draw = random.randint(0, 1)
        cnt = 0
        for idx, v in enumerate(arr):
            if choice == idx:
                continue
            if cnt == draw:
                opened = idx
                break
            cnt += 1

    # find the remaining door number
    remaining = -1
    for idx, v in enumerate(arr):
        if idx == choice or idx == opened:
            continue
        remaining = idx

    # the participant decides if changing door
    draw = random.randint(0, 1)
    # do not change
    if draw == 0 and choice == car:
        sucNoChangeTimes += 1
    # change
    if draw == 1 and remaining == car:
        sucChangeTimes += 1

print("success times of changing: " + str(sucChangeTimes))
print("success times of no changing: " + str(sucNoChangeTimes))
