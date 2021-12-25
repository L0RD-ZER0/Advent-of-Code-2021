def _valid(data: str):
    return len(data) in (2, 4, 3, 7)
        
def preprocess(raw_data: str) -> list[list[str]]:
    return [ line.split(" | ")[1].split() for line in raw_data.split('\n') if line != '' ]

def process(data: list[list[str]]) -> int:
    result = 0
    for digits in data:
        result = result + len(tuple(filter(_valid, digits)))
    print(f"Number of Repetitions of Digits (1,4,7,8): {result}")
    return result

def main():
    with open('.\\Input-1.txt', 'r') as f:
        raw_data = f.read()
    process( preprocess(raw_data) )

if __name__ == '__main__':
    main()
    