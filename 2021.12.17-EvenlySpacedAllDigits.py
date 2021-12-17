# Name five two-digit numbers that are evenly spaced out—like 32, 34, 36, 38, and 40—in which all 10 digits from 0 to 9 are used once each.

for i in range(10,96):
    for spacing in range(1,25):
        if i + spacing * 4 > 99:
            pass
        else:
            nums = []
            for j in range(5):
                for k in str(i+j * spacing):
                    nums.append(int(k))
            allThere = True
            for j in range(10):
                if j not in nums:
                    allThere = False
                    break
            if allThere:
                print("")
                for j in range(5):
                    print(str(j * spacing + i) + "\t", end = "")