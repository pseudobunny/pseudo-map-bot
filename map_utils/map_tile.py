map_tiles = ["\N{WHITE MEDIUM SQUARE}"]
for i in range(9):
    map_tiles.append(f"{i+1}\N{COMBINING ENCLOSING KEYCAP}")

def map_tile(val):
    global map_tiles
    return map_tiles[int(val)]