from Activity_Planner.Domain.activity import Activity
from Activity_Planner.Repository.activity_repository_exception import ActivityRepositoryException


def key_function(element):
    return element[3]


class ActivityRepository:
    def __init__(self):
        self._activity_list = []

    @property
    def activity_list(self):
        """
        :return: the _activity_list of the object
        """
        return self._activity_list

    def add_activity(self, activity_id, person_id, date, time, description):
        """
        This function adds a new activity object in the _activity_list
        :param activity_id: the activity_id given by the user
        :param person_id: the person_id given by the user
        :param date: the date given by the user
        :param time: the time given by the user
        :param description: the description given by the user
        :return: none
        """
        for activity in self._activity_list:
            if activity_id == activity.activity_id:
                raise ActivityRepositoryException("There is already an activity with that id in the list.")
            for person1 in person_id:
                for person2 in activity.person_id:
                    if int(person1) == int(person2):
                        if date == activity.date:
                            time_1 = time.split('-')
                            time_2 = activity.time.split('-')
                            if float(time_2[0]) <= float(time_1[0]) < float(time_2[1]) or \
                                    float(time_2[0]) < float(time_1[1]) <= float(time_2[1]) or \
                                    float(time_1[0]) <= float(time_2[0]) <= float(time_2[1]) <= float(time_1[1]):
                                print(activity_id, activity.activity_id)
                                raise ActivityRepositoryException("The person has another activity at that date "
                                                                  "and time.")

        self._activity_list.append(Activity(activity_id, person_id, date, time, description))

    def remove_activity(self, activity_id):
        """
        This function removes an activity object from the _person_list
        :param activity_id: the activity_id of the activity we want to remove
        :return:
        """
        deleted = False
        for activity in self._activity_list:
            if activity_id == activity.activity_id:
                deleted = True
                self._activity_list.remove(activity)
        if not deleted:
            raise ActivityRepositoryException("The activity id is not in the activity planner")

    def update_activity(self, activity_id, new_activity_id):
        """
        This function updates an activity's id with a new one
        :param activity_id: the activity's id we want to update
        :param new_activity_id: the new activity's id
        :return: none
        """
        for activity in self._activity_list:
            if new_activity_id == activity.activity_id:
                raise ActivityRepositoryException("There is already an activity with that id in the list.")

        for activity in self._activity_list:
            if activity_id == activity.activity_id:
                activity.activity_id = new_activity_id

    def return_activity_list(self):
        """
        This function returns the transformed list of activities
        :return: the transformed list of persons
        """
        good_list = []
        for activity in self._activity_list:
            activity_id = activity.activity_id
            person_id = activity.person_id
            date = activity.date
            time = activity.time
            description = activity.description
            good_list.append([activity_id, person_id, date, time, description])
        return good_list

    def remove_user_id(self, user_id):
        """
        This function removes an user id from the activity list
        :param user_id: the user id to be removed from the activity list
        :return: none
        """
        for activity in self._activity_list:
            activity.remove_id_from_person_id(user_id)

    def add_user_id(self, user_id, activity_id):
        """
        This function adds a user id to an activity id
        :param user_id: the user id to be added
        :param activity_id: the activity list where we put the user id
        :return: none
        """

        for activity in self._activity_list:
            if activity.activity_id == activity_id:
                activity.add_id_from_person_id(user_id)

    def is_activity_id(self, the_id):
        """
        This functions checks whether an id is part of the activity list or not
        :param the_id: the id to be checked
        :return: none
        """
        for activity in self._activity_list:
            if int(the_id) == int(activity.activity_id):
                return True
        return False

    def search_activity_by_date(self, date):
        """
        This function searches for an activity with a given date
        :param date: the date given by the user
        :return: the activity(activities) with that date
        """
        activity_list = []
        date = str(date)
        for activity in self._activity_list:
            if date.lower() in str(activity.date).lower():
                activity_list.append([activity.activity_id, activity.person_id, activity.date, activity.time,
                                      activity.description])
        return activity_list

    def search_activity_by_time(self, time):
        """
        This function searches for an activity with a given time
        :param time: the time given by the user
        :return: the activity(activities) with that time
        """
        activity_list = []
        time = str(time)
        for activity in self._activity_list:
            if time.lower() in str(activity.time).lower():
                activity_list.append([activity.activity_id, activity.person_id, activity.date, activity.time,
                                      activity.description])
        return activity_list

    def search_activity_by_description(self, description):
        """
        This function searches for an activity with a given description
        :param description: the description given by the user
        :return: the activity(activities) with that description
        """
        activity_list = []
        description = str(description)
        for activity in self._activity_list:
            if description.lower() in str(activity.description).lower():
                activity_list.append([activity.activity_id, activity.person_id, activity.date, activity.time,
                                      activity.description])
        return activity_list

    def statistics_given_date(self, date):
        """
        This function creates a statistic with a given date
        :param date: the date given by the user
        :return: the activity(activities) with that date sorted
        """
        activity_list = []
        for activity in self._activity_list:
            if date == activity.date:
                activity_list.append([activity.activity_id, activity.person_id, activity.date, activity.time,
                                      activity.description])

        activity_list.sort(key=key_function)
        return activity_list

    def statistics_busy_days(self, day):
        """
        This function creates a statistic with a given day for the busy days in that week
        :param day: the day given by the user
        :return: a characteristic sequence
        """
        activity_days_characteristics = []
        index = 1
        while index <= 7:
            consumed_time = 0
            for activity in self._activity_list:
                if day == activity.date:
                    time = activity.time
                    time = time.split('-')
                    consumed_time = float(time[1]) - float(time[0])
            activity_days_characteristics.append([index, consumed_time])
            index += 1

            string = day
            string = string.split('.')
            string[0] = int(string[0])
            string[0] += 1
            string[0] = str(string[0])
            day = string[0] + '.' + string[1] + '.' + string[2]

        return activity_days_characteristics

    def statistics_given_person(self, person):
        """
        This function creates a statistic with a given person for each day that he has activities
        :param person: the person id given by the user
        :return:
        """
        person_activities = []
        for activity in self._activity_list:
            for person_2 in activity.person_id:
                if int(person) == int(person_2):
                    person_activities.append([activity.activity_id, activity.person_id, activity.date, activity.time,
                                              activity.description])
        return person_activities
