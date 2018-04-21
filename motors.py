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

    def __init__(self, orientation, pins, driver, switch_state):
        self.orientation = orientation
        self.driver = driver
        self.switch_state = switch_state
        # The pins are important to get in correct order
        self.pins = []
        for p in pins:
            self.pins.append(p)


    def get_orientation(self):
        """Getter for orientation"""
        return self.orientation

    def rotate(self, direction, degrees, speed=0):
        pass




class Mover(Motor):
    """A class for the motors that move the grippers towards and from the cube
    this class contains all the code avoiding double moves, such as
    moving in when position is already in"""

    def __init__(self, orientation, pins, driver, switch_state, position):
        super().__init__(orientation, pins, driver, switch_state)
        self.position = position

    # Moves, contains conditionals to avoid double moves
    def move_in(self, action_timer=True):
        if self.position == MP.Out:
            if action_timer:
                time.sleep(action_time)
                self.rotate(0, 45)
            pass # todo integrate with stepper motors
        else:
            pass

    def move_out(self, action_timer):
        if self.position == MP.In:
            if action_timer:
                time.sleep(action_time)
                self.rotate(1, 45)
            pass # todo integrate with stepper motors
        else:
            pass

    # Finding position and orientation
    def get_position(self):
        return self.position



class Rotator(Motor):
    """A class for the motors that rotate the grippers"""
    def __init__(self, orientation, pins, driver, switch_state, position):
        super().__init__(orientation, pins, driver, switch_state)
        self.position = position

    def get_position(self):
        return self.position

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
