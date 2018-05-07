'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import w_lutz

lights =  w_lutz.game_room
flashAnimation = FlashAnimation(lights, [ORANGE, RED, BLUE], numCycles=2, numFlashes=4)
twinkleAnimation = TwinkleFadeAnimation(lights, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=2)
chaseAnimation = ChaseAnimation(lights, [PURPLE, GREEN, BLUE, RED, YELLOW], numCycles=2, blockSize=1, moveDelay=1.5)
fadeToBlackAnimation = FadeToColorAnimation(w_lutz.globalLight, [WHITE], brightness=1, tsTime=1)
fadeToColorAnimation = FadeToColorAnimation(w_lutz.globalLight, [BLUE], brightness=200, tsTime=10)

ceilingAnimation = ChaseAnimation(w_lutz.game_room_main, [ORANGE, YELLOW, GREEN], numCycles=90, 
	blockSize=len(w_lutz.game_room_main), moveDelay=2)
bgAnimation = TwinkleFadeAnimation(w_lutz.game_room_background, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=900)
compositeAnimation = CompositeAnimation(ceilingAnimation, [bgAnimation])

if __name__ == '__main__':
	controls.startLightQueue()
	while True:
		flashAnimation.run()
	controls.stopLightQueue()




