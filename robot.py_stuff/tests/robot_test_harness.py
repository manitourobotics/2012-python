#!/usr/bin/env python

import sys
import time
import unittest
import pygame

screen = pygame.display.set_mode((640, 400))
running = 1

while running:
   event = pygame.event.poll()
   if event.type == pygame.QUIT:
      running = 0
   screen.fill((255, 255, 255))
   pygame.display.flip()

"""
Goals: Write the testing system for tank drive & launcher (acquisition) by Wendsday.
"""


sys.path.append('../')
import robot_python_new as mod

def suite():

   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestTank))
   suite.addTest(unittest.makesuite(TestLaunch))
   
   return suite

#Tank Tester
class TestTank(unittest.TestCase):
   

     def test_tank(self):
          self.assertTrue(1==1)
          
#Launch Tester
class TestLaunch(unittest.TestCase):
   #get pygame.Joystick
   
   def test_launch(self):
      self.assertTrue(1==1)


if __name__ == "__main__":

   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(suite())
