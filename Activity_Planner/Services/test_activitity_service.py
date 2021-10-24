from Activity_Planner.Services.activity_service import ActivityService
import unittest


class TestActivityRepository(unittest.TestCase):
    def setUp(self):
        """"
        This function is called before any test cases.
        We can add initialization code common to all methods here.
       """
        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        This function is called after all test function are executed
        """
        unittest.TestCase.tearDown(self)

    def test_init(self):
        """
        This function checks if we can successfully declare objects with the class PersonRepository and its
        functionalities
        :return: none
        """
        test_list = ActivityService()
        test_list.add_activity(1, [50, 51], "12.12.2020", "20:00", "Creamfields Festival")
        test_list.add_activity(3, [52], "10.10.2020", "14:00", "EXIT Festival")
        test_list.add_activity(4, [53, 54, 55], "16.09.2020", "19:30", "Tomorrowland Festival")
        test_list.add_activity(5, [56, 57, 58], "16.09.2020", "23:00", "Download Festival")
        test_list.add_activity(6, [59], "15.05.2020", "21:00", "Parklife Festival")

        test_list.remove_activity(3)

        test_list.update_activity(1, 10)
        test_list.update_activity(3, 20)
        test_list.update_activity(10, 40)


test_activity_repo = TestActivityRepository()
test_activity_repo.setUp()
test_activity_repo.test_init()
test_activity_repo.tearDown()
