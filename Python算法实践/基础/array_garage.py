"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.
Say the initial state is an array:
[1, 2, 3, 0, 4],
where 1, 2, 3, 4 are different cars, and 0 is the empty spot.
And the final state is
[0, 3, 2, 1, 4].
We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.
Each step swap with 0 only.
Edit:
Now also prints the sequence of changes in states.
Output of this example :-
initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence :
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4
"""
# 0代表空位，每步只可移动一辆车到空位，最少步数达到目标要求
# 思路：利用0来定位，获取initial里0的index,再获取final对应index值n，在initial里n值和0值位置互换,循环,直到initial==final
# ps.seq.append(initial[::])里initial[::]的作用是复制，直接用initial会用最后一次的值覆盖前面的，
# 原因是append添加的是地址、引用，当这个引用内容被改变时，前面添加的相同地址的内容也随之改变


def garage(initial, final):

    initial = initial[::]      # prevent changes in original 'initial'
    seq = []                   # list of each step in sequence
    steps = 0
    while initial != final:
        # 这里可以是0，可以是1，可以是2，3，4，结果不变
        zero = initial.index(0)
        if zero != final.index(0):  # if zero isn't where it should be,
            car_to_move = final[zero]   # what should be where zero is,
            pos = initial.index(car_to_move)         # and where is it?
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        seq.append(initial[::])
        steps += 1

    return steps, seq
    # e.g.:  4, [{0, 2, 3, 1, 4}, {2, 0, 3, 1, 4},
    #            {2, 3, 0, 1, 4}, {0, 3, 2, 1, 4}]


"""
thus:
1 2 3 0 4 -- zero = 3, true, car_to_move = final[3] = 1,
             pos = initial.index(1) = 0, switched [0], [3]
0 2 3 1 4 -- zero = 0, f, initial[1] != final[1], switched 0,1
2 0 3 1 4 -- zero = 1, t, car_to_move = final[1] = 3,
             pos = initial.index(3) = 2, switched [1], [2]
2 3 0 1 4 -- zero = 2, t, car_to_move = final[2] = 2, 
             pos = initial.index(2) = 0, switched [0], [2]
0 3 2 1 4 -- initial == final
"""

print(garage([1, 2, 3, 0, 4], [0, 3, 2, 1, 4]))
