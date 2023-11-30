def create_world(version):
    # Define the characters that represent different elements of the game
    sky = '☁️'
    ground = '⬛'
    brick = '🟫'
    coin = '💰'
    mario = '🍄'
    peach = '👸'

    # Create the stage
    if version == 1:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, brick, coin, brick, sky, sky, sky, sky, sky, sky, sky, brick, coin, brick, sky, sky, sky, sky],
            [sky, sky, sky, brick, coin, brick, sky, sky, sky, sky, sky, sky, sky, brick, coin, brick, sky, sky, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 2:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, coin, coin, sky, sky, sky, sky, sky, sky, sky, coin, coin, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 3:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, coin, coin, sky, brick, brick, sky, sky, sky, sky, coin, coin, sky, brick, brick, sky, sky],
            [sky, sky, sky, sky, brick, brick, sky, brick, brick, sky, sky, sky, sky, brick, brick, sky, brick, brick, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 4:
        world = [
            [sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, coin, coin, sky, sky, sky, sky, sky, sky, sky, coin, coin, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, sky, sky, sky, brick, brick, sky, sky],
            [sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 5:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, coin, sky, brick, brick, sky, sky, sky, sky, sky, coin, sky, brick, brick, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, sky, sky, sky, brick, brick, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 6:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, brick, coin, sky, brick, brick, sky, sky, sky, sky, brick, coin, sky, brick, brick, sky, sky],
            [sky, sky, sky, sky, brick, coin, sky, brick, brick, sky, sky, sky, sky, brick, coin, sky, brick, brick, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 7:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, brick, brick, sky, brick, brick, sky, sky, sky, sky, brick, brick, sky, brick, brick, sky, sky],
            [sky, sky, sky, sky, coin, coin, sky, coin, coin, sky, sky, sky, sky, coin, coin, sky, coin, coin, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 8:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, coin, coin, sky, sky, sky, sky, brick, brick, sky, coin, coin, sky, sky, sky, sky],
            [sky, sky, sky, sky, brick, brick, sky, sky, sky, sky, brick, brick, sky, brick, brick, sky, sky, sky, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 9:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, coin, sky, sky, brick, brick, sky, sky, sky, sky, sky, coin, sky, sky, brick, brick],
            [sky, sky, sky, sky, sky, brick, sky, sky, sky, sky, sky, sky, sky, sky, brick, sky, sky, sky, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    elif version == 10:
        world = [
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
            [sky, sky, sky, sky, coin, coin, sky, sky, sky, sky, brick, brick, sky, sky, coin, coin, sky, sky, sky, sky],
            [sky, sky, sky, sky, brick, brick, sky, brick, brick, sky, brick, brick, sky, sky, brick, brick, sky, sky, sky, peach],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]
    else:
        print("Invalid version number. Please enter a number between 1 and 10.")

    # Place Mario on the stage
    mario_position = [3, 0]
    world[mario_position[0]][mario_position[1]] = mario

    return world, mario_position

def print_world(world):
    # Imprimimos el escenario
    for row in world:
        print(' '.join(row))
    print("\n")

def move_left(world, mario_position):
    coin_collected = 0
    if mario_position[1] > 0 and world[mario_position[0]][mario_position[1]-1] != '🟫':
        # If Mario encounters a coin, he collects it
        if world[mario_position[0]][mario_position[1]-1] == '💰':
            world[mario_position[0]][mario_position[1]-1] = '☁️'
            coin_collected = 1
        world[mario_position[0]][mario_position[1]], world[mario_position[0]][mario_position[1]-1] = world[mario_position[0]][mario_position[1]-1], world[mario_position[0]][mario_position[1]]
        mario_position[1] -= 1
    print_world(world)
    return world, mario_position, coin_collected

def move_right(world, mario_position):
    coin_collected = 0
    if mario_position[1] < len(world[0]) - 1 and world[mario_position[0]][mario_position[1]+1] != '🟫':
        # If Mario encounters a coin, he collects it
        if world[mario_position[0]][mario_position[1]+1] == '💰':
            world[mario_position[0]][mario_position[1]+1] = '☁️'
            coin_collected = 1
        world[mario_position[0]][mario_position[1]], world[mario_position[0]][mario_position[1]+1] = world[mario_position[0]][mario_position[1]+1], world[mario_position[0]][mario_position[1]]
        mario_position[1] += 1
    print_world(world)
    return world, mario_position, coin_collected

def jump(world, mario_position):
    coin_collected = 0
    if mario_position[0] > 0 and world[mario_position[0]-1][mario_position[1]] != '🟫':
        # If Mario encounters a coin, he collects it
        if world[mario_position[0]-1][mario_position[1]] == '💰':
            world[mario_position[0]-1][mario_position[1]] = '☁️'
            coin_collected = 1
        world[mario_position[0]][mario_position[1]], world[mario_position[0]-1][mario_position[1]] = world[mario_position[0]-1][mario_position[1]], world[mario_position[0]][mario_position[1]]
        mario_position[0] -= 1
    print_world(world)
    return world, mario_position, coin_collected

def move_down(world, mario_position):
    coin_collected = 0
    # Check if Mario can move down
    if mario_position[0] < len(world) - 1 and world[mario_position[0]+1][mario_position[1]] != '🟫':
        # If Mario encounters a coin, he collects it
        if world[mario_position[0]+1][mario_position[1]] == '💰':
            world[mario_position[0]+1][mario_position[1]] = '☁️'
            coin_collected = 1
        # Swap Mario's current position with the position below
        world[mario_position[0]][mario_position[1]], world[mario_position[0]+1][mario_position[1]] = world[mario_position[0]+1][mario_position[1]], world[mario_position[0]][mario_position[1]]
        # Update Mario's position
        mario_position[0] += 1
    print_world(world)
    return world, mario_position, coin_collected
