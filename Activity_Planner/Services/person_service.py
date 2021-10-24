from Activity_Planner.Repository.person_repository import PersonRepository
from Activity_Planner.Repository.person_text_files_repository import PersonTextFileRepository
from Activity_Planner.Repository.person_binary_files_repository import PersonBinaryFileRepository


class PersonService:
    def __init__(self, type_of_repo):
        if type_of_repo == "memory_repo":
            self.person = PersonRepository()
        elif type_of_repo == "text_repo":
            self.person = PersonTextFileRepository()
        elif type_of_repo == "binary_repo":
            self.person = PersonBinaryFileRepository()

    def add_person(self, person_id, name, phone_number):
        """
        This function adds a new person object in the _person_list
        :param person_id: the person_id given by the user
        :param name: the name given by the user
        :param phone_number: the phone_number given by the user
        :return: none
        """
        self.person.add_person(person_id, name, phone_number)

    def remove_person(self, person_id):
        """
        This function removes a person object from the _person_list
        :param person_id: the id of the person we want to remove from the list
        :return: none
        """
        self.person.remove_person(person_id)

    def update_person(self, person_id, new_person_id):
        """
        This function updates a person's id with a new one
        :param person_id: the person's id we want to update
        :param new_person_id: the new person's id
        :return: none
        """
        self.person.update_person(person_id, new_person_id)

    def return_person_list(self):
        """
        This function returns the transformed list of persons
        :return: the transformed list of persons
        """
        good_list = self.person.return_person_list()
        return good_list

    def is_person_id(self, the_id):
        """
        This functions checks whether an id is part of the person list or not
        :param the_id: the id to be checked
        :return: none
        """
        return self.person.is_person_id(the_id)

    def search_person_by_name(self, name):
        """
        This function searches for a person with a given name
        :param name: the name given by the user
        :return: the person(s) with that name
        """
        return self.person.search_person_by_name(name)

    def search_person_by_phone_number(self, phone_number):
        """
        This function searches for a person with a given phone_number
        :param phone_number: the phone_number given by the user
        :return: the person(s) with that phone_number
        """
        return self.person.search_person_by_phone_number(phone_number)