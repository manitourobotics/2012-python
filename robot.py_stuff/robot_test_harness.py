import time
import unittest

"""
Goals: Write the testing system for tank drive & launcher (acquisition) by Wendsday.
"""


sys.path.append('../')
import robot_python_new as mod

def suite():

   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestTank))
   
   return suite


class TestTank(unittest.TestCase):
   

     def test_tank(self):
          self.assertTrue(1==1)


if __name__ == "__main__":

   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(suite())