from Activity_Planner.Domain.person import Person
from Activity_Planner.Repository.person_repository_exception import PersonRepositoryException


class PersonRepository:
    def __init__(self):
        self._person_list = []

    @property
    def person_list(self):
        """
        :return: the _person_list of the object
        """
        return self._person_list

    def add_person(self, person_id, name, phone_number):
        """
        This function adds a new person object in the _person_list
        :param person_id: the person_id given by the user
        :param name: the name given by the user
        :param phone_number: the phone_number given by the user
        :return: none
        """
        for person in self.person_list:
            if person_id == person.person_id:
                raise PersonRepositoryException("There is already a person with that id in the list.")
        self.person_list.append(Person(person_id, name, phone_number))

    def remove_person(self, person_id):
        """
        This function removes a person object from the _person_list
        :param person_id: the id of the person we want to remove from the list
        :return: none
        """
        deleted = False
        for person in self._person_list:
            if person_id == person.person_id:
                deleted = True
                self._person_list.remove(person)
        if not deleted:
            raise PersonRepositoryException("The activity id is not in the activity planner")

    def update_person(self, person_id, new_person_id):
        """
        This function updates a person's id with a new one
        :param person_id: the person's id we want to update
        :param new_person_id: the new person's id
        :return: none
        """
        for person in self.person_list:
            if new_person_id == person.person_id:
                raise PersonRepositoryException("There is already a person with that id in the list.")

        for person in self.person_list:
            if person_id == person.person_id:
                person.person_id = new_person_id

    def return_person_list(self):
        """
        This function returns the transformed list of persons
        :return: the transformed list of persons
        """
        good_list = []
        for person in self.person_list:
            person_id = person.person_id
            name = person.name
            phone_number = person.phone_number
            good_list.append([person_id, name, phone_number])
        return good_list

    def is_person_id(self, the_id):
        """
        This functions checks whether an id is part of the person list or not
        :param the_id: the id to be checked
        :return: none
        """
        for person in self._person_list:
            if int(the_id) == int(person.person_id):
                return True
        return False

    def search_person_by_name(self, name):
        """
        This function searches for a person with a given name
        :param name: the name given by the user
        :return: the person(s) with that name
        """
        person_list = []
        name = str(name)
        for person in self.person_list:
            if name.lower() in str(person.name).lower():
                person_list.append([person.person_id, person.name, person.phone_number])
        return person_list

    def search_person_by_phone_number(self, phone_number):
        """
        This function searches for a person with a given phone_number
        :param phone_number: the phone_number given by the user
        :return: the person(s) with that phone_number
        """
        person_list = []
        for person in self.person_list:
            if phone_number in person.phone_number:
                person_list.append([person.person_id, person.name, person.phone_number])
        return person_list
