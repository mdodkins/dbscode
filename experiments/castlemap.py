from dbscode_minecraft import *
from autocastle import tower

def draw_castle_map(map, tower_height, tower_spacing):
   x = 0
   y = 0
   for t in range(0,len(map)):
      if map[t] == 'O':
         tower((x,y,0), tower_height)

      if map[t] == '\n':
         y = y + tower_spacing
         x = 0
      else:
         x = x + tower_spacing

draw_castle_map("O", 10, 10)

  
