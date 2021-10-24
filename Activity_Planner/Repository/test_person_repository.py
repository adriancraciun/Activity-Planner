from Activity_Planner.Repository.person_repository import PersonRepository
import unittest


class TestPersonRepository(unittest.TestCase):
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
        test_list = PersonRepository()
        test_list.add_person(1, "Norman Rockwell", "0760000001")
        test_list.add_person(2, "Salvador Dalí", "0760000002")
        test_list.add_person(3, "John Wayne", "0760000003")
        test_list.add_person(4, "NC Wyeth", "0760000004")
        test_list.add_person(5, "Andrew Loomis", "0760000005")

        test_list.remove_person(1)
        test_list.remove_person(2)
        test_list.remove_person(22)
        test_list.remove_person(0)
        test_list.remove_person(3)

        test_list.update_person(4, 6)
        test_list.update_person(1, 10)
        test_list.update_person(5, 1)


test_person_repo = TestPersonRepository()
test_person_repo.setUp()
test_person_repo.test_init()
test_person_repo.tearDown()
