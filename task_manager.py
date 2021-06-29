import datetime

global user_name1
global user_password
global name
global user_input
global countusers
global count
global line
# creat a longin system that gives gives accuess to users listed in user file only
# open user.txt file

valid_username = ""
valid_password = ""
login = False
user3 = open('user.txt', 'r')
# ask user to enter their username and password
while not login:
    username = input("Please enter your username : ")
    password = input("Please enter your password : ")

    # checking if username and password is correct
    for lines3 in user3:
        temp = lines3.strip()
        temp = temp.split(", ")
        valid_username = temp[0]  # gives the postion of were the username is in user.txt
        valid_password = temp[1]  # gives the postion of were the password is in user.txt
        if username == valid_username and password == valid_password:  # checks if the correct passord is in and gives accuse to user
            login = True
            print("Welcome to Task Manager \n")
            user3.seek(0)
            break

    if username != valid_username or password != valid_password:  # send message that password is incorrect
        login = False
        print("Please enter a valid username and password")
    user3.seek(0)

user3.close()

# declare a var for choices to creat a choice menu
choice = False


# once user is login show the choice menu so that user can see their options
def menu():
    while login == True:
        choice = input("""Please select one of the following optionS :
        r - Register user
        a - Add task
        va - View all tasks
        vm - View my tasks
        gr - generate reports
        ds - display statistics
        e - Exit
        """)

        def reg_user():
            # only adim is allowed to accuse this option
            # requset admin to login
            global user_ds
            user_ds = 0
            admin_login = False
            while not admin_login:
                admin = input("Please enter username : ")
                ad_password = input("Please enter password : ")

                if admin == "admin" and password == "adm1n":  # makes sure that admin is the only one with accuses
                    admin_login = True
                    print("Welcome Admin")
                    new_username = input(
                        "Please Enter new username : ")  # request admin to give a username for new user
                    new_password = input(
                        "Please enter new password : ")  # request admin to give a password for new user
                    cofrim_password = input(
                        "Please enter password again : ")  # request admin to confrim password entered

                    # open user txt file again
                    with open('user.txt') as file:
                        # check if username is already in user.txt file
                        user_in_file = False
                        while user_in_file == False:
                            if new_username in file.read() or new_password in file.read():  # read through user.txt to see if password or username is already being used
                                print("Username or Password already exists")
                                break
                            else:
                                user_in_file = True

                        # if username or password is not in the user.txt fu=ile the the new user is added
                        if user_in_file == True:
                            if cofrim_password == new_password:  # if password match the user is added to user list
                                with open('user.txt', 'a') as user:
                                    user.write("\n" + new_username + ", " + new_password)
                                    user_ds += 1
                            else:
                                print("Password do not match ")
                            user.close()
                else:
                    print("Please enter a valid username and password")

            # once admin is login admin can now add new register new users
            # open user.txt file to add new users

        if choice == "r":  # is if user choices to register user
            choice = True
            print(reg_user())
            break

        def add_task():
            global task_ds
            task_ds = 0
            # open tasks.txt if user chooses add a task
            task = open('tasks.txt', 'r+')
            for line in task:
                temp = line.strip()
                temp = temp.split(", ")
                # request user to enter task detilas
                username = input("Please enter the user task is assigined to : ")
                description = input("Please enter the description of task : ")
                date = input("Please enter the date that this task is being entered : ")
                due_date = input("Please enter the due date for task to be complete : ")
                complete = input("Please enter Yes or No if task was completed or not : ")

                # sort the task detiles in tasks.txt
                task.write("\n" + username + ", " + description + ", " + date + ", " + due_date + ", " + complete)
                task_ds += 1
                break

        if choice == "a":  # user choices to add task
            choice = True
            print(add_task())
            break

        def view_all():
            count = 0
            # open the tasks.txt
            tasks = open('tasks.txt', 'r+')
            for lines in tasks:
                count += 1
                temp = lines.strip()
                temp = temp.split(", ")  # gives the postion of the following detail
                print("Username : ", temp[0])
                print("Description : ", temp[1])
                print("Date : ", temp[2])
                print("Due Date : ", temp[3])
                print("Complete : ", temp[4])
                print("\n")
            tasks.close()

        if choice == "va":  # user choose to view all task
            choice = True
            print(view_all())
            break

        def view_mine():
            num_task = 0
            user_input = input("Please enter the username which you want to view the tasks for?\n")  # get user input
            infile = open('tasks.txt', 'r+')  # open the file
            for row in infile:  # read each row in the file
                field = row.split(", ")  # split each row with a comma
                view_more = infile.readlines()  # read the file contents to view more

                if field:  # check the field in tasks file
                    num_task += 1  # increment the tasks completed
                    print("Task Number: " + str(num_task) + "\nUsername: " + field[0] + "\nDescription: " + field[1] +
                          "\n Date: " + field[2] + "\nDue Date: " + field[
                              3] + "\n" + "Completed: " + field[4] + "\n")  # display the user's tasks

                    editTask = input(
                        "Would you like to edit a task? (Edit) or return to the menu? (-1)\n")
                    if editTask == "edit".lower():
                        file = open('tasks.txt', 'r+')
                        num_task1 = int(input("Please enter the Task number?\n"))
                        num_task1 -= 1
                        taskFile1 = file.readlines()
                        for line in taskFile1:
                            taskFile1 = file.readlines()
                            #print(taskFile1[num_task1] + "\n")
                            break
                        taskComplete = input("Has this task been completed?\n")
                        if taskComplete == "Yes":
                            with open("tasks.txt", 'r+') as taskFile:
                                for line in taskFile:
                                    field1 = line.strip()
                                    field1 = field1.split(", ")
                                    taskFile = file.readlines()
                                    new_state = taskFile.replace(field1[4], "Yes")

                                    print(new_state)
                        #updated_string = view_more.replace(taskFile1[num_task].strip(), new_state)
                        with open('tasks.txt', 'a+') as file:
                            file.write(new_state)

        if choice == "vm":  # user choices to view they task only
            choice = True
            print(view_mine())
            break

        # display statistics function
        def display_statistics(name1, user_password, countusers, count, line):
            while True:
                name1 = ""
                countusers = 0
                count = 0
                line = []
                print('STATISTICS FOR THE TOTAL NUMBER OF TASKS AND USERS \n')
                print('Only admin must access this option\n')
                infile = open('user.txt', 'r')  # read the file
                name1 = input('\nEnter your Username: \n')  # request the user for their username
                user_password = input('Enter your Password: \n')  # request the user for their password
                for line in infile:
                    if name1 + ', ' + user_password + '\n' == line:  # check if the user's logins match what is in the file
                        print('Welcome! You have successfully logged in.\n')  # print a success message
                        break

                for user in infile:  # check for the users in the file
                    if user[0]:
                        countusers += 1  # count the users

                print('Total number of Users:', countusers)  # display the resul
                break

        if choice == 'ds':  # truth path for the selection variable

            display_statistics('user_name', 'user_password', 'countusers', 'count',
                               'line')  # call the display statistics function

        def generate_reports():
            # Generates task report
            infile = open("tasks.txt", "r")
            info = infile.readlines()
            # Intialising counting variables
            num_of_tasks = 0
            num_of_complete_tasks = 0
            num_of_uncompleted_tasks = 0
            num_of_overdue_tasks = 0
            # Checking through tasks info
            for line in info:
                num_of_tasks += 1
                if "Yes" in line:
                    num_of_complete_tasks += 1
                if "No" in line:
                    num_of_uncompleted_tasks += 1
                    info = line.split(", ")
                due_date = line[4]
                date = datetime.datetime.now()
                line = ", ".join(line)

            # Working out the percentages
            percentage_incomplete = (num_of_uncompleted_tasks / num_of_tasks) * 100
            percentage_overdue = (num_of_overdue_tasks / num_of_tasks) * 100
            # Creating report output list
            print('The percentage is :' + str(percentage_incomplete))
            print('The percentage overdue is:' + str(percentage_overdue))

        if choice == "gr":
            choice = True
            print(generate_reports())
            break

        if choice == "e":  # exit option app stops running once this option is selected
            choice = True
            print("GoodBye")
            break  # allows menu to not show again for every option beside the exit option

        else:
            choice = False
            print("Please enter a valid option")  # user only allowed to enter options showen on the menu


menu()
