'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights
# <<<<<<< HEAD
LIGHT_ID = 3

# animation = [
# 	AnimationStep(controls, LIGHT_ID, RED, tsTime=10),
# 	AnimationStep(controls, LIGHT_ID, BLUE, tsTime=10),
# 	AnimationStep(controls, LIGHT_ID, RED, tsTime=10),
# 	AnimationStep(controls, LIGHT_ID, BLUE, tsTime=10),
# 	AnimationStep(controls, LIGHT_ID, RED),
# 	AnimationStep(controls, LIGHT_ID, BLUE),
# 	AnimationStep(controls, LIGHT_ID, RED),
# 	AnimationStep(controls, LIGHT_ID, BLUE),
# 	AnimationStep(controls, LIGHT_ID, RED),
# 	AnimationStep(controls, LIGHT_ID, BLUE),
# 	AnimationStep(controls, LIGHT_ID, RED),
# 	AnimationStep(controls, LIGHT_ID, BLUE),
# ]

# def loopAnimation(lightID=0):
# 	for i in range(10):
# 		for step in animation:
# 			step.triggerStep(lightID)

# import threading
# def spawn(f, *args):
# 	t = threading.Thread(target=f, args=args)
# 	#t.daemon = True
# 	t.start()

# if __name__ == '__main__':
# 	spawn(loopAnimation)
# =======
# lights =  fuselights.mainroom
# flashAnimation = FlashAnimation(lights, [ORANGE, RED, BLUE], numCycles=2, numFlashes=4)
# twinkleAnimation = TwinkleFadeAnimation(lights, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=2)
# chaseAnimation = ChaseAnimation(lights, [PURPLE, GREEN, BLUE], numCycles=2, blockSize=6, moveDelay=0.2)
# fadeToBlackAnimation = FadeToColorAnimation(fuselights.globalLight, [WHITE], brightness=1, tsTime=1)
# fadeToColorAnimation = FadeToColorAnimation(fuselights.globalLight, [BLUE], brightness=200, tsTime=10)

# ceilingAnimation = ChaseAnimation(fuselights.ceiling, [ORANGE, YELLOW, GREEN], numCycles=90, blockSize=len(fuselights.ceiling), moveDelay=2)
# bgAnimation = TwinkleFadeAnimation(fuselights.background, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=900)
# compositeAnimation = CompositeAnimation(ceilingAnimation, [bgAnimation])

naman_lights = [Light(controls, LIGHT_ID, "Game Room", 0.9, 0.15)]

lights =  naman_lights
flashAnimation = FlashAnimation(lights, [ORANGE, RED, BLUE], numCycles=2, numFlashes=4)
twinkleAnimation = TwinkleFadeAnimation(lights, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=2)
chaseAnimation = ChaseAnimation(lights, [PURPLE, GREEN, BLUE], numCycles=2, blockSize=6, moveDelay=0.2)
fadeToBlackAnimation = FadeToColorAnimation(naman_lights, [WHITE], brightness=1, tsTime=1)
fadeToColorAnimation = FadeToColorAnimation(naman_lights, [BLUE], brightness=200, tsTime=10)

ceilingAnimation = ChaseAnimation(naman_lights, [ORANGE, YELLOW, GREEN], numCycles=90, blockSize=len(naman_lights), moveDelay=2)
# bgAnimation = TwinkleFadeAnimation(fuselights.background, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=900)
compositeAnimation = CompositeAnimation(ceilingAnimation, None)

if __name__ == '__main__':
	controls.startLightQueue()
	while True:
		compositeAnimation.run()
	controls.stopLightQueue()
# >>>>>>> 522b1bf8da2cc70476fb8549a68612788b114418
