'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights
LIGHT_ID = 3

animation = [
	AnimationStep(controls, LIGHT_ID, RED, tsTime=10),
	AnimationStep(controls, LIGHT_ID, BLUE, tsTime=10),
	AnimationStep(controls, LIGHT_ID, RED, tsTime=10),
	AnimationStep(controls, LIGHT_ID, BLUE, tsTime=10),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
]

def loopAnimation(lightID=0):
	for i in range(10):
		for step in animation:
			step.triggerStep(lightID)

import threading
def spawn(f, *args):
	t = threading.Thread(target=f, args=args)
	#t.daemon = True
	t.start()

if __name__ == '__main__':
	spawn(loopAnimation)
