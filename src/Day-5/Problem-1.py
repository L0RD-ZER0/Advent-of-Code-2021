def _range_to_points(point_1: tuple[int, int], point_2: tuple[int, int]) -> list[tuple[int, int]]:
    if point_1[0] == point_2[0]:
        return [ (point_1[0], i) for i in range(
            min(point_1[1], point_2[1]),
            max(point_1[1], point_2[1]) + 1
            ) ]
    elif point_1[1] == point_2[1]:
        return [ (i, point_1[1]) for i in range(
            min(point_1[0], point_2[0]),
            max(point_1[0], point_2[0]) + 1
            ) ]

def _string_to_range(raw_line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = raw_line.split("->")
    start, end = start.split(','), end.split(',')
    return tuple(map(int, start)), tuple(map(int, end))


def preprocess(raw_data: str) -> list[tuple[tuple[int, int]], list[tuple[int, int]]]:
    lines = raw_data.split('\n')
    data = []
    for line in lines:
        if line == '':
            continue
        rng = _string_to_range(line)
        if not ( rng[0][0] == rng[1][0] or rng[0][1] == rng[1][1] ):
            continue
        data.append(rng)
    return data

def process(ranges: list[tuple[tuple[int, int]], list[tuple[int, int]]]) -> int:
    board_map = {}
    for rng in ranges:
        for point in _range_to_points(rng[0], rng[1]):
            board_map[point] = board_map.get(point, 0) + 1
    intersections = sum(1 for amount in board_map.values() if amount > 1)
    print('Intersections:', intersections)
    return intersections


def main():
    with open(".\\Input-1.txt", "r") as f:
        inp = f.read()
    process( preprocess(inp) )

if __name__ == '__main__':
    main()
