import sys

DIGIT_WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
WINDOW_SIZE = max([len(word) for word in DIGIT_WORDS])

def convert_digit_words(input_line: str) -> str:
    converted = ""
    ptr_left = 0
    ptr_right = WINDOW_SIZE
    while ptr_left < len(input_line):
        window = input_line[ptr_left:ptr_right]
        for word in DIGIT_WORDS:
            if window.startswith(word):
                converted += str(DIGIT_WORDS.index(word) + 1)
                ptr_left += len(word)-2
                ptr_right = ptr_left + WINDOW_SIZE
                break
        else:
            converted += window[0]
        ptr_left += 1
        ptr_right += 1
        pass
    return converted


def main_one(lines: list[str]):
    total = 0
    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]
        calibration_number = (digits[0] * 10) + digits[-1]
        total += calibration_number
    return total

def main_two(lines: list[str]):
    total = 0
    for line in lines:
        converted = convert_digit_words(line)
        digits = [int(c) for c in converted if c.isdigit()]
        calibration_number = (digits[0] * 10) + digits[-1]
        total += calibration_number
    return total

# Scaffolding
if __name__ == '__main__':
    filename = "in_test.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename, 'r') as infile:
        lines = [line.strip() for line in infile.readlines()]
        # out = main_one(lines)
        out = main_two(lines)
        print(out)