#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time
import datetime
import typing
import logging
import typing

# from async import *
from dice import *
from dynamic import *
#./game.py


def fib_iter_0(n: int = 0) -> typing.Iterator[int]:
  if n == 0:
    yield 0
  elif n == 1:
    yield 1
  else:
    yield 1
    for x in fib_iter_0(n - 1):
      yield x + 1


def fib_gen_1(n: int = 0) -> typing.Generator[int, None, None]:
  a, b = 0, 1
  while n > 0:
    yield a
    a, b = b, a + b
    n -= 1


def fib_gen_2(n: int = 0) -> typing.Generator[int, None, None]:
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b


def fib_generator(n: int = 0) -> typing.Generator[int, None, None]:
  if n == 0:
    yield 0
  elif n == 1:
    yield 1
  else:
    yield 1
    for x in fib_generator(n - 1):
      yield x + 1


def fib_generator_2(n: int = 0) -> typing.Generator[int, None, None]:
  if n == 0:
    yield 0
  elif n == 1:
    yield 1
  else:
    yield 1
    for x in fib_generator_2(n - 1):
      yield x + 1


def test_iter_fib():
  assert list(iter_fib(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def gen_range(end: int, start: int = 1, step: int = 1) -> typing.Iterator[int]:
  while start <= end:
    yield start
    start += step


def gen_range_step(end: int,
                   start: int = 1,
                   step: int = 1) -> typing.Iterator[int]:
  while start <= end:
    yield start
    start += step


def gen_range_step_reverse(end: int,
                           start: int = 1,
                           step: int = 1) -> typing.Iterator[int]:
  while start <= end:
    yield start
    start += step


def main():
  # print(list(gen_range(10)))

  # print(list(gen_range_step(10)))

  # test_iter_fib()
  # print(list(iter_fib(0)))
  # print(list(iter_fib(1)))
  # print(list(iter_fib(2)))
  # print(list(iter_fib(10)))
  # print(list(fib_gen_1(10)))
  print(roll())
  print(roll(50, 40))


if __name__ == '__main__':
  main()
