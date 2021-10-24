from Activity_Planner.Domain.person import Person
import unittest


class TestPerson(unittest.TestCase):
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
        This function checks if we can successfully declare objects with the class Person
        :return: none
        """
        person_list = []
        person = Person(1, "Tyler Joseph", "0760000001")
        person_list.append(person)
        person_list.append(Person(2, "Jesse Rutherford", "0760000002"))
        person_list.append(Person(3, "Brendon Urie", "0760000003"))
        person_list.append(Person(4, "Patrick Stump", "0760000004"))
        person_list.append(Person(5, "Yungblud", "0760000005"))
        person_list.append(Person(6, "Dan Reynolds", "0760000006"))
        person_list.append(Person(7, "Alex Turner", "0760000007"))
        person_list.append(Person(8, "Machine Gun Kelly", "0760000008"))
        person_list.append(Person(9, "Matthew Healy", "0760000009"))


test = TestPerson()
test.setUp()
test.test_init()
test.tearDown()
