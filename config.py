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

# TODO: Set up gradients
HAIR_GRADIENTS = {
    'blonde': ['#ed984a', '#f0c97d', '#faf4bd'],
    'brunette': ['#59312c', '#694838', '#786148'],
    'black': ['#111822', '#2f313e', '#504d5c']
}

EYE_GRADIENTS = {'brown': ['#59312c', '#694838', '#786148'],
                 'black': ['#111822', '#5b7f79', '#ededc4']}

def define_option(name, recolorable=True, batch_size=1):
    return {'name': name,
        'recolorable': recolorable,
        'batch_size': batch_size}