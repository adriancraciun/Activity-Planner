from Activity_Planner.Repository.activity_repository import ActivityRepository
import pickle


class ActivityBinaryFileRepository(ActivityRepository):
    def __init__(self, file_name='activity.bin'):
        """
        The constructor of the Activity Text File Repository
        :param file_name: the file name of the txt file repository
        """
        self._activity = ActivityRepository()
        self._file_name = file_name
        self.read_binary_file()

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
        self.write_binary_file()

    def remove_activity(self, activity_id):
        """
        This function removes an activity object from the _person_list
        :param activity_id: the activity_id of the activity we want to remove
        :return:
        """
        self._activity.remove_activity(activity_id)
        self.write_binary_file()

    def update_activity(self, activity_id, new_activity_id):
        """
        This function updates an activity's id with a new one
        :param activity_id: the activity's id we want to update
        :param new_activity_id: the new activity's id
        :return: none
        """
        self._activity.update_activity(activity_id, new_activity_id)
        self.write_binary_file()

    def return_activity_list(self):
        """
        This function returns the transformed list of activities
        :return: the transformed list of persons
        """
        return self._activity.return_activity_list()

    def write_binary_file(self):
        """
        This functions saves the data in the binary file
        """
        # wt = write binary
        f = open(self._file_name, 'wb')
        pickle.dump(self._activity, f)
        #           self._activity.activity_list , f
        f.close()

    def read_binary_file(self):
        """
        This functions loads the data from the binary file
        """
        end_of_file_result = []
        try:
            f = open(self._file_name, 'rb')
            self._activity = pickle.load(f)
            f.close()
            return self._activity
        except EOFError:
            return end_of_file_result
        except IOError as e:
            raise e
