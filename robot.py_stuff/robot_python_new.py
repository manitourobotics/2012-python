#!/usr/bin/env python

import wpilib

"""Need to begin to get autonomous period of game play opporational. Should be done by Friday.
   The new test harness that I am writing should also be done by then.
"""

lstick = wpilib.Joystick(1)
rstick = wpilib.Joystick(2)
leftFrontMotor = wpilib.PWNJaguar(3)
leftRearMotor = wpilib.PWNaguar(4)
rightFrontMotor = wpilib.PWNJaguar(5)
rightRearMotor = wpilib.PWNJaguar(6)
rightTopMotor = wpilib.PWNJaguar(7)
leftTopMotor = wpilib.PWNJaguar(8)
LaunchMotor(1) = wpilib.PWNJaguar(9)
LaunchMotor(2) = wpilib.PWNJaguar(10)
ltrigger = wpilib.Trigger(1)
rtrigger = wpilib.Trigger(2)
lbumper = wpilib.Bumper(1)
rbumber = wpilib.Bumper(2)


def init():
    
    """Not necassarily important                     |
                                                     V
    """
    
    #Joystick(1) = [leftFrontMotor, leftBackMotor]
    #Joystick(2) = (rightFrontMotor, rightBackMotor)
    #JoystickTrigger(1) = [LaunchMotor(1), LaunchMotor(2)]
    #Trigger(1) = rightTopMotor
    #Trigger(2) = leftTopMotor
    #Bumper(1) = TopMotor
    #Bumper(2) = BottomMotor

    # Driving 
    drive = wpilib.RobotDrive(leftFrontMotor, leftRearMotor,
                              rightFrontMotor, rightRearMotor)
                          
    # Launching the ball 
    launch = wpilib.RobotLaunch(LaunchMotor(1), LaunchMotor(2))


def main():

    init()

    while True:

        if wpilib.IsDisabled():
            print("Running wait function")
            wait_for_restart_or_healthy_state()
            while wpilib.IsDisabled():
                wpilib.Wait(0.01)
        elif wpilib.IsAutonomous():
            print("Running autonomous()")
            autonomous()
            while wpilib.IsAutonomous() and wpilib.IsEnabled():
                wpilib.Wait(0.01)
        else:
            print("Running teleop()")
            teleop()
            while wpilib.IsOperatorControl() and wpilib.IsEnabled():
                wpilib.Wait(0.01)


def check_restart_button():
    """ Allows user to remotely trigger a restart
    """
    if lstick.GetRawButton(10):
        raise RuntimeError("Restart")


def wait_for_restart_or_healthy_state():
    """ keep checking to see if user wants to restart
        If user hits restart button it will cause an exception
    """
    while wpilib.IsDisabled():
        check_restart_button()

def autonomous():

    wpilib.GetWatchdog().SetEnabled(False)
    while wpilib.IsAutonomous() and wpilib.IsEnabled():
        check_restart_button()
        wpilib.Wait(0.01)


def teleop():

    dog = wpilib.GetWatchdog()
    dog.SetEnabled(True)
    dog.SetExpiration(0.25)
    shiftTime = wpilib.Timer()

    shiftTime.Start()


    while wpilib.IsOperatorControl() and wpilib.IsEnabled():

        dog.Feed()
        check_restart_button()


        if shiftTime.Get() > 0.3:
            shifter1.Set(False)
            shifter2.Set(False)

        # Shifter control 

        if rstick.GetTrigger():
            shifter1.Set(True)
            shifter2.Set(False)
            shiftTime.Reset()
            highGear = True
        elif lstick.GetTrigger():
            shifter1.Set(False)
            shifter2.Set(True)
            shiftTime.Reset()
            highGear = False

        drive.TankDrive(lstick, rstick)

        wpilib.Wait(0.04)




if __name__ == '__main__':
   main()
