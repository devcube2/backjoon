def solution(dirs):    
    visited = set()
    (x, y) = 5, 5
    for d in dirs:        
        (org_x, org_y) = (x, y)
        if d == "U":
            if y == 0:
                continue
            y -= 1
        elif d == "D":
            if y == 10:
                continue
            y += 1
        elif d == "R":
            if x == 10:
                continue
            x += 1
        elif d == "L":
            if x == 0:
                continue
            x -= 1
        visited.add((org_x, org_y, x, y))
        visited.add((x, y, org_x, org_y))        
    return len(visited)//2