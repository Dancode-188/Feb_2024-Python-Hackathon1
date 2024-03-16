# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

import time
import random
import colorama
from colorama import Fore, Style

colorama.init()

def vote_eligibility_checker():
    """
    Check the eligibility of a person to vote based on their age.

    This function prompts the user to input their age and then checks if they are eligible to vote.
    If the age is 18 or above, the function informs the user that they are eligible to vote
    and provides tips on being a responsible voter.
    If the age is below 18, the function informs the user that they are not eligible to vote yet
    and suggests ways to get involved while waiting for future elections.

    Note:
        The function uses colorama for colorful terminal output.

    """
    print(Fore.CYAN + "Welcome to the" + Fore.MAGENTA + " Vote Eligibility" + Fore.YELLOW + " Checker!" + Style.RESET_ALL)
    print(Fore.GREEN + "Let's find out if you can exercise your civic duty!" + Style.RESET_ALL)

    try:
        age = int(input(Fore.BLUE + "Enter your age: " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "Invalid input! Age must be a number." + Style.RESET_ALL)
        return

    loading_messages = [
        "Checking voter rolls...",
        "Verifying eligibility criteria...",
        "Consulting the electoral commission...",
        "Analyzing voter data...",
        "Processing your information..."
    ]

    for message in loading_messages:
        print(Fore.YELLOW + message + Style.RESET_ALL)
        time.sleep(random.uniform(0.5, 1.5))

    if age >= 18:
        print(Fore.GREEN + "🗳️  You are eligible to vote! Make your voice heard!" + Style.RESET_ALL)
        print(Fore.YELLOW + "As a responsible citizen, consider these tips:")
        print("1. Research candidates and their policies.")
        print("2. Encourage others to vote.")
        print("3. Remember, every vote counts!")
    else:
        print(Fore.RED + "⛔ You are not eligible to vote yet. Stay tuned for future elections!" + Style.RESET_ALL)
        print(Fore.YELLOW + "While you wait to vote, here are some ways to get involved:")
        print("1. Participate in local community events.")
        print("2. Educate yourself on important issues.")
        print("3. Volunteer for causes you care about.")

    print(Fore.CYAN + "Thank you for using the Vote Eligibility Checker!" + Style.RESET_ALL)

vote_eligibility_checker()