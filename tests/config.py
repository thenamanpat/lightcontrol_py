'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Light Controller Config/Import File
'''

from HueControls import HueControls
from LightControl import *

#HUE_BRIDGE_IP = '10.3.0.177' # Fuse
#HUE_BRIDGE_API_KEY = ' d5orxbetHKF46FCV1wBmnFTVNSkGQWMSjwNOHu2i'
HUE_BRIDGE_IP = '192.168.1.125' # 344
HUE_BRIDGE_API_KEY = 'QeU9qwKYDc5Z1OqzhPMbrutdRwSKj9wDFgLUAii4'

controls = HueControls(HUE_BRIDGE_IP, HUE_BRIDGE_API_KEY)

RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"