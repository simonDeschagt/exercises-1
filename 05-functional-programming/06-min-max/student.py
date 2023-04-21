def closest(points, target_point):
    def distance(point):
        x,y = point
        dx =x-tx
        dy = y-ty
        distance = dx**2 + dy**2
        return distance
    tx,ty = target_point
    return min(points, key=distance)


