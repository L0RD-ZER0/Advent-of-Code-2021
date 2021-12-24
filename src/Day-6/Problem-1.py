class LanternFish:

    __slots__ = 'counter', 'pond'

    def __init__(self, counter, pond):
        self.counter = counter
        self.pond = pond
    
    def tick(self, *, days: int = 1):
        self.counter = self.counter - days
        while self.counter < 0:
            self.counter = self.counter + 7
            self.pond.append(LanternFish(7 + 2 - days, self.pond))
    
    def __repr__(self) -> str:
        return f"<LanternFish: {self.counter}>"

def _tick(pond: list[LanternFish],*, days: int = 1):
    for fish in range(len(pond)):
        pond[fish].tick(days=days)

def preprocess(raw_data: str) -> list[LanternFish]:
    pond = []
    for days in raw_data.split(','):
        pond.append(LanternFish(int(days), pond))
    return pond

def process(pond: list[LanternFish], *, days = 80) -> int:
    for _ in range(days):
        _tick(pond)
    result = len(pond)
    print(f"Number of Fishes: {result}")
    return result

def main():
    with open('.\\Input-1.txt', 'r') as f:
        raw_data = f.read()

    process( preprocess(raw_data) )

if __name__ == '__main__':
    main()
