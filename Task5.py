class SportArts:
    _ARTS = ["Soccer", "Table Tennis", "Boxing", "Swimming", "Cyclyng", "Tennis"]

    def add_new_art(self, arg):
        self._ARTS.append(arg)

    def delete_an_art(self, arg):
        if arg in self._ARTS:
            self._ARTS.remove(arg)
        else:
            Exception.failure_info()

    def print_arts(self):
        print(self._ARTS)


class TrainerTeam(SportArts):
    _TEAM = [["Serhiy Ivanko", "Pavlo Dubko"], ["Natalia Maslov"], ["Ivan Kotyshko"], ["Maksym Perepelytsa"],
             ["Kateryna Liahova"], ["Anton Raketka"]
             ]
    trainers_dict = {}

    @classmethod
    def validate(cls):
        return len(cls._TEAM) == len(cls._ARTS)

    @staticmethod
    def find_trainer():
        search = input("Enter the whole name of the trainer: ")
        ind = False
        for k, v in TrainerTeam.trainers_dict.items():
            if search in v:
                ind = True
                print(f"{search} is found. Information: {k}")
        if not ind:
            Exception.trainer_not_found(search)


    def create_trainers_dict(self):
        if self.validate():
            for x in range(len(self._ARTS)):
                self.trainers_dict[self._ARTS[x]] = (self._TEAM[x])
            print(self.trainers_dict)
        else:
            print("Admins must update all related information.")
            print("If a trainer or sport is deleted, sport art or trainer may have"
                  " to be updated too by an admin.")

    def add_new_trainer(self, name):
        self._TEAM.append(name.split(sep=None, maxsplit=0))

    def delete_a_trainer(self, name):
        ind = False
        for i in self._TEAM:
            if name in i:
                i.remove(name)
                if len(i) == 0:
                    self._TEAM.remove(i)
                    self.create_trainers_dict()
                ind = True
        if ind:
            print(f"The trainer {name} was deleted")
            print("Our trainers are: ", TrainerTeam._TEAM)
        else:
            Exception.failure_info()
            print("Our trainers are: ", TrainerTeam._TEAM)


class Trainings:
    _TIME_TABLE = {
        "MONDAY": {"Soccer": "11 o`clock",
                 "Table Tennis": "1 o`clock",
                 "Boxing": "3 o`clock",
                 "Swimming": "5 o`clock",
                 "Cycling": "6 o`clock",
                 "Tennis": "7 o`clock"},
        "WEDNESDAY": {"Soccer": "11 o`clock",
                 "Table Tennis": "1 o`clock",
                 "Boxing": "3 o`clock",
                 "Swimming": "5 o`clock",
                 "Cycling": "6 o`clock",
                 "Tennis": "7 o`clock"},
        "FRIDAY": {"Soccer": "11 o`clock",
                 "Table Tennis": "1 o`clock",
                 "Boxing": "3 o`clock",
                 "Swimming": "5 o`clock",
                 "Cycling": "6 o`clock",
                 "Tennis": "7 o`clock"}
    }

    def _change_time_table(self):
        ask = input("CHOOSE A DAY: ").upper()
        if Exception.alpha_(ask):
            if ask in Trainings._TIME_TABLE.keys():
                ask1 = input("Choose an art: ").title()
                if ask1 in Trainings._TIME_TABLE[ask]:
                    change = input("Enter new time: ")
                    if Exception.digit(change):
                        Trainings._TIME_TABLE[ask][ask1] = change + " " + "o`clock"
                    else:
                        Exception.failure_info()
                else:
                    Exception.failure_info()
            else:
                Exception.free_day()
        else:
            Exception.failure_info()

    def show_time_table(self):
        for k, v in Trainings._TIME_TABLE.items():
            print(k, v)


class Fee:
    already_set = False
    __FEE = 0

    @property
    def fee(self):
        return self.__FEE

    @fee.setter
    def fee(self, arg):
        Fee.__FEE = arg
        Fee.already_set = True


class Exception:

    @staticmethod
    def alpha_(arg):
        a = [char.isalpha() or char == " " for char in arg]
        return all(a)

    @staticmethod
    def free_day():
        print("It is not a working day")

    @staticmethod
    def digit(arg):
        a = [char.isdigit() for char in arg]
        return all(a)

    @staticmethod
    def set_time(arg):
        return int(arg) in range(1, 13)

    @staticmethod
    def lenth(arg):
        if type(arg) == int:
            return len(arg) == 1

    @staticmethod
    def trainer_not_found(arg):
        print(f"{arg} does not work for us as a trainer")

    @staticmethod
    def failure_info():
        print("You must have made a failure when typed")


class Admin:
    def __init__(self, name):
        self.name = name

    def menu(self):
        sa = SportArts()
        tt = TrainerTeam()
        t = Trainings()
        f = Fee()
        p = ProgramRunning()
        while True:

            print("""                           ADMIN MODE
                                                OPTIONS:
                    1 - add new sport art     2 - delete a sport art      3 - Find a trainer
                    4 - add a new trainer     5 - delete a trainer        6 - change timetable
                    7 - set a fee             8 - change to user mode     9 - end"""
                  )
            choice = input(f"{self.name}, please give your choice in the menu: ")

            match choice:
                case "1":
                    sa.print_arts()
                    new_art = input("Add a new sport art")
                    if Exception.alpha_(new_art):
                        sa.add_new_art(new_art)
                        sa.print_arts()
                    else:
                        Exception.failure_info()
                case "2":
                    sa.print_arts()
                    art_to_del = input("Enter the art to delete: ").title()
                    sa.delete_an_art(art_to_del)
                    sa.print_arts()
                case "3":
                    tt.create_trainers_dict()
                    tt.find_trainer()
                case "4":
                    n_trainer = input("Enter a new trainer's name: ")
                    if Exception.alpha_(n_trainer):
                        tt.add_new_trainer(n_trainer)
                        print(tt._TEAM)
                    else:
                        Exception.failure_info()
                case "5":
                    d_trainer = input("Enter a trainer's name to delete: ")
                    tt.delete_a_trainer(d_trainer)
                case "6":
                    t.show_time_table()
                    t._change_time_table()
                    t.show_time_table()
                case "7":
                    fee = input("Set a fee for a training: ")
                    if Exception.digit(fee):
                        f.fee = fee
                    else:
                        Exception.failure_info()
                case "8":
                    p.admin_changes_mode()
                case "9":
                    print("Your session has finished")
                    break
                case _:
                    Exception.failure_info()


class User:
    def __init__(self, name):
        self.name = name

    def user_menu(self):
        sa1 = SportArts()
        tt1 = TrainerTeam()
        t1 = Trainings()
        f1 = Fee()
        while True:
            print("""                           USER MODE
                                                OPTIONS:
                    1 - Sport arts     2 - Trainers    3 - Find a trainer
                     4 - Timetable for trainings    5 - Information about the fee      6 - end"""
                  )
            choice = input(f"{self.name}, please give your choice in the menu: ")
            match choice:
                case "1":
                    sa1.print_arts()
                case "2":
                    tt1.create_trainers_dict()
                case "3":
                    tt1.find_trainer()
                case "4":
                    t1.show_time_table()
                case "5":
                    if Fee.already_set:
                        print(f1.fee, "UAH")
                    else:
                        f1.fee = 50
                        print(f1.fee, "UAH")
                case "6":
                    break
                case _:
                    Exception.failure_info()

class ProgramRunning:
    def __init__(self):
        self.name = None

    def run(self):
        self.name = input("What is your name: ")
        if Exception.alpha_(self.name):
            choice = input("Print 'y' if you are an admin or any other symbol if not: ")
            if choice == "y":
                admin = Admin(self.name)
                admin.menu()
            else:
                user = User(self.name)
                user.user_menu()
        else:
            Exception.failure_info()

    def admin_changes_mode(self):
        user = User(self.name)
        user.user_menu()


program = ProgramRunning()
program.run()
