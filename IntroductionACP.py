import random

compliments_list = [
    "Your smile is beautiful!",
    "That's a fantastic outfit you're wearing.",
    "You have a really sharp mind.",
    "You make the world a better place just by being in it.",
    "Talking to you is the highlight of my day."
]

greet = input("Hello! What is your name? ")
mood = input(f"Wow! You have such a nice name, {greet}. How are you feeling? ")

random_addition = random.choice(compliments_list)

compliment = (f"You said you are feeling {mood}. Well, I will make you feel even better than you are right now. {random_addition}")

print(compliment)