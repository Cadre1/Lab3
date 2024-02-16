"""! @file encoder_reader.py
This program creates the class "Encoder" which initializes the timers/counters required for the encoder using provided channel pins and a timer/counter.
This class also contains the ability to set the read the overall motor position (being able to bypass overflow and underflow), and is able to zero at any position.
"""
import utime

class MotorControl:
    """! 

    """
    def __init__(self, setpoint, Kp):
        self.times = []
        self.positions = []
        self.setpoint = setpoint
        self.Kp = Kp
    
    
    def run(self, measured_output):
        time = utime.ticks_ms()
        self.times.append(time)
        self.positions.append(measured_output)
        
        error = self.setpoint - measured_output
        output = self.Kp*error
        return output
    
    
    def set_setpoint(self, setpoint):
        self.setpoint = setpoint
        
        
    def set_Kp(self, Kp):
        self.Kp = Kp
        
        
    def print_step_response(self, start_time):
        for i in range(len(self.times)):
            print(f"{self.times[i]-start_time}, {self.positions[i]}")
    
        