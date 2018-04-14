# Script that holds the gripper class
from motors import Mover, Rotator
from enumsProj import MotorOrientations as MO, MoverPosition as MP, RotatorPosition as RP, GripperPosition as GP


class Gripper:
    """Class for the grippers that are moved in and out and rotated"""

    def __init__(self, mover, rotator, orientation):

        if isinstance(mover, Mover):
            self.mover = mover
        else:
            raise TypeError('mover is not Mover type')

        if isinstance(rotator, Rotator):
            self.rotator = rotator
        else:
            raise TypeError('rotator is not Rotator type')

        if type(orientation) is int:
            if orientation in MO:
                self.orientation = orientation
            else:
                raise ValueError('Entered value not within allowed range: 0/1/2/3')
        else:
            raise TypeError('Type not int')

    def move_in(self, AT=True):
        self.mover.move_in(AT)

    def move_out(self, AT=True):
        self.mover.move_out(AT)

    def rotate1(self, AT=True):
        self.rotator.rotate_clockwise(AT)

    def rotate2(self, AT=True):
        self.rotator.rotate_half(AT)

    def rotate3(self, AT=True):
        self.rotator.rotate_counter_clockwise(AT)

    def rotate(self, rotation, AT=True):
        if rotation == 1:
            self.rotate1(AT)
        elif rotation == 2:
            self.rotate2(AT)
        elif rotation == 3:
            self.rotate3(AT)
        else:
            raise RuntimeError('No rotations of 4 or greater')

    def set_default(self): # TO avoid crashes CubeMechanics needs to orient adjacent grippers vertically
        # Finding original position and orientation
        org_mover_position = self.mover.get_position()
        org_rotation_position = self.rotator.get_position()
        # If gripper already in default position
        if org_mover_position == MP.In and org_rotation_position == RP.Vertical:
            pass
        # If gripper is out but vertical
        elif org_mover_position == MP.Out and org_rotation_position == RP.Vertical:
            self.move_in()
        # If gripper is out and horizontal
        elif org_mover_position == MP.out and org_rotation_position == RP.Horizontal:
            self.rotate1()
            self.move_in()
        # If gripper is in and horizontal
        elif org_mover_position == MP.In and org_rotation_position == RP.Horizontal:
            self.move_out()
            self.rotate1()
            self.move_in()

    def get_position(self):
        rotator_position = self.rotator.get_position()
        mover_position = self.mover.get_position()
        if rotator_position == RP.Vertical and mover_position == MP.In:
            return GP.Vert_In
        elif rotator_position == RP.Vertical and mover_position == MP.Out:
            return GP.Vert_Out
        elif rotator_position == RP.Horizontal and mover_position == MP.Out:
            return GP.Horiz_Out
        elif rotator_position == RP.Horizontal and mover_position == MP.In:
            return GP.Horiz_In



