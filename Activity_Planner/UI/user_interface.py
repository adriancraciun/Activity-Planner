from Activity_Planner.Services.activity_service import ActivityService
from Activity_Planner.Services.person_service import PersonService
from Activity_Planner.Repository.person_repository_exception import PersonRepositoryException
from Activity_Planner.Repository.activity_repository_exception import ActivityRepositoryException
from Activity_Planner.Services.undo_service import UndoService, Operation, FunctionCall
from configparser import ConfigParser
import sys
import random


def my_key(element):
    return element[1]


class UI:
    def __init__(self, type_of_rep):
        self._person_list_ui = PersonService(type_of_rep)
        self._activity_list_ui = ActivityService(type_of_rep)
        self._undo_service = UndoService()

    def property_a_ui(self):
        person_id = input("Choose an ID for the person: ")
        name = input("Choose a name for the person: ")
        phone_number = input("Choose a phone number for the person: ")
        try:
            self._person_list_ui.add_person(person_id, name, phone_number)
            undo_fun = FunctionCall(self._person_list_ui.remove_person, person_id)
            redo_fun = FunctionCall(self._person_list_ui.add_person, person_id, name, phone_number)
            operation = Operation(undo_fun, redo_fun)
            self._undo_service.record(operation)
        except PersonRepositoryException as e:
            print(e)

    def property_b_ui(self):
        person_id = input("Choose an ID you want to remove from the person list: ")
        person_name = ""
        person_number = ""
        try:
            repo = self._person_list_ui.person.person_list
            for person in repo:
                if person.person_id == person_id:
                    person_name = person.name
                    person_number = person.phone_number
            self._person_list_ui.remove_person(person_id)
            undo_fun = FunctionCall(self._person_list_ui.add_person, person_id, person_name, person_number)
            redo_fun = FunctionCall(self._person_list_ui.remove_person, person_id)
            o = Operation(undo_fun, redo_fun)
            self._undo_service.record(o)
        except PersonRepositoryException:
            print("Invalid input for the remove_person functionality. \n"
                  "The person id is not in the activity planner \n")

    def property_c_ui(self):
        person_id = input("Choose an ID you want to update from the person list: ")
        new_person_id = input("Choose a new ID: ")
        try:
            self._person_list_ui.update_person(person_id, new_person_id)
            undo_fun = FunctionCall(self._person_list_ui.update_person, new_person_id, person_id)
            redo_fun = FunctionCall(self._person_list_ui.update_person, person_id, new_person_id)
            operation = Operation(undo_fun, redo_fun)
            self._undo_service.record(operation)
        except PersonRepositoryException:
            print("Invalid input for the update functionality. \n"
                  "There's already a person with a similar id in the activity planner. \n")

    def property_d_ui(self):
        my_list = self._person_list_ui.return_person_list()
        for person in my_list:
            print(person[1], "has the ID:", person[0], "and their phone number is:", person[2])

    def property_e_ui(self):
        activity_id = input("Choose an ID for the activity: ")
        person_id = input("Choose some persons IDs for the activity: ")
        date = input("Choose a date for the activity: ")
        time = input("Choose a time for the activity: ")
        description = input("Choose a description for the activity: ")
        person_id = person_id.split()
        i = 0
        while i < len(person_id):
            person_id[i] = int(person_id[i])
            i += 1
        try:
            self._activity_list_ui.add_activity(activity_id, person_id, date, time, description)
            undo_fun = FunctionCall(self._activity_list_ui.remove_activity, activity_id)
            redo_fun = FunctionCall(self._activity_list_ui.add_activity, activity_id, person_id, date, time,
                                    description)
            o = Operation(undo_fun, redo_fun)
            self._undo_service.record(o)
        except ActivityRepositoryException:
            print("Invalid input for the add_activity functionality. \n"
                  "Either there's already an activity id similar in the activity planner or one of the persons "
                  "you have input has another activity in that date. \n")

    def property_f_ui(self):
        activity_id = input("Choose an ID you want to remove from the activity list: ")
        person_id = []
        date = ""
        time = ""
        description = ""
        try:
            activity = self._activity_list_ui.activity  # the service
            repo = activity.activity_list  # the repo
            for activity in repo:
                if activity.activity_id == activity_id:
                    person_id = activity.person_id
                    date = activity.date
                    time = activity.time
                    description = activity.description
            self._activity_list_ui.remove_activity(activity_id)
            undo_fun = FunctionCall(self._activity_list_ui.add_activity, activity_id, person_id, date, time,
                                    description)
            redo_fun = FunctionCall(self._activity_list_ui.remove_activity, activity_id)
            o = Operation(undo_fun, redo_fun)
            self._undo_service.record(o)
        except ActivityRepositoryException:
            print("Invalid input for the remove_activity functionality. \n"
                  "The activity id is not in the activity planner \n")

    def property_g_ui(self):
        activity_id = input("Choose an ID you want to update from the activity list: ")
        new_person_id = input("Choose a new ID: ")
        try:
            self._activity_list_ui.update_activity(activity_id, new_person_id)
            undo_fun = FunctionCall(self._activity_list_ui.update_activity, new_person_id, activity_id)
            redo_fun = FunctionCall(self._activity_list_ui.update_activity, activity_id, new_person_id)
            o = Operation(undo_fun, redo_fun)
            self._undo_service.record(o)
        except ActivityRepositoryException:
            print("Invalid input for the update functionality. \n"
                  "There's already an activity with a similar id in the activity planner. \n")

    def property_h_ui(self):
        my_list = self._activity_list_ui.return_activity_list()
        for activity in my_list:
            print("The persons with the IDS:", activity[1], "will attend to the activity", activity[0],
                  activity[4], "in the date", activity[2], "at the time", activity[3])

    def property_i_ui(self):
        is_in_list = False
        user_id = input("Choose a person ID in the person list: ")
        new_activity_id = input("Choose an activity ID in the activity list: ")
        # We check if the person id is in the person_list
        if not self._person_list_ui.is_person_id(user_id):
            print("The person id you input is not part of the list.")
        # We check if the activity id is in the activity_list
        if not self._activity_list_ui.is_activity_id(new_activity_id):
            print("The activity id you input is not part of the list.")
        # We check if the person is in another activity in the list.
        # If so, we remove that person for that activity
        self._activity_list_ui.remove_user_id(user_id)
        # We put the id in the other activity
        self._activity_list_ui.add_user_id(user_id, new_activity_id)

    def property_j_ui(self):
        user_id = input("Choose a person ID in the person list: ")
        self._activity_list_ui.remove_user_id(user_id)

    def property_k_ui(self):
        the_name = input("Choose a name to search for: ")
        person_list = self._person_list_ui.search_person_by_name(the_name)
        for person in person_list:
            print("The person", person[1], "has the id", person[0], "and the phone number", person[2])

    def property_l_ui(self):
        the_phone_number = input("Choose a phone number to search for: ")
        person_list = self._person_list_ui.search_person_by_phone_number(the_phone_number)
        for person in person_list:
            print("The person", person[1], "has the id", person[0], "and the phone number", person[2])

    def property_m_ui(self):
        the_date = input("Choose a date to search for: ")
        activity_list = self._activity_list_ui.search_activity_by_date(the_date)
        for activity in activity_list:
            print("The persons with the IDS:", activity[1], "will attend to the activity", activity[0],
                  activity[4], "in the date", activity[2], "at the time", activity[3])

    def property_n_ui(self):
        the_time = input("Choose a time to search for: ")
        activity_list = self._activity_list_ui.search_activity_by_time(the_time)
        for activity in activity_list:
            print("The persons with the IDS:", activity[1], "will attend to the activity", activity[0],
                  activity[4], "in the date", activity[2], "at the time", activity[3])

    def property_o_ui(self):
        the_description = input("Choose a description to search for: ")
        activity_list = self._activity_list_ui.search_activity_by_description(the_description)
        for activity in activity_list:
            print("The persons with the IDS:", activity[1], "will attend to the activity", activity[0],
                  activity[4], "in the date", activity[2], "at the time", activity[3])

    def property_p_ui(self):
        given_date = input("Choose a date in order to see its statistics: ")
        activity_list = self._activity_list_ui.statistics_given_date(given_date)
        for activity in activity_list:
            print("The persons with the IDS:", activity[1], "will attend to the activity", activity[0],
                  activity[4], "in the date", activity[2], "at the time", activity[3])

    def property_q_ui(self):
        given_day = input("Choose a date in order to see the next week's statistics: ")
        activity_characteristic_list = self._activity_list_ui.statistics_busy_days(given_day)
        activity_characteristic_list.sort(key=my_key)
        for activity in activity_characteristic_list:
            print("For the day", activity[0], "we have", 24 - activity[1], "hours of unoccupied time!")

    def property_r_ui(self):
        given_person_id = input("Choose a person id in order to see their activities' statistics: ")
        person_activities = self._activity_list_ui.statistics_given_person(given_person_id)
        for activity in person_activities:
            print("The person with the id", given_person_id, "will participate at the activity",
                  activity[0], activity[4], "in the date", activity[2],
                  "at the time", activity[3])

    @staticmethod
    def print_menu():
        print("\n"
              "Press A in order to add a person to the list of persons. \n"
              "Press B in order to remove a person from the list of persons. \n"
              "Press C in order to update a given person ID with a new one \n"
              "Press D in order to list all persons in the list \n"
              "\n"
              "Press E in order to add an activity to the list of activities.\n"
              "Press F in order to remove an activity from the list of activities. \n"
              "Press G in order to update a given activity ID with a new one. \n"
              "Press H in order to list all activities in the list. \n"
              "\n"
              "Press K in order to search for a person by their name. \n"
              "Press L in order to search for a person by their phone number. \n"
              "Press M in order to search for an activity by its date. \n"
              "Press N in order to search for an activity by its time. \n"
              "Press O in order to search for an activity by its description. \n"
              "\n"
              "Press P in order to create a statistic for a date: \n"
              "Press Q in order to create a statistic for the next week: \n"
              "Press R in order to create a statistic for a given person id: \n"
              "\n"
              "Press S in order to undo the last operation. \n"
              "Press T in order to redo the last operation. \n"
              "\n"
              "Press Z in order to exit the program. \n")

    def start(self):
        # self.test_init()
        while True:
            self.print_menu()
            command = input("Choose a command from the command menu: ")
            if command == 'A' or command == 'a':
                self.property_a_ui()
            elif command == 'B' or command == 'b':
                self.property_b_ui()
            elif command == 'C' or command == 'c':
                self.property_c_ui()
            elif command == 'D' or command == 'd':
                self.property_d_ui()
            elif command == 'E' or command == 'e':
                self.property_e_ui()
            elif command == 'F' or command == 'f':
                self.property_f_ui()
            elif command == 'G' or command == 'g':
                self.property_g_ui()
            elif command == 'H' or command == 'h':
                self.property_h_ui()
            elif command == 'I' or command == 'i':
                self.property_i_ui()
            elif command == 'J' or command == 'j':
                self.property_j_ui()
            elif command == 'K' or command == "k":
                self.property_k_ui()
            elif command == 'L' or command == 'l':
                self.property_l_ui()
            elif command == 'M' or command == 'm':
                self.property_m_ui()
            elif command == 'N' or command == 'n':
                self.property_n_ui()
            elif command == 'O' or command == 'o':
                self.property_o_ui()
            elif command == 'P' or command == 'p':
                self.property_p_ui()
            elif command == 'Q' or command == 'q':
                self.property_q_ui()
            elif command == 'R' or command == 'r':
                self.property_r_ui()
            elif command == 'S' or command == 's':
                self._undo_service.undo()
            elif command == 'T' or command == 't':
                self._undo_service.redo()
            elif command == 'Z' or command == 'z':
                sys.exit()
            else:
                print("The command you have chosen is not in the menu.")

    def test_init(self):
        person1_id = str(random.randint(100, 100000))

        person2_id = str(random.randint(100, 100000))
        while person2_id == person1_id:
            person2_id = str(random.randint(100, 100000))

        person3_id = str(random.randint(100, 100000))
        while person3_id == person1_id or person3_id == person2_id:
            person3_id = str(random.randint(100, 100000))

        person4_id = str(random.randint(100, 100000))
        while person4_id == person3_id or person4_id == person2_id or person4_id == person1_id:
            person4_id = str(random.randint(100, 100000))

        person5_id = str(random.randint(100, 100000))
        while person5_id == person4_id or person5_id == person3_id or person5_id == person2_id \
                or person5_id == person1_id:
            person5_id = str(random.randint(100, 100000))

        person6_id = str(random.randint(100, 100000))
        while person6_id == person5_id or person6_id == person4_id or person6_id == person3_id \
                or person6_id == person2_id or person6_id == person1_id:
            person6_id = str(random.randint(100, 100000))

        person7_id = str(random.randint(100, 100000))
        while person7_id == person6_id or person7_id == person5_id or person7_id == person4_id \
                or person7_id == person3_id or person7_id == person2_id or person7_id == person1_id:
            person7_id = str(random.randint(100, 100000))

        person8_id = str(random.randint(100, 100000))
        while person8_id == person6_id or person8_id == person5_id or person8_id == person4_id \
                or person8_id == person3_id or person8_id == person2_id or person8_id == person1_id \
                or person8_id == person7_id:
            person8_id = str(random.randint(100, 100000))

        person9_id = str(random.randint(100, 100000))
        while person9_id == person6_id or person9_id == person5_id or person9_id == person4_id \
                or person9_id == person3_id or person9_id == person2_id or person9_id == person1_id \
                or person9_id == person7_id or person9_id == person8_id:
            person9_id = str(random.randint(100, 100000))

        person10_id = str(random.randint(100, 100000))
        while person10_id == person6_id or person10_id == person5_id or person10_id == person4_id \
                or person10_id == person3_id or person10_id == person2_id or person10_id == person1_id \
                or person10_id == person7_id or person10_id == person8_id or person10_id == person9_id:
            person10_id = str(random.randint(100, 100000))

        self._person_list_ui.add_person(person1_id, "Tyler Joseph", "0760000001")
        self._person_list_ui.add_person(person2_id, "Jesse Rutherford", "0760000002")
        self._person_list_ui.add_person(person3_id, "Brendon Urie", "0760000003")
        self._person_list_ui.add_person(person4_id, "Patrick Stump", "0760000004")
        self._person_list_ui.add_person(person5_id, "Yungblud", "0760000005")
        self._person_list_ui.add_person(person6_id, "Dan Reynolds", "0760000006")
        self._person_list_ui.add_person(person7_id, "Alex Turner", "0760000007")
        self._person_list_ui.add_person(person8_id, "Machine Gun Kelly", "0760000008")
        self._person_list_ui.add_person(person9_id, "Matthew Healy", "0760000009")
        self._person_list_ui.add_person(person10_id, "Mickey Mouse", "0760000010")

        activity1_id = str(random.randint(100, 10000))

        activity2_id = str(random.randint(100, 10000))
        while activity2_id == activity1_id:
            activity2_id = str(random.randint(100, 10000))

        activity3_id = str(random.randint(100, 10000))
        while activity3_id == activity1_id or activity3_id == activity2_id:
            activity3_id = str(random.randint(100, 10000))

        activity4_id = str(random.randint(100, 10000))
        while activity4_id == activity1_id or activity4_id == activity2_id or activity4_id == activity3_id:
            activity4_id = str(random.randint(100, 10000))

        activity5_id = str(random.randint(100, 10000))
        while activity5_id == activity1_id or activity5_id == activity2_id or activity5_id == activity3_id \
                or activity5_id == activity4_id:
            activity5_id = str(random.randint(100, 10000))

        activity6_id = str(random.randint(100, 10000))
        while activity6_id == activity1_id or activity6_id == activity2_id or activity6_id == activity3_id \
                or activity6_id == activity4_id or activity6_id == activity5_id:
            activity6_id = str(random.randint(100, 10000))

        activity7_id = str(random.randint(100, 10000))
        while activity7_id == activity1_id or activity7_id == activity2_id or activity7_id == activity3_id \
                or activity7_id == activity4_id or activity7_id == activity5_id or activity7_id == activity6_id:
            activity7_id = str(random.randint(100, 10000))

        activity8_id = str(random.randint(100, 10000))
        while activity8_id == activity1_id or activity8_id == activity2_id or activity8_id == activity3_id \
                or activity8_id == activity4_id or activity8_id == activity5_id or activity8_id == activity6_id \
                or activity8_id == activity7_id:
            activity8_id = str(random.randint(100, 10000))

        activity9_id = str(random.randint(100, 10000))
        while activity9_id == activity1_id or activity9_id == activity2_id or activity9_id == activity3_id \
                or activity9_id == activity4_id or activity9_id == activity5_id or activity9_id == activity6_id \
                or activity9_id == activity7_id or activity9_id == activity8_id:
            activity9_id = str(random.randint(100, 10000))

        activity10_id = str(random.randint(100, 10000))
        while activity10_id == activity1_id or activity10_id == activity2_id or activity10_id == activity3_id \
                or activity10_id == activity4_id or activity10_id == activity5_id or activity10_id == activity6_id \
                or activity10_id == activity7_id or activity10_id == activity8_id or activity10_id == activity9_id:
            activity10_id = str(random.randint(100, 10000))

        self._activity_list_ui.add_activity(activity1_id, [0], "10.10.2020", "14.30-14.50",
                                            "EXIT Festival")
        self._activity_list_ui.add_activity(activity2_id, [1, 2], "11.11.2020", "18.00-19.00",
                                            "Sziget Festival")
        self._activity_list_ui.add_activity(activity3_id, [3, 4, 5], "16.09.2020", "19.30-20.00",
                                            "Tomorrowland Festival")
        self._activity_list_ui.add_activity(activity4_id, [6, 7, 8], "16.09.2020", "23.00-23.30",
                                            "Download Festival")
        self._activity_list_ui.add_activity(activity5_id, [9, 10, 11, 12], "15.05.2020", "21.00-22.00",
                                            "Parklife Festival")
        self._activity_list_ui.add_activity(activity6_id, [13], "16.12.2020", "22.00-23.00",
                                            "Awakenings Festival")
        self._activity_list_ui.add_activity(activity7_id, [14, 15, 16], "01.07.2020", "23.30-23.45",
                                            "Coachella Festival")
        self._activity_list_ui.add_activity(activity8_id, [17, 19, 20], "10.10.2021", "12.00-14.00",
                                            "ENVISION Festival")
        self._activity_list_ui.add_activity(activity9_id, [22, 18, 21], "10.10.2020", "14.00-14.30",
                                            "SXM Festival")
        self._activity_list_ui.add_activity(activity10_id, [30], "10.10.2020", "14.50-20.00",
                                            "SNOWBOMBING Festival")


type_of_repo = ""
settings = ConfigParser()
settings.read("settings.properties")
if settings["DEFAULT"]["repository"] == "inmemory":
    type_of_repo = "memory_repo"
elif settings["DEFAULT"]["repository"] == "textfile":
    type_of_repo = "text_repo"
elif settings["DEFAULT"]["repository"] == "binaryfile":
    type_of_repo = "binary_repo"

ui = UI(type_of_repo)
ui.start()
