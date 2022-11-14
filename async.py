#!/usr/bin/env python3

import asyncio
import time


@asyncio.coroutine
def task():
  print('task started')
  yield from asyncio.sleep(1)
  print('task finished')


async def async_task():
  print('async task started')
  yield from asyncio.sleep(1)
  print('async task finished')


def main():
  loop = asyncio.get_event_loop()
  loop.run_until_complete(task())
  loop.run_until_complete(async_task())
  loop.close()


if __name__ == '__main__':
  main()
