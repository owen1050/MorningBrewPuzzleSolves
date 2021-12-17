#https://ci3.googleusercontent.com/proxy/mSn5iVt4tWi5ZhHpsf8o45sL1XGTE48UgKepiW9R5OjqKORaE1EdxhTOre3wYuGzqrN5rYXfMu0MzF0IrkRiVUR-EcA6Jca-kR6qsrTqsyjdHm2tDmmRkmww7Dl0TU3j_qN8jacOB05OYKHEewboc3UsWmVOSkssRRQhdLGQqg4tCdkYrhh2bOxBuNcRUPGaRjcguQsp8-KXkSnQd3dddlWQn9mrAA_vUw=s0-d-e1-ft#https://dlp31coh2a67q.cloudfront.net/eyJrZXkiOiJ1cGxvYWRzL21lZGl1bS9hc3NldC83MzM0L3NlbmRfbW9yZV9tb25leS5wbmciLCJidWNrZXQiOiJvc2xvLXByb2R1Y3Rpb24ifQ==

sols = []

for p in range(9):
    m = p + 1
    print(m)
    for s in range(10):
        for e in range(10):
            for n in range(10):
                for d in range(10):
                    for o in range(10):
                        for r in range(10):
                            for y in range(10):
                                x = d + 10 * n + 100 * e + 1000 * s
                                q = 1000 * m + 100 * o + 10 * r + e
                                w = y + 10 * e + 100 * n + 1000 * o + 10000 * m
                                if (x + q== w):
                                    sols.append([s,e,n,d,m,o,r,y, x, q, w])
for sol in sols:
    print("SEND + MORE = " + str(sol[8]) + " + " + str(sol[9]) + " = " + str(sol[10]) + " = MONEY")


