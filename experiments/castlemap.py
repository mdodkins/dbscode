from dbscode_minecraft import *
from autocastle import tower

def draw_castle_map(map, tower_height, tower_spacing):
   x = 0
   for t in range(0,len(map)):
      if map[t] == 'O':
         tower((x,0,0), tower_height)
      x=x+tower_spacing

draw_castle_map("O", 10, 10)

  
