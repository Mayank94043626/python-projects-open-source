from ursina import *

app = Ursina()

# Constants for block types
BLOCK_GRASS = 1
BLOCK_STONE = 2
BLOCK_BRICK = 3
BLOCK_DIRT = 4

# Textures for blocks
TEXTURES = {
    BLOCK_GRASS: 'assets/grass_block.png',
    BLOCK_STONE: 'assets/stone_block.png',
    BLOCK_BRICK: 'assets/brick_block.png',
    BLOCK_DIRT: 'assets/dirt_block.png'
}

# Mapping keys to block types
BLOCK_PICKS = {
    '1': BLOCK_GRASS,
    '2': BLOCK_STONE,
    '3': BLOCK_BRICK,
    '4': BLOCK_DIRT
}

# Create the scene
scene = Entity()

def update():
    # Handle block selection
    handle_block_selection()

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), block_type=BLOCK_GRASS):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=TEXTURES[block_type],
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                block_type = BLOCK_PICKS.get(block_pick, BLOCK_GRASS)
                voxel = Voxel(position=self.position + mouse.normal, block_type=block_type)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

# ... Sky, Hand, and Player classes as before ...

def handle_block_selection():
    global block_pick
    for key, block_type in BLOCK_PICKS.items():
        if held_keys[key]:
            block_pick = block_type

if __name__ == "__main__":
    grass_texture = load_texture(TEXTURES[BLOCK_GRASS])
    stone_texture = load_texture(TEXTURES[BLOCK_STONE])
    brick_texture = load_texture(TEXTURES[BLOCK_BRICK])
    dirt_texture = load_texture(TEXTURES[BLOCK_DIRT])

    window.fps_counter.enabled = False
    window.exit_button.visible = False

    for z in range(20):
        for x in range(20):
            voxel = Voxel(position=(x, 0, z))

    player = FirstPersonController()
    sky = Sky()
    hand = Hand()

    app.run()
