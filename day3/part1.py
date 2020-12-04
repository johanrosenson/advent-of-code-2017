# https://adventofcode.com/2017/day/3

square = int(open('input').read())

squares = {}

bounds = {'x': [0, 1], 'y': [0, 0]}
current= {'x': 0, 'y': 0}

axis = 'x'
direction = 1

for n in range(1, square+1):
    # store square at current position
    squares[n] = current.copy()

    if current[axis] == bounds[axis][(0, 1)[direction == 1]]:
        # change direction, then axis
        direction = (-1, 1)[(axis == 'x' and direction == 1) or (axis == 'y' and direction == -1)]
        axis = ('y', 'x')[axis == 'y']
        # expand bounds
        bounds[axis][(0, 1)[direction == 1]] += direction

    # move current position
    current[axis] += direction

distance = abs(squares[square]['x']) + abs(squares[square]['y'])
print('distance {}'.format(distance))
