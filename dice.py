#!/usr/bin/env python3


def roll(n: int = 1, sides: int = 6):
  """
  Rolls n dice with sides.
  """
  return sum(map(lambda x: x * n, range(1, sides + 1)))


def main():
  """
  Main program.
  """
  print(roll())
  print(roll(3))
  print(roll(3, 6))


if __name__ == '__main__':
  main()
