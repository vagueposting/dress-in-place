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

# The gradients should have VERY dark shadows,
# moderate midtones, and moderate-to-light highlights.

SKIN_GRADIENTS = {
    'Light Warm': ['#916b55', '#c0a188', '#f0dac1'],
    'Mid Warm': ['#825538', '#a47758', '#c79a7a'],
    'Dark Warm': ['#602915', '#723d23', '#855132'],
    'Light Cool': ['#9c5e5e', '#ca908c', "#fbe8dd"],
    'Mid Cool': ['#8b4b4b', '#ac6f68', '#cd9588'],
    'Dark Cool': ['#421010', '#612c25', '#80483c']
}
HAIR_GRADIENTS = {
    'Black': ['#111822', "#484C64", "#d3d1de"],
    'Blonde': ["#b48129", '#f0c97d', '#faf4bd'],
    'Brunette': ['#59312c', '#694838', "#E49846"],
    'Redhead': ['#441723', '#952e39', '#e6513d']
}
# Eye gradients are 4-colors (3 shades + FFBF7)
EYE_GRADIENTS = {'Brown': ['#59312c', '#694838', 
                           '#786148', '#FFFBF7'],
                 'Black': ['#111822', '#5b7f79', 
                           '#ededc4', '#FFFBF7'],
                 'Blue': ['#17235e', '#176aac', 
                          '#18baf0', '#FFFBF7'],
                 'Green': ['#0e481b', '#619f2a', 
                           '#dbf820', '#FFFBF7']}

SOCK_GRADIENTS = {'White': ["#4C4650", '#f1f7fe'],
                  'Blue': ["#363581", "#e6faff"],
                  'Pink': ["#c66060", "#ffedf8"],
                  'Green': ["#439777", "#f7ffec"]}

GRADIENT_MAPPING = {
    'hair': HAIR_GRADIENTS,
    'eyes': EYE_GRADIENTS,
    'body': {
        'parts': ['head', 'torso-and-legs', 'lower-arms'],
        'gradients': SKIN_GRADIENTS
    },
    'socks': SOCK_GRADIENTS
    # Add more as needed
}

# Define customization options for each part
CUSTOMIZATION_OPTIONS = {
    'Body': {'color': ('Skin Color', list(SKIN_GRADIENTS.keys()), 'body')},
    'Hairstyle': {
        'style': ('Hairstyle', ['Bob', 'Idol-inspired', 'Long', 'Pixie'], 'hair'),
        'color': ('Hair Color', list(HAIR_GRADIENTS.keys()), 'hair')
    },
    'Eyes': {
        'style': ('Eye Style', ['Tareme', 'Flat', 'Tsurime'], 'eyes'),
        'color': ('Eye Color', list(EYE_GRADIENTS.keys()), 'eyes')
    },
    'Mouth': {
        'style': ('Mouth Style', ['Smile', 'Meh', 'Frown'], 'mouth')
    },
    'Tie': {
        'style': ('Tie Style', ['Standard', 'Classic', 'Bow'], 'tie')
    },
    'Skirt': {
        'style': ('Skirt Style', ['Short', 'Medium', 'Long'], 'skirt')
    },
    'Socks': {
        'style': ('Sock Style', ['Thigh-high', 'Kitty', 'Frilly'], 'socks'),
        'color': ('Sock Color', list(SOCK_GRADIENTS.keys()), 'socks')
    },
    'Shoes': {
        'style': ('Shoe Style', ['Mary Jane', 'Loafers'], 'shoes')
    }
}

def define_option(name, recolorable=True, batch_size=1):
    return {'name': name,
        'recolorable': recolorable,
        'batch_size': batch_size}