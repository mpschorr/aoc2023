import sys
from datetime import datetime

# type Grid = list[list[str]]

def construct_grid(lines: list[str]) -> list[list[str]]:
  grid = []
  for line in lines:
    grid.append([char for char in line])
  return grid

def get_number_groups(grid: list[list[str]]) -> list[tuple[int,int,int]]:
  groups = []
  for row,row_a in enumerate(grid):
    last_was_digit = False
    length = 0
    for col,char in enumerate(row_a):
      if char.isdigit():
        length += 1
      if last_was_digit and not char.isdigit():
        groups.append((col-length, row, length))
        length = 0
      last_was_digit = char.isdigit()
    if last_was_digit:
      groups.append((len(grid[0])-length, row, length))
  return groups

def get_number_from_group(grid: list[list[str]], group: (int,int,int)) -> int:
  x, y, length = group
  num = 0
  for i in range(length):
    digit = int(grid[y][x + i])
    num += digit * 10**(length-i-1)
  return num

def get_neighbor_bounds_of_group(grid: list[list[str]], group: (int,int,int)) -> tuple[tuple[int,int],tuple[int,int]]:
  cols = len(grid[0])
  rows = len(grid)
  x, y, length = group
  x_min = max(x - 1, 0)
  x_max = min(x + length + 1, cols)
  y_min = max(y - 1, 0)
  y_max = min(y + 1, rows - 1)
  return ((x_min,y_min),(x_max,y_max))

def get_neighbors_from_bounds(grid: list[list[str]], bounds: tuple[tuple[int,int],tuple[int,int]]) -> list[list[str]]:
  neighbors: list[list[str]] = []
  x_min,y_min=bounds[0]
  x_max,y_max=bounds[1]
  for y in range(y_min, y_max+1):
    row = grid[y][x_min:x_max]
    neighbors.append(row)
  return neighbors

def get_neighbor_symbol_coords(neighbors: list[list[str]]) -> list[tuple[int,int]]:
  neighbor_symbols: list[tuple[int,int]] = []
  for row,row_v in enumerate(neighbors):
    for col,col_v in enumerate(row_v):
      if not (col_v.isdigit() or col_v == '.'):
        # return True
        neighbor_symbols.append((col, row))
  return neighbor_symbols

def main_one(lines: list[str]) -> int:
  grid = construct_grid(lines)
  groups = get_number_groups(grid)
  accumulator = 0

  for group in groups:
    number = get_number_from_group(grid, group)
    bounds = get_neighbor_bounds_of_group(grid, group)
    neighbors = get_neighbors_from_bounds(grid, bounds)
    neighbor_symbols = get_neighbor_symbol_coords(neighbors)
    if len(neighbor_symbols) > 0:
      accumulator += number

  return accumulator

def main_two(lines: list[str]) -> int:
  grid = construct_grid(lines)
  groups = get_number_groups(grid)

  gears = {}
  for group in groups:
    number = get_number_from_group(grid, group)
    bounds = get_neighbor_bounds_of_group(grid, group)
    neighbors = get_neighbors_from_bounds(grid, bounds)
    neighbor_symbol_coords = get_neighbor_symbol_coords(neighbors)
    for neighbor_coord in neighbor_symbol_coords:
      x = neighbor_coord[0] + bounds[0][0]
      y = neighbor_coord[1] + bounds[0][1]
      coord = (x,y)
      symbol = grid[y][x]
      if symbol == '*':
        if coord not in gears:
          gears[coord] = [group]
        else:
          gears[coord].append(group)

  accumulator = 0
  for index,(gear_coord,number_coords) in enumerate(gears.items()):
    if len(number_coords) == 2:
      group_a = number_coords[0]
      group_b = number_coords[1]
      num_a = get_number_from_group(grid, group_a)
      num_b = get_number_from_group(grid, group_b)
      accumulator += num_a * num_b

  # print(gears)

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
    print(f'Function result: {out}')
    print(f'Execution completed in {end-start}µs ({(end-start)/1000}ms)')