#!/usr/bin/env python

import sys
import time
import unittest
import pygame

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
   
   
   def test_launch(self):
      self.assertTrue(1==1)


if __name__ == "__main__":

   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(suite())
