class Activity:
    def __init__(self, activity_id, person_id, date, time, description):
        """
        The constructor of the class Activity. We declare an activity as an object with 5 parameters
        :param activity_id: the activity_id of the object
        :param person_id: the list person_id of the object
        :param date: the date of the object
        :param time: the time of the object
        :param description: the description of the object
        """
        self._activity_id = activity_id
        self._person_id = person_id
        self._date = date
        self._time = time
        self._description = description

    @property
    def activity_id(self):
        """
        :return: the activity_id of the current object
        """
        return self._activity_id

    @property
    def person_id(self):
        """
        :return: the person_id list of the current object
        """
        return self._person_id

    @property
    def date(self):
        """
        :return: the date of the current object
        """
        return self._date

    @property
    def time(self):
        """
        :return: the time of the current object
        """
        return self._time

    @property
    def description(self):
        """
        :return: the description of the current object
        """
        return self._description

    @activity_id.setter
    def activity_id(self, other):
        """
        :param other: the activity_id to be set
        :return: none
        """
        self._activity_id = other

    @person_id.setter
    def person_id(self, other):
        """
        :param other: the person_id to be set
        :return: none
        """
        self._person_id = other

    @date.setter
    def date(self, other):
        """
        :param other: the date to be set
        :return: none
        """
        self._date = other

    @time.setter
    def time(self, other):
        """
        :param other: the time to be set
        :return: none
        """
        self._time = other

    @description.setter
    def description(self, other):
        """
        :param other: the description to be set
        :return: none
        """
        self._description = other

    def remove_id_from_person_id(self, person_index):
        person_index = int(person_index)
        for each_id in self._person_id:
            if each_id == person_index:
                self._person_id.remove(person_index)

    def add_id_from_person_id(self, person_index):
        person_index = int(person_index)
        self._person_id.append(person_index)
