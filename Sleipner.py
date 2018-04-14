# A script that holds all the moves such as U3, F1, B2 etc. and outputs a set of mechanical moves such as
# right_gripper.out(), left_gripper.clockwise(), front_gripper_cclockwise() etc.
# based on current orientation of the cube. There are 4 * 6 = 24 possible orientations.
# Functions with capital face letter and number are orientation dependent,
# otherwise orientation-independent

# update will not worry about orientation, all moves will return cube 
# to original orientation. Important to note the grippers are, U, D, R, L
# as the F should face the camera before any move.

from grippers import Gripper
import time
from enumsProj import MotorOrientations as MO, MoverPosition as MP, RotatorPosition as RP, GripperPosition as GP

class CubeMechanics:
    """A class that holds all the class mechanics, i.e. movements of the grippers and how to implement on cube"""
    def __init__(self, UG, RG, DG, LG):
        self.UG = UG            # Up gripper
        self.LG = LG            # Left gripper
        self.DG = DG            # Down gripper
        self.RG = RG            # Right gripper


    def set_default_position(self):
        """Function sets the CubeMechanics to the default position
                without collisions or any change. Default position
                is all grippers in and vertical"""
        self.LG.set_default()
        self.RG.set_default()
        self.UG.set_default()
        self.DG.set_default()

    def return_gripper(self, gripper_index):
        if gripper_index == MO.Left:
            return self.LG
        elif gripper_index == MO.Right:
                return self.RG
        elif gripper_index == MO.Up:
                return self.UG
        elif gripper_index == MO.Down:
                return self.DG
        else:
            raise RuntimeError('No gripper with index 4 or greater')

    # Orientation independent functions, all these return the cube to its original rotation.
    # Follow a similar pattern. If it does not need to rotate cube orientation, i.e. rotate up or down.
    # These are special as they have no grippers in default position.
    # The pattern for gripped sides are:
    # Collision avoidance:
    # Check if all grippers are in default position (in and vertical) any that are not will be set in default position
    # Rotation:
    # Rotate necessary gripper desired direction
    # Re-default:
    # Move rotated gripper out, set vertical and move in again

    def rotate(self, face, rotation):
        self.set_default_position()
        if face < 4:
            gripper = self.return_gripper(face)
            gripper.rotate(rotation)
            gripper.set_default()
        elif face == MO.Front:
            # move left and right out simultaneously
            self.LG.move_out(AT=False)
            self.RG.move_out(AT=True)
            # Up and down moving Front to Left
            self.UG.rotate1(AT=False)
            self.DG.rotate3(AT=True)
            # Set all into default position and LG acts as "FG"
            self.set_default_position()
            self.LG.rotate(rotation)
            # Revert back to original orientation
            self.LG.move_out(AT=False)
            self.RG.move_out(AT=True)
            #
            self.UG.rotate3(AT=False)
            self.DG.rotate1(AT=True)
            #
            self.set_default_position()
            pass
        elif face == MO.Back:
            # Same as Front face but mirrored for cube rotation
            self.LG.move_out(AT=False)
            self.RG.move_out(AT=True)
            # Up and down moving Back to Left simultaneously
            self.UG.rotate3(AT=False)
            self.DG.rotate1(AT=True)
            # Set all into default position and LG acts as "BG"
            self.set_default_position()
            self.LG.rotate(rotation)
            # Revert back to original orientation
            self.LG.move_out(AT=False)
            self.RG.move_out(AT=True)
            # Rotate Back back to Back
            self.UG.rotate1(AT=False)
            self.DG.rotate3(AT=True)
            # Set Default position again
            self.set_default_position()
            pass
        else:
            raise RuntimeError('No face with index 6 or higher')

    def perform(self, list_of_moves):
        # List of moves is a list of strings of form '[Face][rotation]', e.g. 'L1', 'U3', etc.
        for i in list_of_moves:
            face = 0
            rotation = 0
            # Find which of MO i[0] equals and set the face to rotate, (WOULD LIKE TO REDUCE CODE)
            if i[0] in 'L':
                face = MO.Left
            elif i[0] in 'R':
                face = MO.Right
            elif i[0] in 'U':
                face = MO.Up
            elif i[0] in 'D':
                face = MO.Down
            elif i[0] in 'F':
                face = MO.Fight
            elif i[0] in 'B':
                face = MO.Back
            else:
                raise RuntimeError('Face of move-set not recognized:' + str(i))
            # Find desired rotation
            rotation = i[1]
            # and apply corresponding int of MO Face as face
            self.rotate(face, rotation)
