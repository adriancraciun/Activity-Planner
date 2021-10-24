from Activity_Planner.Repository.person_repository import PersonRepository
import pickle


class PersonBinaryFileRepository(PersonRepository):
    def __init__(self, file_name='person.bin'):
        """
        The constructor of the Person Text File Repository
        :param file_name: the file name of the txt file repository
        """
        self._person = PersonRepository()
        self._file_name = file_name
        self.read_binary_file()

    @property
    def person_list(self):
        return self._person.person_list

    def add_person(self, person_id, name, phone_number):
        """
        This function adds a new person object in the _person_list
        :param person_id: the person_id given by the user
        :param name: the name given by the user
        :param phone_number: the phone_number given by the user
        :return: none
        """
        self._person.add_person(person_id, name, phone_number)
        self.write_binary_file()

    def remove_person(self, person_id):
        """
        This function removes a person object from the _person_list
        :param person_id: the id of the person we want to remove from the list
        :return: none
        """
        self._person.remove_person(person_id)
        self.write_binary_file()

    def update_person(self, person_id, new_person_id):
        """
        This function updates a person's id with a new one
        :param person_id: the person's id we want to update
        :param new_person_id: the new person's id
        :return: none
        """
        self._person.update_person(person_id, new_person_id)
        self.write_binary_file()

    def return_person_list(self):
        """
        This function returns the transformed list of persons
        :return: the transformed list of persons
        """
        return self._person.return_person_list()

    def is_person_id(self, the_id):
        """
        This functions checks whether an id is part of the person list or not
        :param the_id: the id to be checked
        :return: none
        """
        return self._person.is_person_id(the_id)

    def search_person_by_name(self, name):
        """
        This function searches for a person with a given name
        :param name: the name given by the user
        :return: the person(s) with that name
        """
        return self._person.search_person_by_name(name)

    def search_person_by_phone_number(self, phone_number):
        """
        This function searches for a person with a given phone_number
        :param phone_number: the phone_number given by the user
        :return: the person(s) with that phone_number
        """
        return self._person.search_person_by_phone_number(phone_number)

    def write_binary_file(self):
        """
        This functions saves the data in the binary file
        """
        # wb = write binary
        f = open(self._file_name, 'wb')
        pickle.dump(self._person, f)
        f.close()

    def read_binary_file(self):
        """
        This functions loads the data from the binary file
        """
        end_of_file_result = []
        try:
            f = open(self._file_name, 'rb')
            self._person = pickle.load(f)
            f.close()
            return self._person
        except EOFError:
            return end_of_file_result
        except IOError as e:
            raise e
