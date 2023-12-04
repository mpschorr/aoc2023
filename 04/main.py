import sys
from datetime import datetime

def parse_line(line: str) -> tuple[list[int],list[int]]:
  split_colon = line.split(": ")
  split_pipe = split_colon[1].split(" | ")
  numbers_holding = [int(n) for n in split_pipe[0].split()]
  numbers_winning = [int(n) for n in split_pipe[1].split()]
  return (numbers_holding,numbers_winning)

def find_intersections(a: list[int], b: list[int]) -> list[int]:
  return [i for i in a if i in b]

def calculate_points(intersections: list[int]) -> int:
  if len(intersections) == 0:
    return 0
  return 2 ** (len(intersections)-1)

def main_one(lines: list[str]) -> int:
  accumulator = 0
  for line in lines:
    line_data = parse_line(line)
    intersections = find_intersections(line_data[0], line_data[1])
    points = calculate_points(intersections)
    accumulator += points
  return accumulator

def main_two(lines: list[str]) -> int:
  total_cards = 0
  card_counts = [1] * len(lines)
  for line_i,line in enumerate(lines):
    line_data = parse_line(line)
    intersections = find_intersections(line_data[0], line_data[1])
    wins = len(intersections)
    card_count = card_counts[line_i]
    if wins > 0:
      for i in range(line_i+1, line_i+1+wins):
        card_counts[i] += card_count
    total_cards += wins * card_count + 1
  return total_cards

# Scaffolding
if __name__ == '__main__':
  filename = "in_test.txt"
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  with open(filename, 'r') as infile:
    lines = [line.strip() for line in infile.readlines()]
    
    start = datetime.now().microsecond
    # out = main_one(lines)
    out = main_two(lines)
    end = datetime.now().microsecond
    print(f'Function result: {out}')
    print(f'Execution completed in {end-start}µs ({(end-start)/1000}ms)')