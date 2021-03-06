### THIS SCRIPT IS FOR PYTHON BOARD TO COMMS WITH ARDUINO THROUGH PULSES"""
import RPi.GPIO as GPIO
from enumsProj import Moves
import time

class ServoControl:
    """Class that communicates with Arduino to control servo-motors"""
    def __init__(self, channel_out=3, channel_in=5):
        self.channel_out = channel_out
        self.channel_in = channel_in
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel_out, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(channel_in, GPIO.IN)

    def solve(self, move_set):
        """Take the moveset and translates it to pulses for arduino to interpret"""
        for move in move_set:
            for member in Moves:
                if move == member.name:
                    self.pulse(member.value)
                    break

    def pulse(self, number_of_pulses):
        """Function that sends a number of pulses to the Arduino to make the desired move"""
        delay = number_of_pulses/2500
        for i in range(number_of_pulses):
            GPIO.output(self.channel_out, GPIO.HIGH)
            time.sleep(delay)
            GPIO.out(self.channel_out, GPIO.LOW)
            time.sleep(delay)
        # Pause until arduino sends message signaling it has completed move
        while GPIO.input(self.channel_in) == GPIO.LOW:
            time.sleep(0.1)

    def read(self):
        """Function that reads signal from arduino"""
        return bool(GPIO.input(self.channel_in))

    def start_sequence(self):
        """Starts the start sequence by having an 19 pulse sent to arduino"""
        self.pulse(19)

