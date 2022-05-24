import math

file = open("liczby.txt").readlines()


# 4.1
def first():
    print("Zadanie 4.1")
    ctr = 0
    first = False
    solv = 0
    for line in file:
        val = line[:-1]
        if val[0] == val[-1]:
            if not first:
                solv = val
                first = True
            ctr += 1

    print(str(solv) + ', ' + str(ctr))


# 4.2

nums = []


def second():
    print("Zadanie 4.2")
    divs = []
    divs_notset = []
    for line in file:
        val = int(line[:-1])
        div = []
        x = 2
        nums.append(val)
        while val != 1:
            if val % x == 0:
                val = int(val / x)
                div.append(x)
                x = 2
            else:
                x += 1
        divs.append(set(div))
        divs_notset.append(div)

    lens = []
    for div in divs_notset:
        lens.append(len(div))
    for div in divs_notset:
        if len(div) == max(lens):
            print(str(nums[divs_notset.index(div)]) + str(div))

    lens = []
    for div in divs:
        lens.append(len(div))
    for div in divs:
        if len(div) == max(lens):
            print(str(nums[divs.index(div)]) + str(div))


# 4.3

def third():
    print("Zadanie 4.3")
    nums = []
    for line in file:
        nums.append(int(line[:-1]))
    nums = list(set(nums))
    nums.sort(reverse=True)
    tres = []
    for num in nums:
        for d1 in nums:
            if num != d1 and num % d1 == 0:
                for d2 in nums:
                    if d2 != d1 and d1 % d2 == 0:
                        tres.append(str([d2, d1, num]))

    cinco = []
    for num in nums:
        for d1 in nums:
            if num != d1 and num % d1 == 0:
                for d2 in nums:
                    if d2 != d1 and d1 % d2 == 0:
                        for d3 in nums:
                            if d3 != d2 and d2 % d3 == 0:
                                for d4 in nums:
                                    if d4 != d3 and d3 % d4 == 0:
                                        cinco.append(str([d4, d3, d2, d1, num]))

    print("a)" + str(len(tres)))
    print("b)" + str(len(cinco)))


first()
second()
third()

# OUT
# Zadanie 4.1
# 93639, 18
# Zadanie 4.2
# 99792[2, 2, 2, 2, 3, 3, 3, 3, 7, 11]
# 20992[2, 2, 2, 2, 2, 2, 2, 2, 2, 41]
# 56064[2, 2, 2, 2, 2, 2, 2, 2, 3, 73]
# 62790{2, 3, 5, 7, 13, 23}
# Zadanie 4.3
# a)27
# b)2
