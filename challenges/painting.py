

def wall_painting (ink, x, y):
    wall_size = x * y
    total = wall_size / ink
    return print(f'You need {total} inks to paint this wall')


ink = int(input('Inform the ink performance: '))
wall_hight = int(input('Inform the wall hight: '))
wall_width = int(input('Inform the wall width: '))

wall_painting(ink, wall_hight, wall_width)
