import itertools as it
import pprint
import math
import sys
import math
import itertools

n = int(input("enter number of persons"))
distance_p_list = []
dis = []
if (n >= 2 and n <= 16) and (n % 2 == 0):

    print('Enter x coordinate and y coordinate /n')
    for person in range(0, n):
        x = sys.stdin.readline().strip()  # strip removes the \n
        y = sys.stdin.readline().strip()

        myTuple = tuple([int(x), int(y)])
        print(myTuple)
        dis.append(myTuple)


def distance_points(dis):
    for p in two_point_list:
        px1 = p[0][0]
        px2 = p[1][0]
        py1 = p[0][1]
        py2 = p[1][1]

        distance = ((px1 - px2) ** 2 + (py1 - py2) ** 2) ** 0.5
        distance_p_list.append((distance, p))

    return distance_p_list


two_point_list = list(it.combinations(dis, 2))
print("Non-repeating point combinations:")
pprint.pprint(two_point_list)
print('-' * 40)
distance_p_list = distance_points(two_point_list)
print("List of (distance, (point1, point2)) tuples:")
pprint.pprint(distance_p_list)
print('-' * 40)
shortest_distance = min(distance_p_list)
print(shortest_distance, "value")
# show result
sf = "The shortest distance is {:f} between points {}"
print(sf.format(shortest_distance[0], shortest_distance[1]))

l = distance_p_list
tl = two_point_list

print distance_p_list[5][1][0], "5 th index"
print shortest_distance[1][0], "shortest distance"
if shortest_distance[1][0] == distance_p_list[5][1][0] or shortest_distance[1][1] == distance_p_list[5][1][0]:
    print("saved")
