def _median(pos_map: dict[int, int]) -> int:
    median_loc = sum(pos_map.values()) // 2
    items = 0
    for pos in sorted(pos_map.keys()):
        items += pos_map[pos]
        if items >= median_loc:
            return pos

def preprocess(raw_data: str) -> dict[int]:
    positions = {}
    for pos in raw_data.split(','):
        positions[int(pos)] = positions.get(int(pos), 0) + 1
    return positions

def process(pos_map: dict[int, int]) -> int:
    median = _median(pos_map)
    result = 0
    for pos in pos_map:
        result = result + (abs(pos - median) * pos_map[pos])
    print(f"Result: {result}")
    return result

def main():
    with open(".\\Input-1.txt", "r") as f:
        raw_data = f.read()
    process( preprocess(raw_data) )

if __name__ == '__main__':
    main()
