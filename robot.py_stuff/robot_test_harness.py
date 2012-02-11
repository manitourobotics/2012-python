import robot_pthon_new.py
import time

"""
Goals: Write the testing system for tank drive & launcher by Wendsday. I should also get dad's example of one of his actual test harnesses
"""


sys.path.append('../')
import metadata  as mod

def suite():

   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestSchema))
   suite.addTest(unittest.makeSuite(TestStructType))
   suite.addTest(unittest.makeSuite(TestStruct))
   suite.addTest(unittest.makeSuite(TestElement))
   suite.addTest(unittest.makeSuite(TestReports))
   return suite

def test_tank(1):
     print 'Begining to test tank drive'
     time.wait (2.0)
     
     print 'Finished testing tank drive.'
           'The tank drive is reliable '%' percent of the time and failed '%' tests of the '%'

def test_launch(2):
     print 'Begining to test the launching system'
     time.wait (2.0)
     
     print 'Finished testing the launching system.'
           'The launching system is reliable '%' percent of the time and failed '%' tests of the '%'

def test_acquire(3):
     print 'Begining to test the acquisition system'
     time.wait (2.0)
     
     print 'Finished testing the acquisition system.'
           'The acquisition system is reliable '%' percent of the time and failed '%' tests of the '%'
           

if __name__ == "__main__":

   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(suite())