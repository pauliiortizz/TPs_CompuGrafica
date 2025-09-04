def bresenham_line(x0, y0, x1, y1):
    points = []
    deltaX = abs(x1 - x0)
    deltaY = abs(y1 - y0)
    stepX = 1 if x0 < x1 else -1 # bool ? 1 : -1
    stepY = 1 if y0 < y1 else -1
    err = deltaX - deltaY

    while True:
        if x0 == x1 and y0 == y1:
            points.append((x0, y0))
            break
        points.append((x0, y0))
        e2 = 2 * err
        if e2 > -deltaY:
            err -= deltaY
            x0 += stepX
        if e2 < deltaX:
            err += deltaX
            y0 += stepY
        points.append((x0, y0))
    return points