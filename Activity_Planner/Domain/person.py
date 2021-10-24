class Person:
    def __init__(self, person_id, name, phone_number):
        """
        The constructor of the class Person. We declare a person as an object with 3 parameters
        :param person_id: the person_id of the object
        :param name: the name of the object
        :param  phone_number: the person_number of the object
        """
        self._person_id = person_id
        self._name = name
        self._phone_number = phone_number

    @property
    def person_id(self):
        """
        :return: the person_id of the current object
        """
        return self._person_id

    @property
    def name(self):
        """
        :return: the name of the current object
        """
        return self._name

    @property
    def phone_number(self):
        """
        :return: the person_number of the current object
        """
        return self._phone_number

    @person_id.setter
    def person_id(self, other):
        """
        :param other: the person_id to be set
        :return: none
        """
        self._person_id = other

    @name.setter
    def name(self, other):
        """
        :param other: the name to be set
        :return: none
        """
        self._name = other

    @ phone_number.setter
    def phone_number(self, other):
        """
        :param other: the  phone_number to be set
        :return: none
        """
        self._phone_number = other
