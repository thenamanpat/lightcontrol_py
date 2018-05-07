from config import *

globalLight	= [Light(controls, 0, "All Lights", 0, 0)]

game_room_bulb = Light(controls, 3, "Bulb - Game Room", 0.5, 0.9)
game_room_strip = Light(controls, 5, "Strip - Game Room ", 0.5, 0.9)
bar_dimm_bulb = Light(controls, 4, "Bar", 0.5, 0.9)
bedroom_1 = Light(controls, 6, "Bedroom 1", 0.5, 0.9)
bedroom_2 = Light(controls, 7, "Bedroom 2", 0.5, 0.9)

game_room = [game_room_bulb, game_room_strip]
game_room_main = [game_room_strip]
game_room_background = [game_room_bulb]

bar = [bar_dimm_bulb]

bedroom = [bedroom_1, bedroom_2]

alllights = game_room + bedroom

