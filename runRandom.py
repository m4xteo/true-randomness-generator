''' 
True Randomness Generator Concept 1.0

How it works:
- Generates noise based on mouse-movements
- Takes random values based on clock jitter code 


To-Do:
- Generate random entropy 

Designed by Matt (m4xteo) 
"Trust no one"

''' 


import pyautogui
import sys
import secrets

randomSeed = []

def main():
	print(rngClock())
	#positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
	#print(positionStr, end='')
	#print('\b' * len(positionStr), end='', flush=True)


def generateSeed():

	return x

def generateNoise():
	x, y = pyautogui.position()

def rngClock():
	t_clock = secrets.randbelow(50)

	return t_clock

def generateRand_1(srng, n_inputs):
	return x

if __name__ == "__main__":
	main() 
