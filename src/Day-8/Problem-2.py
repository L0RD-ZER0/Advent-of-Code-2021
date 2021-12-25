class SevenSegmentDisplay:
    """
     1111
    2    3
    2    3
     4444
    5    6
    5    6
     7777

    len-2: 1
    len-3: 7
    len-4: 4
    len-5: 2, 3, 5
    len-6: 0, 6, 9
    len-7: 8
    """

    __slots__ = ['_input', '_output', '_segments', '_digits']

    def __init__(self, input_string: str):
        codes, out = input_string.split("|")
        codes, out = codes.strip().split(), out.strip().split()
        self._input: dict[int, list[set]] = {  }
        for code in codes:
            if len(code) not in self._input:
                self._input[len(code)] = []
            self._input[len(code)].append(set(code))
        self._output: list[set] = [ set(out_code) for out_code in out ]
        self._segments: dict[int, set] = {}
        self._digits: dict[int, set] = { i: set() for i in range(1, 10) }
        self._decode_segments()
        self._prepare_digits()
    
    def _decode_segments(self):
        segs_1_4_7 = set.intersection( *self._input[5] )
        self._segments[1] = segs_1_4_7.intersection( self._input[3][0] )
        self._segments[4] = segs_1_4_7.intersection( self._input[4][0] )
        self._segments[7] = segs_1_4_7.difference( self._segments[1] | self._segments[4] )
        self._segments[2] = self._input[4][0] - self._segments[4] - self._input[2][0]
        segs_1_2_6_7 = set.intersection( *self._input[6] )
        self._segments[6] = segs_1_2_6_7 - self._segments[1] - self._segments[2] - self._segments[7]
        self._segments[3] = self._input[2][0] - self._segments[6]
        self._segments[5] = self._input[7][0] - set.union( *self._segments.values() )
    
    def _prepare_digits(self):
        s = self._segments
        self._digits[0] = s[1] | s[2] | s[3] | s[5] | s[6] | s[7]
        self._digits[1] = s[3] | s[6]
        self._digits[2] = s[1] | s[3] | s[4] | s[5] | s[7]
        self._digits[3] = s[1] | s[3] | s[4] | s[6] | s[7]
        self._digits[4] = s[2] | s[3] | s[4] | s[6]
        self._digits[5] = s[1] | s[2] | s[4] | s[6] | s[7]
        self._digits[6] = s[1] | s[2] | s[4] | s[5] | s[6] | s[7]
        self._digits[7] = s[1] | s[3] | s[6]
        self._digits[8] = s[1] | s[2] | s[3] | s[4] | s[5] | s[6] | s[7]
        self._digits[9] = s[1] | s[2] | s[3] | s[4] | s[6] | s[7]

    def fetch_digit(self, digit: int) -> set:
        return self._digits.get(digit, set())
    
    def fetch_segment(self, segment: str) -> set:
        return self._segments.get(segment, set())
    
    def match_digit(self, digit_code: set) -> int:
        for digit, code in self._digits.items():
            if code == digit_code:
                return digit
        return -1
    
    def get_output(self) -> int:
        result = 0
        for digit in self._output:
            result = result*10 + self.match_digit(digit)
        return result

def preprocess(raw_data: str) -> list[SevenSegmentDisplay]:
    return [ SevenSegmentDisplay(line) for line in raw_data.split('\n') if line != '' ]

def process(data: list[SevenSegmentDisplay]) -> int:
    result = 0
    for display in data:
        result = result + display.get_output()
    print(f"Result: {result}")
    return result

def main():
    with open('.\\Input-1.txt', 'r') as f:
        raw_data = f.read()
    process( preprocess(raw_data) )

if __name__ == "__main__":
    main()
