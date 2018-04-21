from Hugin import record_cube
from Mimir import find_solution
import ServoMotors as SM


def main():
    """The main function that solves the cube"""
    arduino = SM.ServoControl()

    input('Ready to start?')

    state_string = record_cube(arduino)

    solution_move_set = find_solution(state_string)

    print(solution_move_set)

    arduino.solve(solution_move_set)

    #TODO: Fix CV by hardcode
    #TODO: Remove redundant code




if __name__ == '__main__':
    main()
