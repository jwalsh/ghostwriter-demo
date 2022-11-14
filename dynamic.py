#!/usr/bin/env python


def fib(n: int) -> int:
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)


def ways_to_climb_stairs(n: int) -> int:
  """
  Returns the number of ways to climb n stairs.

  There are n stairs, a person standing at the bottom wants to reach the top. The
  person can climb either 1 stair or 2 stairs at a time. Count the number of ways,
  the person can reach the top.
  """
  # n is a positive integer
  if n == 1:
    return 1
  if n == 2:
    return 2


def ways_to_climb_stairs_1(n: int) -> int:
  """
  Returns the number of ways to climb n stairs.
  """
  return fib(n + 1)
