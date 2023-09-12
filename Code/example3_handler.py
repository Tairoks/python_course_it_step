"""
try-except explanation
"""

# try:
#     with open('test.txt', "r") as file:
#         nums = file.readlines()
#         for n in nums:
#             print(int(n.strip()))
# except FileNotFoundError as error:
#     print(f"An error occurred: FileNotFoundError -> {error}")
# except ValueError as error:
#     print(f"An error occurred: ValueError -> {error}")
# finally:
#     print("End program")


try:
    with open('test.tx', "r") as file:
        nums = file.readlines()
        for n in nums:
            print(int(n.strip()))
except (FileNotFoundError, ValueError) as error:
    print(f"A common error occurred -> {error}")
finally:
    print("End program")

