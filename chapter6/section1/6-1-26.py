n = 7 # must be odd
c = n // 2

def rot(p):
    x = p[0] - c
    y = p[1] - c
    return (-y + c, x + c)

ans = 0
cnt = set()

for x1 in range(n):
    for y1 in range(n):
        for x2 in range(n):
            for y2 in range(n):
                p1 = (x1, y1)
                p2 = (x2, y2)
                if p1 == p2: continue
                if (p1, p2) in cnt: continue
                
                ans += 1

                p1_, p2_ = p1, p2
                for r in range(4):
                    cnt.add((p1_,p2_))
                    cnt.add((p2_,p1_))
                    p1_ = rot(p1_)
                    p2_ = rot(p2_)

print(ans)