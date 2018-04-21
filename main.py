from Hugin import record_cube
from Mimir import find_solution
from Sleipner import CubeMechanics


def main():
    """The main function that solves the cube"""

    input('Ready to start?')

    state_string = record_cube()

    solution_move_set = find_solution(state_string)

    print(solution_move_set)

    #TODO: NEED TO BE ABLE TO INITIALIZE MOTORS/GRIPPERS AS PORTS

    # Initialize motors:



if __name__ == '__main__':
    main()
