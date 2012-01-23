#!/usr/bin/env python
import wpilib


"""!!!Definition of controls!!!
"""

lstick = wpilib.Joystick(1)

rstick = wpilib.Joystick(2)

leftFrontMotor = wpilib.CANJaguar(2)

leftRearMotor = wpilib.CANJaguar(7)

rightFrontMotor = wpilib.CANJaguar(4)

rightRearMotor = wpilib.CANJaguar(6)


drive = wpilib.RobotDrive(leftFrontMotor, leftRearMotor,

                          rightFrontMotor, rightRearMotor)


def checkRestart():

    if lstick.GetRawButton(10):

        raise RuntimeError("Restart")


def disabled():

    while wpilib.IsDisabled():

        checkRestart()


"""!!!Autonomous period of game play!!!
"""


def autonomous():

    wpilib.GetWatchdog().SetEnabled(False)

    while wpilib.IsAutonomous() and wpilib.IsEnabled():

        checkRestart()

        wpilib.Wait(0.01)




def teleop():
    """!!!Teleoperated period of game play!!!
    """

    dog = wpilib.GetWatchdog()

    dog.SetEnabled(True)

    dog.SetExpiration(0.25)

    shiftTime = wpilib.Timer()


    shiftTime.Start()


    while wpilib.IsOperatorControl() and wpilib.IsEnabled():

        dog.Feed()

        checkRestart()


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


        # Drive control
        drive.TankDrive(lstick, rstick)


        wpilib.Wait(0.04)


def run():


    """Main loop
    """


    while 1:

        if wpilib.IsDisabled():

            print("Running disabled()")

            disabled()

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
