import math
import random
import numpy as np
import matplotlib.pyplot as plt


class Tiger:
    def __init__(self, minimal, maximal):
        self.minimal = minimal
        self.maximal = maximal
        self.r = 10
        self.n = 10

    def rotate_triangle(self, point, angle, touching_point):
        sinus, cosinus = np.sin(angle), np.cos(angle)
        point = (point[0] - touching_point[0], point[1] - touching_point[1])
        x_new = point[0] * cosinus - point[1] * sinus
        y_new = point[0] * sinus + point[1] * cosinus
        point = (x_new + touching_point[0], y_new + touching_point[1])
        return point
    def tigers_generator(self):
        points = []
        for _ in range(20):
            x = random.uniform(self.minimal, self.maximal)
            y = random.uniform(self.minimal, self.maximal)
            points.append((x, y))
        return points

    def circle_points_generator(self, tiger_centers):
        par = random.uniform(0, 2 * math.pi)
        rot = 2 * math.pi/self.n
        a = []
        for point in tiger_centers:
            for k in range(self.n):
                x = self.r * math.cos(par + k * rot) + point[0]
                y = self.r * math.sin(par + k * rot) + point[1]
                a.append((x, y))
        return a

    def tiger_points_generator(self, tiger_centers):
        a = random.uniform(0, 5)
        b = 2
        outcome = []
        polygon = []
        alfa = random.uniform(0, 2 * np.pi)
        beta = random.uniform(0, np.pi/6)
        gamma = random.uniform(0, np.pi/4)
        polygon.append((point[0], point[1]))
        polygon.append((point[0] + a, point[1] + a))
        polygon.append((point[0] - a, point[1] + a))
        rotating = self.rotate_triangle((point[0] + b * np.cos(0), point[1] + b * np.tan((2 * np.pi - beta - 2 * gamma - np.pi/2)/8)), -gamma, point)
        polygon.append(rotating)
        rotating = self.rotate_triangle(
            (point[0] - b * np.cos(0), point[1] + b * np.tan((2 * np.pi - beta - 2 * gamma - np.pi / 2) / 8)), gamma,
            point)
        polygon.append(rotating)
        rotating = self.rotate_triangle(
            (point[0] + b * np.cos(0), point[1] - b * np.tan((2 * np.pi - beta - 2 * gamma - np.pi / 2) / 8)), -gamma,
            point)
        polygon.append(rotating)
        rotating = self.rotate_triangle(
            (point[0] - b * np.cos(0), point[1] - b * np.tan((2 * np.pi - beta - 2 * gamma - np.pi / 2) / 8)), gamma,
            point)
        polygon.append(rotating)

        for pnt in polygon:
                buf = (pnt[0]*np.cos(alfa) - pnt[1]*np.sin(alfa), pnt[0]*np.sin(alfa) + pnt[1]*np.cos(alfa))
                outcome.append(buf)
        #(360-beta - 2gamma - 90)/4

        return outcome



def calculate_angle(p_0, p_1, p_2):
    p_1p_0 = [p_0[0] - p_1[0], p_0[1] - p_1[1]]
    p_1p_2 = [p_2[0] - p_1[0], p_2[1] - p_1[1]]

    scalar = p_1p_0[0] * p_1p_2[0] + p_1p_0[1] * p_1p_2[1]

    l1 = math.sqrt(p_1p_0[0] ** 2 + p_1p_0[1] ** 2)
    l2 = math.sqrt(p_1p_2[0] ** 2 + p_1p_2[1] ** 2)

    if l1 * l2 == 0:
        return -math.inf

    cos = scalar / (l1 * l2)

    if cos > 1:
        cos = 1
    elif cos < -1:
        cos = -1

    return math.degrees(math.acos(cos))


tiger_count = 20
vertexes = 5
tigers = Tiger(0, 100)
tigerro = []
tigerpoints = tigers.tigers_generator()
for point in tigerpoints:
    polygon = tigers.tiger_points_generator(tigerpoints)
    tiger_x = []
    tiger_y = []
    for points in polygon:
        plt.scatter(points[0], points[1])
    for i in range(1, 7):
        tigerro.append(polygon[i])

    tiger_x = []
    tiger_y = []

    tiger_x.append(polygon[0][0])
    tiger_y.append(polygon[0][1])
    tiger_x.append(polygon[1][0])
    tiger_y.append(polygon[1][1])
    tiger_x.append(polygon[2][0])
    tiger_y.append(polygon[2][1])
    tiger_x.append(polygon[0][0])
    tiger_y.append(polygon[0][1])
    plt.plot(tiger_x, tiger_y)

    tiger_x = []
    tiger_y = []

    tiger_x.append(polygon[0][0])
    tiger_y.append(polygon[0][1])
    tiger_x.append(polygon[3][0])
    tiger_y.append(polygon[3][1])
    tiger_x.append(polygon[5][0])
    tiger_y.append(polygon[5][1])
    tiger_x.append(polygon[0][0])
    tiger_y.append(polygon[0][1])
    plt.plot(tiger_x, tiger_y)

    tiger_x = []
    tiger_y = []

    tiger_x.append(polygon[0][0])
    tiger_y.append(polygon[0][1])
    tiger_x.append(polygon[4][0])
    tiger_y.append(polygon[4][1])
    tiger_x.append(polygon[6][0])
    tiger_y.append(polygon[6][1])
    tiger_x.append(polygon[0][0])
    tiger_y.append(polygon[0][1])
    plt.plot(tiger_x, tiger_y)

#tigerro = tigers.circle_points_generator(tigerpoints)
p1 = tigerro[0]

for i in range(120):
    if tigerro[i][1] < p1[1]:
        p1 = tigerro[i]
    elif tigerro[i][1] == p1[1]:
        if tigerro[i][0] < p1[0]:
            p1 = tigerro[i]

p0 = (-10000, p1[1])
n = (math.inf, math.inf)

hull = [p0, p1]
i = 1

while n != p1:
    angle = -math.inf
    pi = (0, 0)
    for point in tigerro:
        if calculate_angle(hull[i-1], hull[i], point) > angle:
            angle = calculate_angle(hull[i-1], hull[i], point)
            # print(hull[i - 1], hull[i], tigerro[f], angle)
            pi = point
    hull.append(pi)
    n = pi
    i += 1

hull.pop(0)

hull_x = [point[0] for point in hull]
hull_y = [point[1] for point in hull]
plt.plot(hull_x, hull_y)

plt.axis('equal')
plt.show()
