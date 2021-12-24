def _mean(pos_map: dict[int, int]) -> int:
    return int(sum([ pos*num for pos, num in pos_map.items()]) / sum(pos_map.values()))

def calc_path_cost(length: int) -> int:
    return (length * (length + 1)) // 2

def preprocess(raw_data: str) -> dict[int]:
    positions = {}
    for pos in raw_data.split(','):
        positions[int(pos)] = positions.get(int(pos), 0) + 1
    return positions

def process(pos_map: dict[int, int]) -> int:
    mean = _mean(pos_map)
    print(f"Mean: {mean}")
    result = 0
    for pos in pos_map:
        result = result + (calc_path_cost(abs(pos - mean)) * pos_map[pos])
    print(f"Result: {result}")
    return result

def main():
    with open(".\\Input-1.txt", "r") as f:
        raw_data = f.read()
    process( preprocess(raw_data) )

if __name__ == '__main__':
    main()
