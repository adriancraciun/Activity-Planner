from Activity_Planner.Repository.person_repository import PersonRepository


class PersonTextFileRepository(PersonRepository):
    def __init__(self, file_name="person.txt"):
        """
        The constructor of the Person Text File Repository
        :param file_name: the file name of the txt file repository
        """
        self._person = PersonRepository()
        self._file_name = file_name
        self._load()

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
        self._save()

    def remove_person(self, person_id):
        """
        This function removes a person object from the _person_list
        :param person_id: the id of the person we want to remove from the list
        :return: none
        """
        self._person.remove_person(person_id)
        self._save()

    def update_person(self, person_id, new_person_id):
        """
        This function updates a person's id with a new one
        :param person_id: the person's id we want to update
        :param new_person_id: the new person's id
        :return: none
        """
        self._person.update_person(person_id, new_person_id)
        self._save()

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

    def _load(self):
        """
        This functions loads the data from the txt file
        """
        f = open(self._file_name, 'rt')
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            if len(line) == 3:
                self._person.add_person(line[0], line[1], line[2])

    def _save(self):
        """
        This functions saves the data in the txt file
        """
        # wt = write text
        f = open(self._file_name, 'wt')
        person_list = self._person.person_list
        for person in person_list:
            line = str(person.person_id) + ';' + str(person.name) + ';' + str(person.phone_number)
            f.write(line)
        f.close()
