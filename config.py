CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480
CHARACTER_POS_X = CANVAS_WIDTH * 3.5 / 5
CHARACTER_POS_Y = CANVAS_HEIGHT / 2
SIDEBAR_MAX = 225

LAYER_ORDER = ('head',
                'eyes',
                'mouth',
                'hair',
                'torso-and-legs',
                'socks',
                'shoes',
                'skirt',
                'blouse',
                'tie',
                'collar',
                'lower-arms',
                'lower-sleeves')

def define_option(name, recolorable=True, batch_size=1):
    return {'name': name,
        'recolorable': recolorable,
        'batch_size': batch_size}