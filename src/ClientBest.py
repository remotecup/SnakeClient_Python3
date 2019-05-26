from src.World import *


def get_action(world: World):
    head_pos = world.get_self().get_head()
    next_head = []
    next_head.append(head_pos + Vector2D(1, 0))
    next_head.append(head_pos + Vector2D(0, 1))
    next_head.append(head_pos + Vector2D(-1, 0))
    next_head.append(head_pos + Vector2D(0, -1))
    next_head_ok = [True, True, True, True]

    h_number = 0
    for h in next_head:
        accident = False
        for s in world.snakes:
            if h in world.snakes[s].get_body():
                accident = True
                break
        if accident:
            print(h, 'snake')
        if h in world.get_walls():
            accident = True
            print(h, 'wall')
        if accident:
            next_head_ok[h_number] = False
        h_number += 1

    print(next_head)
    print(next_head_ok)
    min_dist = 1000
    h_best = -1
    for h in range(4):
        if not next_head_ok[h]:
            continue
        dist = next_head[h].dist(world.goal_position)
        if dist < min_dist:
            min_dist = dist
            h_best = h

    print(h_best)

    actions = ['d', 'r', 'u', 'l']
    if h_best > 0:
        return actions[h_best]
    return actions[0]
