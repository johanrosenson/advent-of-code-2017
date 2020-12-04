# https://adventofcode.com/2017/day/3

square = int(open('input').read())

squares = {}
coord_map = {}

bounds = {'x': [0, 1], 'y': [0, 0]}
current= {'x': 0, 'y': 0}

axis = 'x'
direction = 1

def value(n, squares, coord_map):
    center = squares[n]['coord']

    # get all other squares
    adjacents = [
        {'x': center['x']-1, 'y': center['y']+1},
        {'x': center['x']-0, 'y': center['y']+1},
        {'x': center['x']+1, 'y': center['y']+1},
        {'x': center['x']-1, 'y': center['y']-0},
        {'x': center['x']+1, 'y': center['y']-0},
        {'x': center['x']-1, 'y': center['y']-1},
        {'x': center['x']-0, 'y': center['y']-1},
        {'x': center['x']+1, 'y': center['y']-1},
    ]

    value = 0
    for adjacent in adjacents:
        square = coord_map.get('{}x{}'.format(adjacent['x'], adjacent['y']))
        if square != None:
            value += squares[square]['value']

    return value

for n in range(1, square+1):
    # map coords to n
    coord_map['{}x{}'.format(current['x'], current['y'])] = n

    # store square at current position
    squares[n] = {
        'value': 1,
        'coord': current.copy(),
    }

    # update with adjacent values
    if n > 1:
        squares[n]['value'] = value(n, squares, coord_map)

    if squares[n]['value'] > square:
        print('{} is larger than input'.format(squares[n]['value']))
        exit()

    if current[axis] == bounds[axis][(0, 1)[direction == 1]]:
        # change direction, then axis
        direction = (-1, 1)[(axis == 'x' and direction == 1) or (axis == 'y' and direction == -1)]
        axis = ('y', 'x')[axis == 'y']
        # expand bounds
        bounds[axis][(0, 1)[direction == 1]] += direction

    # move current position
    current[axis] += direction
