from Activity_Planner.Repository.activity_repository import ActivityRepository


class ActivityTextFileRepository(ActivityRepository):
    def __init__(self, file_name='activity.txt'):
        """
        The constructor of the Activity Text File Repository
        :param file_name: the file name of the txt file repository
        """
        self._activity = ActivityRepository()
        self._file_name = file_name
        self._load()

    @property
    def activity_list(self):
        return self._activity.activity_list

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
        self._activity.add_activity(activity_id, person_id, date, time, description)
        self._save()

    def remove_activity(self, activity_id):
        """
        This function removes an activity object from the _person_list
        :param activity_id: the activity_id of the activity we want to remove
        :return:
        """
        self._activity.remove_activity(activity_id)
        self._save()

    def update_activity(self, activity_id, new_activity_id):
        """
        This function updates an activity's id with a new one
        :param activity_id: the activity's id we want to update
        :param new_activity_id: the new activity's id
        :return: none
        """
        self._activity.update_activity(activity_id, new_activity_id)
        self._save()

    def return_activity_list(self):
        """
        This function returns the transformed list of activities
        :return: the transformed list of persons
        """
        return self._activity.return_activity_list()

    def _save(self):
        """
        This functions saves the data in the txt file
        """
        # wt = write text
        f = open(self._file_name, 'wt')
        activity_list = self._activity.activity_list
        for activity in activity_list:
            line = str(activity.activity_id) + ';' + str(activity.person_id) + ';' + str(activity.date) + ';' + \
                   str(activity.time) + ';' + str(activity.description)
            f.write(line)
            f.write('\n')
        f.close()

    def _load(self):
        """
        This functions loads the data from the txt file
        """
        # rt = read text
        f = open(self._file_name, 'rt')
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            if len(line) == 5:
                person_list = line[1].replace('[', '').replace(']', '').split(',')
                self._activity.add_activity(line[0], person_list, line[2], line[3], line[4])

