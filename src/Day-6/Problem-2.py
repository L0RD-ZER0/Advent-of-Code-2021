def _tick(pond: dict[int, int]):
    reset_cycle = 0
    for period in pond:
        if period == 0:
            reset_cycle = pond[period]
        else:
            pond[period - 1] = pond[period]
    pond[8] = reset_cycle
    pond[6] += reset_cycle

def preprocess(raw_data: str) -> dict[int, int]:
    pond = { i: 0 for i in range(9) }
    for days in raw_data.split(','):
        pond[int(days)] = pond.get(int(days), 0) + 1
    return pond

def process(pond: dict[int, int], *, days = 256) -> int:
    for _ in range(days):
        print(_)
        _tick(pond)
    result = sum(pond.values())
    print(f"Number of Fishes: {result}")
    return result

def main():
    with open('.\\Input-1.txt', 'r') as f:
        raw_data = f.read()
    process( preprocess(raw_data) )

if __name__ == '__main__':
    main()
