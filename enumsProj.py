# HOLDS ALL ENUMERATIONS FOR THE PROJEC
from enum import IntEnum


class MotorOrientations(IntEnum):
    """Orientations of motors to be used in all instances they are needed"""
    Up = 0
    Left = 1
    Down = 2
    Right = 3
    Front = 4
    Back = 5


class MoverPosition(IntEnum):
    """Position of movers to be used in all instances they are needed"""
    In = 0
    Out = 1


class RotatorPosition(IntEnum):
    """Position of rotators to be used in all instances they are needed"""
    Vertical = 0
    Horizontal = 1


class GripperPosition(IntEnum):
    """Position of gripper"""
    Vert_In = 0
    Vert_Out = 1
    Horiz_In = 2
    Horiz_Out = 3


class Drivers(IntEnum):
    """Driver number"""
    driver1 = 0     # Left and Up
    driver2 = 1     # Right and Down


class SwitchStates(IntEnum):
    LRM = 0     # Left, Right Movers
    LRR = 1     # Left, Right Rotators
    UDM = 2     # Up, Down Movers
    UDR = 3     # Up, Down Rotators
