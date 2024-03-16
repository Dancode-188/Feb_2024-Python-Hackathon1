# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
import time
import random
import colorama
from colorama import Fore, Style

colorama.init()

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n (int): The number of terms in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to n terms.
    """
    if n <= 1:
        return [0] if n == 0 else [0, 1]
    else:
        a, b = 0, 1
        sequence = [a, b]
        for _ in range(2, n):
            c = a + b
            sequence.append(c)
            a, b = b, c
        return sequence

def fibonacci_animation(n):
    """
    Generate and display the Fibonacci sequence with an animation effect.

    Args:
        n (int): The number of terms in the Fibonacci sequence.

    Returns:
        list: The generated Fibonacci sequence.
    """
    print(Fore.YELLOW + "Initializing Fibonacci Sequence Generator..." + Style.RESET_ALL)
    time.sleep(1)

    fibonacci_sequence = fibonacci(n)

    print(Fore.GREEN + "Generating Fibonacci Sequence..." + Style.RESET_ALL)
    for i, num in enumerate(fibonacci_sequence):
        print(Fore.CYAN + f"Term {i + 1}: {num}" + Style.RESET_ALL)
        time.sleep(random.uniform(0.1, 0.5))

    print(Fore.MAGENTA + "Fibonacci Sequence Complete!" + Style.RESET_ALL)
    return fibonacci_sequence

def display_sequence(fibonacci_sequence, reverse=False):
    """
    Display the Fibonacci sequence.

    Args:
        fibonacci_sequence (list): The Fibonacci sequence to display.
        reverse (bool, optional): If True, display the sequence in reverse order. Defaults to False.
    """
    print(Fore.YELLOW + "Displaying Fibonacci Sequence:" + Style.RESET_ALL)
    if reverse:
        fibonacci_sequence.reverse()
    for num in fibonacci_sequence:
        print(Fore.GREEN + str(num) + Style.RESET_ALL, end=" ")
    print()

def get_valid_input(prompt, data_type=int):
    """
    Get valid user input of specified data type with error handling.

    Args:
        prompt (str): The input prompt message.
        data_type (type, optional): The expected data type. Defaults to int.

    Returns:
        data_type: Valid user input of specified data type.
    """
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid value." + Style.RESET_ALL)

# User Input with Error Handling
num_terms = get_valid_input(Fore.BLUE + "Enter the number of terms: " + Style.RESET_ALL)

# Generate Fibonacci Sequence
fibonacci_sequence = fibonacci_animation(num_terms)

# Display Sequence
display_sequence(fibonacci_sequence)

# Offer the option to display the sequence in reverse
reverse_option = get_valid_input(Fore.BLUE + "Do you want to display the sequence in reverse? (y/n): " + Style.RESET_ALL, str)
if reverse_option.lower() == 'y':
    display_sequence(fibonacci_sequence, reverse=True)

print(Fore.CYAN + "Thank you for using the Fibonacci Sequence Generator!" + Style.RESET_ALL)