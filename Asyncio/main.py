import asyncio


async def task1():
    print("starting task 1")
    await asyncio.sleep(5)
    data = {"data": "data frm task 1"}
    print(data)
    return data


async def task2():
    print("starting task 2")
    await asyncio.sleep(1)
    data = {"data": "data frm task 2"}
    print(data)
    return data


async def main():
    print("this is the start of the program")
    print("will be performing two task ")

    # creating objects of the co-routine
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())

    #
    await x
    await y
    print("tasks triggered")

# starts an event loop
asyncio.run(main())
