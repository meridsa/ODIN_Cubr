# A class that holds the two motor classes of movers and rotators.
# todo make interface between motors and code

from Hugin import check_input
import time
from enumsProj import MotorOrientations as MO, MoverPosition as MP, RotatorPosition as RP

# The time each action has to complete, can be set to false

action_time = 2

class Motor:
    """Abstract class for all motors, has orientation so it's easy to see what functions
    should call it, and driver and switch_state so the pins are easily associated with it:
    Switch_state:   Driver1,    Driver2
        00 (0)      LM          RM
        01 (1)      LR          RR
        10 (2)      UM          DM
        11 (3)      UR          DR
    First letter = orientation, 2nd letter for either mover or rotator"""

    def __init__(self, orientation, driver, switch_state):
        if type(orientation) == int:
            if orientation in MO:
                self.orientation = orientation
            else:
                raise ValueError('Entered value not within allowed range: 0/1/2/3')
        else:
            raise TypeError('Type not int')
        self.driver = driver
        self.switch_state = switch_state



class Mover(Motor):
    """A class for the motors that move the grippers towards and from the cube
    this class contains all the code avoiding double moves, such as
    moving in when position is already in"""

    def __init__(self, motor, position):
        super(Motor motor)
        print('Position values: in = ' + str(MP.In) + ', out = ' + str(MP.Out))
        print('Orientation values: Up = ' + str(MO.Up) + ', Left = ' + str(MO.Left) + ', '
                      'Right = ' + str(MO.Right) + ', Down = ' + str(MO.Down))
        print('It is really vital to confirm that the position: ' + position + 'and '
              'orientation: ' + orientation + ' is correct to avoid any potential collisions!')
        correct_pos_ori_prompt = check_input('Is the orientation and position correct [y/n]')
        while True:
            if correct_pos_ori_prompt in 'n':
                position = check_input('Enter position: [0/1]')
                orientation = check_input('Enter orientation: [0/1/2/3]')
            elif correct_pos_ori_prompt in 'y':
                if type(position) == str:
                    if position in MP:
                        self.position = position
                    else:
                        raise ValueError('Entered value not within allowed range: 0/1')
                else:
                    raise TypeError('Type not int')
            correct_pos_ori_prompt = check_input('Please enter [y] or [n], or [q] to quit')

    # Moves, contains conditionals to avoid double moves
    def move_in(self, action_timer=True):
        if self.position == MP.Out:
            if action_timer:
                time.sleep(action_time)
            pass # todo integrate with stepper motors
        else:
            pass

    def move_out(self, action_timer):
        if self.position == MP.In:
            if action_timer:
                time.sleep(action_time)
            pass # todo integrate with stepper motors
        else:
            pass

    # Finding position and orientation
    def get_position(self):
        return self.position

    def get_orientation(self):
        return self.orientation


class Rotator(Motor):
    """A class for the motors that rotate the grippers"""

    def __init__(self, position, orientation):
        if type(position) == int:
            if position in RP:
                self.position = position
            else:
                raise ValueError('Entered value not within allowed range: 0/1')
        else:
            raise TypeError('Type not int')

    def get_position(self):
        return self.position

    def get_orientation(self):
        return self.orientation

    # As rotation collisions depend only on collision with
    # other grippers, code to avoid that is in the CubeMechanics
    # class and there is no fear of double rotating or anything
    def rotate_clockwise(self, action_timer=True):
        if action_timer:
            time.sleep(action_time)
        pass

    def rotate_half(self, action_timer=True):
        if action_timer:
            time.sleep(action_time)
        pass

    def rotate_counter_clockwise(self, action_timer=True):
        if action_timer:
            time.sleep(action_time)
        pass
