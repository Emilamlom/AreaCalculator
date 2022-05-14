# Part 1
# Import the necessary module (use an alias name during importation to help with code readability)
import emily_kaemmerer as areas

def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    # Code to check that a valid shape has been selected
    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))

    return shape

def main():
    while True:
        # Part 2
        # Determine which shape the user selected by calling the selection() function
        # Determine which area should be computed based off the value returned by the selection() function
        shape = selection()
        if shape == 1:
            areas.circle()
        elif shape == 2:
            areas.rectangle()
        elif shape == 3:
            areas.square()
        elif shape == 4:
            areas.triangle()

        # Part 3
        # Ask the user if they want to continue
        # If they enter 'n', break out of the loop and display 'PROGRAM DONE'
        # If they enter 'y' the loop should be repeated (go back to the top of the loop)
        # Use a loop to check that they are entering a valid response (y/n)

        status = input('Would you like to continue? (y/n): ').strip().lower()
        while status != 'y' and status != 'n':
            status = input('Would you like to continue? (please enter either "y" or "n"): ').strip().lower()

        if status == 'y':
            continue
        elif status == 'n':
            print('PROGRAM DONE')
            break

if __name__ == '__main__':
    main()
