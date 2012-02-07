
import wpilib


"""
!!!Definition of controls!!! |
                             V
"""

lstick = wpilib.Joystick(1)

rstick = wpilib.Joystick(2)

leftFrontMotor = wpilib.CANJaguar(3)

leftRearMotor = wpilib.CANJaguar(4)

rightFrontMotor = wpilib.CANJaguar(5)

rightRearMotor = wpilib.CANJaguar(6)

rightTopMotor = wpilib.CANJaguar(7)

leftTopMotor = wpilib.CANJaguar(8)

TopMotor = wpilib.CANJaguar(9)

BottomMotor = wpilib.CANJaguar(10)

ltrigger = wpilib.Trigger(1)

rtrigger = wpilib.Trigger(2)

lbumper = wpilib.Bumper(1)

rbumber = wpilib.Bumper(2)

"""
not sure if needed (yet) |
                         V
"""

abutton = wpilib.

bbutton = wpilib.

xbutton = wpilib.

ybutton = wpilib.

"""
not sure if needed (yet) |
                         V
"""

padup = wpilib.

paddown = wpilib.

padleft = wpilib.

padright = wpilib.

"""
Definintly needed |
                  V
"""

Joystick(1) = leftFrontMotor, leftBackMotor

Joystick(2) = rightFrontMotor, rightBackMotor

JoystickTrigger(1) = LaunchMotor(1), LaunchMotor(2)

Trigger(1) = rightTopMotor

Trigger(2) = leftTopMotor

Bumper(1) = TopMotor

Bumper(2) = BottomMotor

"""
Driving |
        V
"""

drive = wpilib.RobotDrive(leftFrontMotor, leftRearMotor,

                          rightFrontMotor, rightRearMotor)
                          
"""
Launching the ball |
                   V
"""

launch = wpilib.RobotLaunch(LaunchMotor(1), LaunchMotor(2))


def checkRestart():

    if lstick.GetRawButton(10):

        raise RuntimeError("Restart")


def disabled():

    while wpilib.IsDisabled():

        checkRestart()

"""
!!!Autonomous period of game play!!! |
                                     V
"""

def autonomous():

    wpilib.GetWatchdog().SetEnabled(False)

    while wpilib.IsAutonomous() and wpilib.IsEnabled():

        checkRestart()

        wpilib.Wait(0.01)

"""
!!!Teleoperated period of game play!!! |
                                       V
"""

def teleop():

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

        """
        Shifter control |
                        V
        """

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

        """
        Drive Control |
                      V
        """
        
        drive.TankDrive(lstick, rstick)


        wpilib.Wait(0.04)

"""
Main Run |
         V
"""

def run():

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
