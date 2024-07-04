# In Python, the `async` and `await` keywords are used to create asynchronous functions. An asynchronous function is a function that can run in the background while other code is running.

# Think of it like this: imagine you're cooking a meal and you need to boil some water. You put the water on the stove and wait for it to boil. But instead of just standing there waiting for the water to boil, you start chopping vegetables or doing some other task. When the water is finally boiling, you come back to it and continue with the recipe.

# In Python, an asynchronous function is like the water boiling in the background. You can start it running and then do other things while it's running. When it's finished, you can come back to it and get the result.

# The `async` keyword is used to define an asynchronous function. It's like saying "Hey, I'm going to start boiling some water now, but I'll come back to it later".

# The `await` keyword is used to wait for the result of an asynchronous function. It's like saying "Okay, I'm done chopping vegetables, now I need to check if the water is boiling yet". If the water is boiling, you can use the result (e.g. pour it into a pot). If it's not boiling yet, you can keep doing other things until it is.

# Here's an example:
# ```
# async def boil_water():
#     # simulate boiling water
#     print("Boiling water...")
#     time.sleep(5)
#     print("Water is boiling!")

# async def chop_veggies():
#     # simulate chopping veggies
#     print("Chopping veggies...")
#     time.sleep(2)
#     print("Veggies are chopped!")

# async def cook_meal():
#     # start boiling water
#     await boil_water()
#     # chop veggies while water is boiling
#     await chop_veggies()
#     # use the boiled water and chopped veggies to cook the meal
#     print("Meal is cooked!")

# # start cooking the meal
# cook_meal()
# ```
# In this example, the `boil_water()` function is an asynchronous function that simulates boiling water. The `chop_veggies()` function is another asynchronous function that simulates chopping veggies. The `cook_meal()` function starts the `boil_water()` function and then does some other task (chopping veggies) while the water is boiling. When the water is finally boiling, it uses the result (the boiled water) to cook the meal.

# I hope this helps! Let me know if you have any questions.


# Here is an example of using the `asyncio` module to create a simple asynchronous program:
# ```
# import asyncio

# async def greet(name):
#     print(f"Hello, {name}!")

# async def main():
#     # Create a task to run the greet function
#     task = asyncio.create_task(greet("John"))

#     # Run the task and wait for it to complete
#     await task

# asyncio.run(main())
# ```
# This code defines two coroutines: `greet` and `main`. The `greet` coroutine takes a name as an argument and prints a greeting message. The `main` coroutine creates a task to run the `greet` coroutine with the name "John" and waits for the task to complete.

# The `asyncio.run()` function is used to run the `main` coroutine and start the event loop. This will execute the `greet` coroutine and print the greeting message.

# Note that this is a very simple example, but it demonstrates the basic idea of creating and running coroutines using the `asyncio` module.

# You can also use `asyncio.gather()` to run multiple tasks concurrently:

# This code creates two tasks to run the `greet` coroutine with different names, and uses `asyncio.gather()` to run them concurrently. This will print both greeting messages simultaneously.

# I hope this helps! Let me know if you have any questions or need further examples.

# Execute -> python3 /Users/ntnmathur/github/ai_engineer/asyncio_example.py
import asyncio
async def greet(name):
    print(f"Hello, {name}!")
async def main():
    tasks = [asyncio.create_task(greet("John")), asyncio.create_task(greet("Jane"))]
    await asyncio.gather(*tasks)
asyncio.run(main())

