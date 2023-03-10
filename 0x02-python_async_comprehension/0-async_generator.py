#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module."""
import random
import asyncio
from typing import List


async def async_generator() -> List[float]:
    """ yield a random number between 0 and 10
    and asynchronously wait for 1seconds"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
