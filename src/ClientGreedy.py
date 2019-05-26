from src.World import *


def get_action(world: World):
    head_pos = world.get_self().get_head()
    next_head = []
    next_head.append(head_pos + Vector2D(1, 0))
    next_head.append(head_pos + Vector2D(0, 1))
    next_head.append(head_pos + Vector2D(-1, 0))
    next_head.append(head_pos + Vector2D(0, -1))

    min_dist = 1000
    h_best = -1
    for h in range(4):
        dist = next_head[h].dist(world.goal_position)
        if dist < min_dist:
            min_dist = dist
            h_best = h

    print(h_best)

    actions = ['d', 'r', 'u', 'l']
    if h_best > 0:
        return actions[h_best]
    return actions[0]
