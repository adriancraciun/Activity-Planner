from Activity_Planner.Domain.activity import Activity
import unittest


class TestActivity(unittest.TestCase):
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
        This function checks if we can successfully declare objects with the class Activity
        :return: none
        """
        activity_list = []
        person_id_list = [1, 2, 3]
        activity = Activity(1, person_id_list, "12.12.2020", "20:00", "Creamfields Festival")
        this_person_list = activity.person_id
        activity_list.append(activity)
        activity_list.append(Activity(2, this_person_list, "11.11.2020", "18:00", "Sziget Festival"))
        activity_list.append(Activity(3, [7], "10.10.2020", "14:00", "EXIT Festival"))
        activity_list.append(Activity(4, [8, 9, 10], "16.09.2020", "19:30", "Tomorrowland Festival"))
        activity_list.append(Activity(5, [7, 6, 5], "16.09.2020", "23:00", "Download Festival"))
        activity_list.append(Activity(6, [5], "15.05.2020", "21:00", "Parklife Festival"))
        activity_list.append(Activity(7, [1, 9, 10], "16.12.2020", "22:00", "Awakenings Festival"))
        activity_list.append(Activity(8, [4, 2, 8], "01.07.2020", "23:30", "Coachella Festival"))


test = TestActivity()
test.setUp()
test.test_init()
test.tearDown()
