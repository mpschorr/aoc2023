import sys
import math
from datetime import datetime

COLORS = ("red", "green", "blue")

# Compares 2 lists and returns a list of the max values for each index
def grab_max(prev: list[int], next: list[int]) -> list[int]:
  maxed = [0,0,0]
  for i,val_p in enumerate(prev):
    val_n = next[i]
    maxed[i] = max(val_p, val_n)
  return maxed

# Returns a list of [red, green, blue] for the string representing it
def parse_grab(grab_str: str) -> list[int]:
  split_comma = grab_str.split(", ")
  groups = [0,0,0]
  for group_str in split_comma:
    split_space = group_str.split()
    amount = int(split_space[0])
    group = split_space[1]
    group_index = COLORS.index(group)
    groups[group_index] = amount
  return groups

# Returns the game number & maximum for each color
def parse_line(line: str) -> (int, list[int]):
  split_col = line.split(": ")
  game_id = int(split_col[0].split(" ")[1])
  grab_strs = split_col[1].split("; ")
  max_grab = [0,0,0]
  for grab_str in grab_strs:
    grab = parse_grab(grab_str)
    max_grab = grab_max(max_grab, grab)
    pass
  return (game_id, max_grab)

# Sees if a grab is possible given a comparison
def grab_possible(grab: list[int], comp: list[int]) -> bool:
  for i in range(3):
    if grab[i] > comp[i]:
      return False
  return True

# Part 1
def main_one(lines: list[str]) -> int:
  accumulator = 0
  for line in lines:
    line_data = parse_line(line)
    possible = grab_possible(line_data[1], [12, 13, 14])
    if possible:
      accumulator += line_data[0]
    # pass
  return accumulator

# Part 2
def main_two(lines: list[str]) -> int:
  accumulator = 0
  for line in lines:
    line_data = parse_line(line)
    power = math.prod(line_data[1])
    accumulator += power
  return accumulator

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
    print(out)
    print(f'Execution completed in {end-start}µs ({(end-start)/1000}ms)')