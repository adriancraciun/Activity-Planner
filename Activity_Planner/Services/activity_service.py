from Activity_Planner.Repository.activity_repository import ActivityRepository
from Activity_Planner.Repository.activity_text_files_repository import ActivityTextFileRepository
from Activity_Planner.Repository.activity_binary_files_repository import ActivityBinaryFileRepository


class ActivityService:
    def __init__(self, type_of_repo):
        if type_of_repo == "memory_repo":
            self.activity = ActivityRepository()
        elif type_of_repo == "text_repo":
            self.activity = ActivityTextFileRepository()
        elif type_of_repo == "binary_repo":
            self.activity = ActivityBinaryFileRepository()

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
        self.activity.add_activity(activity_id, person_id, date, time, description)

    def remove_activity(self, activity_id):
        """
        This function removes an activity object from the _person_list
        :param activity_id: the activity_id of the activity we want to remove
        :return:
        """
        self.activity.remove_activity(activity_id)

    def update_activity(self, activity_id, new_activity_id):
        """
       This function updates an activity's id with a new one
       :param activity_id: the activity's id we want to update
       :param new_activity_id: the new activity's id
       :return: none
       """
        self.activity.update_activity(activity_id, new_activity_id)

    def return_activity_list(self):
        """
        This function returns the transformed list of activities
        :return: the transformed list of persons
        """
        good_list = self.activity.return_activity_list()
        return good_list

    def remove_user_id(self, user_id):
        """
        This function removes an user id from the activity list
        :param user_id:
        :return: none
        """
        self.activity.remove_user_id(user_id)

    def add_user_id(self, user_id, activity_id):
        """
        This function adds a user id to an activity id
        :param user_id: the user id to be added
        :param activity_id: the activity list where we put the user id
        :return: none
        """
        self.activity.add_user_id(user_id, activity_id)

    def is_activity_id(self, the_id):
        """
        This functions checks whether an id is part of the activity list or not
        :param the_id: the id to be checked
        :return: none
        """
        return self.activity.is_activity_id(the_id)

    def search_activity_by_date(self, date):
        """
        This function searches for an activity with a given date
        :param date: the date given by the user
        :return: the activity(activities) with that date
        """
        return self.activity.search_activity_by_date(date)

    def search_activity_by_time(self, time):
        """
        This function searches for an activity with a given time
        :param time: the time given by the user
        :return: the activity(activities) with that time
        """
        return self.activity.search_activity_by_time(time)

    def search_activity_by_description(self, description):
        """
        This function searches for an activity with a given description
        :param description: the description given by the user
        :return: the activity(activities) with that description
        """
        return self.activity.search_activity_by_description(description)

    def statistics_given_date(self, date):
        """
        This function creates a statistic with a given date
        :param date: the date given by the user
        :return: the activity(activities) with that date sorted
        """
        return self.activity.statistics_given_date(date)

    def statistics_busy_days(self, day):
        """
        This function creates a statistic with a given day for the busy days in that week
        :param day: the day given by the user
        :return: a characteristic sequence
        """
        return self.activity.statistics_busy_days(day)

    def statistics_given_person(self, person):
        """
        This function creates a statistic with a given person for each day that he has activities
        :param person: the person id given by the user
        :return:
        """
        return self.activity.statistics_given_person(person)
