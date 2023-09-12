"""
Create Custom exceptions (raise...from)
"""


class CustomException(Exception):

    def __str__(self):
        return "My custom exception"
