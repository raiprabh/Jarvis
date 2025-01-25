from plugin import plugin
import secrets


@plugin('coin flip')
def coin_flip(jarvis, s):
    """
    Randomizes between Heads and Tails
    """

    options = ('Heads', 'Tails')

    rand_value = options[secrets.SystemRandom().randint(0, 1)]

    jarvis.say(rand_value)
