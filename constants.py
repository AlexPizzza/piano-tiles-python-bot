EMULATOR_REGION = (5, 30, 555, 975)

LANE_HEIGHT = 727
STARTING_MIDDLE_LANE = 65
DIFFERENCE_BETWEEN_LANES = 135

LANES = [
    {
        'press': False,
        'location': (LANE_HEIGHT, STARTING_MIDDLE_LANE),
        'key': 'a'
    },
    {
        'press': False,
        'location': (LANE_HEIGHT, STARTING_MIDDLE_LANE + DIFFERENCE_BETWEEN_LANES),
        'key': 's'
    },
    {
        'press': False,
        'location': (LANE_HEIGHT, STARTING_MIDDLE_LANE + 2 * DIFFERENCE_BETWEEN_LANES),
        'key': 'd'
    },
    {
        'press': False,
        'location': (LANE_HEIGHT, STARTING_MIDDLE_LANE + 3 * DIFFERENCE_BETWEEN_LANES),
        'key': 'f'
    }
]
