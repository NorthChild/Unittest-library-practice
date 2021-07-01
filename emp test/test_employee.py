# to run this test, download both scripts in a folder, 'cd' to the folder containing both downloaded scripts, 
# when you have changed directory to the folder, run this on your command line 'python test_employee.py', 
# make sure both scripts are in the same folder

import unittest
from unittest.mock import patch
from employee import Employee



class TestEmployee( unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('\nSetupClass\n')

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass\n')

    def setUp(self):
        self.emp_1 = Employee('Mike', 'Wazoski', 50000)
        self.emp_2 = Employee('Carla', 'Baduski', 60000)

    def tearDown(self):
        pass



    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Mike.Wazoski@email.com')
        self.assertEqual(self.emp_2.email, 'Carla.Baduski@email.com')

        self.emp_1.first = 'Nick'
        self.emp_2.first = 'Mia'

        self.assertEqual(self.emp_1.email, 'Nick.Wazoski@email.com')
        self.assertEqual(self.emp_2.email, 'Mia.Baduski@email.com')


    def test_fullnam(self):

        self.assertEqual(self.emp_1.fullname, 'Mike Wazoski')
        self.assertEqual(self.emp_2.fullname, 'Carla Baduski')

        self.emp_1.first = 'Nick'
        self.emp_2.first = 'Mia'

        self.assertEqual(self.emp_1.fullname, 'Nick Wazoski')
        self.assertEqual(self.emp_2.fullname, 'Mia Baduski')


    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    def test_monthly_schedule(self):

        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Wazoski/May')
            self.assertEqual(schedule, 'Success!')

            mocked_get.return_value.ok = False
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Baduski/June')
            self.assertEqual(schedule, 'Bad response!')





if __name__ == '__main__':
    unittest.main()
