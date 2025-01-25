from plugin import plugin
from colorama import Fore
import secrets


@plugin("random list")
def generate_random_list(jarvis, str):
    ls = get_user_input(jarvis)

    if len(ls) <= 1:
        jarvis.say("Enter at least 2 strings", Fore.RED)
    else:
        secrets.SystemRandom().shuffle(ls)
        for i in ls:
            jarvis.say(i, Fore.GREEN)


def get_user_input(jarvis):
    ls = list()
    while True:
        try:
            user_input = jarvis.input("Enter string (enter \"JarvisStop\" to end): ")
            if user_input == "JarvisStop":
                break
            ls.append(user_input)
        except ValueError:
            jarvis.say("Sorry, I didn't understand that.", Fore.RED)
            continue

    return ls
