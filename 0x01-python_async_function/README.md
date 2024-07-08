# Asynchronous Programming with Python asyncio

This repository contains Python scripts that demonstrate the use of asyncio for asynchronous programming. It includes functions to create and manage asyncio tasks, measure runtime, and handle concurrent coroutines.

## Introduction

Asynchronous programming is a programming paradigm that allows tasks to run concurrently and independently, improving the efficiency of applications that perform I/O-bound operations. Python's `asyncio` module provides support for asynchronous programming and allows the creation of coroutines and tasks.

This repository includes several Python scripts that demonstrate the use of asyncio:

- `0-basic_async_syntax.py`: Defines a coroutine `wait_random` that waits for a random delay and returns it.
- `1-concurrent_coroutines.py`: Implements `wait_n`, which runs multiple instances of `wait_random` concurrently using asyncio.
- `2-measure_runtime.py`: Measures the runtime of `wait_n` and calculates average execution time.
- `3-tasks.py`: Defines `task_wait_random` to create asyncio tasks from regular functions.
- `4-tasks.py`: Implements `task_wait_n`, which uses `task_wait_random` to run concurrent coroutines.

## Setup

To run the scripts in this repository, make sure you have Python 3.7+ installed along with the necessary dependencies:

```bash
pip install asyncio
