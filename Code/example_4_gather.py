import asyncio


async def division(num: int, div: int) -> float:
    print(f'Worker started with {num}')
    await asyncio.sleep(0.5)
    return num / div


async def worker_gather():
    res = await asyncio.gather(
        division(10, 5),
        division(100, 51),
        division(10501, 70),
        division(90, 30),
        division(150, 3),
    )
    print(res)

asyncio.run(worker_gather())

# loop = asyncio.get_event_loop()
# tasks = [loop.create_task(worker_gather())]
# task_list = asyncio.wait(tasks)
# loop.run_until_complete(task_list)
# loop.close()
