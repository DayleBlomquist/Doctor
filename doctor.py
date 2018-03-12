"""
Program: doctor.py
Author: Dayle

Conducts an interactive session of nondirective psychotherapy.
"""

import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.", "That's disturbing.", "I'm calling the police.", "You're a sick individual.")

qualifiers = ("Why do you say that ", "You seen to think that ", "Can you explain why ", "How does that make you feel ", "Why are you so screwed up ", "Stop whining ")

replacements = {"I":"you", "me":"you", "my": "your", "we":"you", "us":"you", "mine":"yours"}

def reply(sentence):
	"""Builds and returns a reply to the sentence."""
	probability = random.randint(1,4)
	if probability == 1:
		return random.choice(hedges)
	else:
		return random.choice(qualifiers) + changePerson(sentence)
		
def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns."""
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)
	
def main():
	"""Handles the interaction between patient and doctor."""
	print("Good morning, I hope you are well today.")
	print("What can I do for you?")
	while True:
		sentence = input("\n>> ")
		if sentence.upper() == "QUIT":
			print("Have a nice day!")
			break
		print(reply(sentence))
		
main()
		