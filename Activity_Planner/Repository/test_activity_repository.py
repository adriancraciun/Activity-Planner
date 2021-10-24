from Activity_Planner.Repository.activity_repository import ActivityRepository
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
        test_list = ActivityRepository()
        test_list.add_activity(1, [0, 1], "12.12.2020", "20:00", "Creamfields Festival")
        test_list.add_activity(3, [7], "10.10.2020", "14:00", "EXIT Festival")
        test_list.add_activity(4, [8, 9, 10], "16.09.2020", "19:30", "Tomorrowland Festival")
        test_list.add_activity(5, [7, 6, 5], "16.09.2020", "23:00", "Download Festival")
        test_list.add_activity(6, [5], "15.05.2020", "21:00", "Parklife Festival")

        test_list.remove_activity(1)
        test_list.remove_activity(0)
        test_list.remove_activity(20)

        test_list.update_activity(1, 10)
        test_list.update_activity(3, 20)
        test_list.update_activity(0, 0)


test_activity_repo = TestActivityRepository()
test_activity_repo.setUp()
test_activity_repo.test_init()
test_activity_repo.tearDown()
