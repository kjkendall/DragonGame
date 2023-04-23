# KYRA KENDALL

def main():
    # Define rooms and items
    rooms = {
        'Library': {'North': 'Gallery'},
        'Gallery': {'North': 'Dungeon', 'East': 'Dining Room', 'South': 'Library'},
        'Dungeon': {'South': 'Gallery'},
        'Cellar': {'West': 'Dining Room', 'North': 'Pantry'},
        'Pantry': {'South': 'Cellar'},
        'Dining Room': {'West': 'Gallery', 'East': 'Cellar', 'North': 'Kitchen'},
        'Kitchen': {'South': 'Dining Room'}
    }
    items = {
        'Library': 'book',
        'Gallery': 'armor',
        'Cellar': 'sword',
        'Dining Room': 'shield',
        'Kitchen': 'peanut butter sandwich',
    }
    villain_room = 'Dungeon'
    has_book = False
    has_armor = False
    has_sword = False
    has_shield = False
    has_sandwich = False

    # Initialize game loop
    current_room = 'Library'
    game_over = False

    # Print welcome message
    print(
        "Welcome to the Castle Adventure Game! Your goal is to  find the items, defeat the dragon and rescue Princess Peach in order to escape the castle.")

    while not game_over:
        # Output current room and available moves
        print('You are in the', current_room)
        print('Available moves:', list(rooms[current_room].keys()))

        # Get player input
        command = input('Enter command: ')

        # Handle valid move commands
        if command in rooms[current_room]:
            new_room = rooms[current_room][command]
            # Check if the new room has an item and add it to the inventory
            if new_room in items:
                item = items[new_room]
                print('You found a', item)
                if item == 'book':
                    has_book = True
                elif item == 'armor':
                    has_armor = True
                elif item == 'sword':
                    has_sword = True
                elif item == 'shield':
                    has_shield = True
                elif item == 'peanut butter sandwich':
                    has_sandwich = True
            # Check if the new room is the villain room
            if new_room == villain_room:
                # Check if the player has all the items to win
                if has_book and has_armor and has_sword and has_shield and has_sandwich:
                    print('You defeated the dragon and escaped the castle with all the treasures! You won the game!')
                    game_over = True
                else:
                    print('You encountered the dragon before collecting all the treasures and lost the game.')
                    game_over = True
            else:
                current_room = new_room
        # Handle exit command
        elif command == 'exit':
            current_room = 'exit'
            game_over = True
        # Handle invalid commands
        else:
            print('Invalid command.')

    print('Game over.')


if __name__ == '__main__':
    main()
