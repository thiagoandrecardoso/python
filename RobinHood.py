import math

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]


def hittingAnArrowWithAnotherArrowCoordinates():
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i] == points[j]:
                print(points[i])


def howManyArrowsHaveFallenInEachQuadrant():
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0

    for point in points:
        if point[0] > 0 and point[1] > 0:
            Q1 += 1
        if point[0] < 0 < point[1]:
            Q2 += 1
        if point[0] < 0 and point[1] < 0:
            Q3 += 1
        if point[0] > 0 > point[1]:
            Q4 += 1
    quadrants = [Q1, Q2, Q3, Q4]
    print(quadrants)


def distanceToTheCenter(point):
    return math.sqrt(((point[0] - 0) * (point[0] - 0)) + ((point[1] - 0) * (point[1] - 0)))


def findPointClosestToTheCenter():
    distance = distanceToTheCenter(points[0])
    pointClosest = []
    for i in range(1, len(points)):
        if distanceToTheCenter(points[i]) <= distance:
            distance = distanceToTheCenter(points[i])
            pointClosest.append(points[i])
    print(distance)
    print(pointClosest)


def numberArrowWontHitTheTarget():
    radius = 9
    numberWontArrow = 0
    for point in points:
        if distanceToTheCenter(point) > radius:
            numberWontArrow += 1
    return numberWontArrow
