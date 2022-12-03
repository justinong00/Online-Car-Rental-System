#JUSTIN ONG CHIN IT
#TP063682


#   ADMIN

#   (ii)    [ADMIN Add Car Records]     [Verified]


def entry_check(msg, list):         # carType, carSeat, carTransmission, carFuel, carStatus
    while (True):
        print("\n", list)
        ans = input("\n" + msg).replace(" ", "")
        if (ans not in list):
            print("Invalid input. Try again.")
            continue
        else:
            return ans


def car_ID_check(msg):              # carID
    while (True):
        ans = input("\n" + msg).replace(" ", "")
        if (ans.startswith("SCRS") and len(ans) == 7):    # assume admin has the knowledge to not input the same SCRS num
            return ans
        else:
            print("Invalid input. Try again")
            continue


def check_num_entry(msg):           # carDailyRate
    while (True):
        try:
            ans = int(input("\n"+msg))      # < class int > auto strip whitespaces
            return str(ans)
        except:
            print("Invalid input. Try again.")
            continue


def rec_upd_msg(filename):
    print("\nRecords Updated!")
    print("\nTAKE NOTE!\n=========\n"
          "New Status will only be updated upon EXIT from MAIN MENU."
          "\nCHECK", filename, "to view UPDATED STATUS.")


def try_again(msg):
    while (True):
        ans = input("\nWould you like to " + msg + " ? (y/n): ").replace(" ", "")
        if (ans == "y"):
            return True
        elif (ans == "n"):
            return False
        else:
            print("Invalid input. Try Again.")
            continue


def add_car_rec():

    with open("car.txt", "a") as car_file:
        car_typ_list = ["Hatchback", "Sedan", "MPV", "SUV"]
        car_seat_list = ["4Seats", "5Seats", "7Seats", "8Seats"]
        car_trans_list = ["Automatic", "Manual"]
        car_fuel_list = ["Gasoline", "Diesel"]
        car_status_list = ["Yes", "No"]
        car_typ_msg = "Enter car type: "
        car_seat_msg = "Enter seat capacity: "
        car_trans_msg = "Enter Transmission Type: "
        car_fuel_msg = "Enter Fuel Type: "
        car_status_msg = "Availability: "
        car_ID_msg = "Create a Car ID (e.g, SCRSxxx): "
        day_rate_msg = "Enter daily rate: RM"
        while (True):
            car_model = input("\nEnter car model (e.g, ProtonSaga): ").replace(" ", "")
            if (car_model.find(":") != -1):
                print("\":\" is not allowed. Try Again.")
                continue
            car_type = entry_check(car_typ_msg, car_typ_list)
            seat = entry_check(car_seat_msg, car_seat_list)
            trans = entry_check(car_trans_msg, car_trans_list)
            fuel = entry_check(car_fuel_msg, car_fuel_list)
            status = entry_check(car_status_msg, car_status_list)
            car_ID = car_ID_check(car_ID_msg)
            daily_rate = check_num_entry(day_rate_msg)
            rec_str = car_model + ":" + car_type + \
                      ":" + seat + ":" + trans + \
                      ":" + fuel + ":" + status + \
                      ":" + car_ID + \
                      ":" + daily_rate + "\n"
            car_file.write(rec_str)

            rec_upd_msg("car.txt")      # message that record has been updated

            ans = try_again("add another record")           # add another record ?

            if (ans):           # ans == True
                continue
            else:               # ans == False
                break


#   (iii)   [ADMIN Modify Car Records]      [Verified]


def validate_car_ID(all_car_rec_list):
        car_ID_list = []                # returns all fields of carID
        for rec in all_car_rec_list:
            end_carID_marker = rec.rfind(":")
            front_carID_marker = rec.rfind(":", 0, end_carID_marker)
            car_ID_index = rec[front_carID_marker + 1:end_carID_marker]
            car_ID_list.append(car_ID_index)
        while (True):
            skey = input("\nEnter Car ID (SCRSxxx): ").replace(" ", "")     # compares the CarID with car_ID_list
            if (skey not in car_ID_list):
                print("Invalid Car ID. Try Again.")
                continue
            else:
                return skey


# specific numbers like 1 to 8
def check_spec_num_entry(msg):
    while (True):
        try:
            ans = int(input("\n" + msg))  # < class int > auto strip whitespace
            if (0 < ans < 9):  # between 1 to 8 only accepted
                return ans
            else:
                print("Invalid number option. Try Again. "
                      "Enter between 1 - 8")
                continue
        except:
            print("Invalid input. Try again.")
            continue


def overwrite_file(filename, new_list):
    with open(filename, "w") as write_file:
        for fields in new_list:
            str_rec = ":".join(fields)              # each fields joins into one record
            write_file.write(str_rec + "\n")        # each record overwrites the specified filename, e.g, car.txt

# vertical
def display_car_rec(heading, field):
    if (heading != "CAR BOOKING"):
        print("\n" + heading + "\n====================\n")
        print("1. Car Model: ", field[0])
        print("2. Car Type: ", field[1])
        print("3. Seat Capacity: ", field[2])
        print("4. Transmission: ", field[3])
        print("5. Fuel Type: ", field[4])
        print("6. Availability: ", field[5])
        print("7. Car ID: ", field[6])
        print("8. Daily Rate: RM", field[7], "per day")
    else:                                                   # (v)   for Customer Do Payment to Confirm Booking
        print("\n" + heading + "\n====================\n")
        print("1. Car Model: ", field[0])
        print("2. Car Type: ", field[1])
        print("3. Seat Capacity: ", field[2])
        print("4. Transmission: ", field[3])
        print("5. Fuel Type: ", field[4])
        # print("Availability: ", each_rec[5])      # no need to print Availability, since it will be "No" always
        print("6. Car ID: ", field[6])
        print("7. Daily Rate: RM", field[7], "per day")


def check_new_data(num_op, msg):
    car_typ_list = ["Hatchback", "Sedan", "MPV", "SUV"]
    car_seat_list = ["4Seats", "5Seats", "7Seats", "8Seats"]
    car_trans_list = ["Automatic", "Manual"]
    car_fuel_list = ["Gasoline", "Diesel"]
    car_status_list = ["Yes", "No"]
    if (num_op == 1):
        while (True):
            new_data = input("\n" + msg).replace(" ", "")
            if new_data.find(":") != -1:
                print("\":\" is not allowed. Try Again.")
                continue
            else:
                break
        return new_data
    elif (num_op == 2):
        new_data = entry_check(msg, car_typ_list)
        return new_data
    elif (num_op == 3):
        new_data = entry_check(msg, car_seat_list)
        return new_data
    elif (num_op == 4):
        new_data = entry_check(msg, car_trans_list)
        return new_data
    elif (num_op == 5):
        new_data = entry_check(msg, car_fuel_list)
        return new_data
    elif (num_op == 6):
        new_data = entry_check(msg, car_status_list)
        return new_data
    elif (num_op == 7):
        print("\nFollow Car ID Format, e.g, (SCRSxxx).")
        new_data = car_ID_check(msg)
        return new_data
    else:                        # num_op == 8 (Daily Rate), check_spec_num_entry(msg) already validate num_op 1 to 8
        new_data = check_num_entry(msg)
        return new_data


def mod_car_rec ():
    while (True):
        new_car_rec_list = []

        with open("car.txt", "r") as car_file:
            all_car_rec_list = car_file.readlines()
            skey = validate_car_ID(all_car_rec_list)   # returns validated skey, compared to car.txt file

            for rec in all_car_rec_list:
                field = rec.strip().split(":")
                if (skey == field[6]):
                    heading = "CAR PROFILE"
                    display_car_rec(heading, field)       # display car profile

                    num_op_msg = "Enter number option to change: "
                    num_op = check_spec_num_entry(num_op_msg)      # returns validated number option, between 1 to 8
                    print("\nPresent data: ", field[num_op - 1])    # shows present data

                    new_data_msg = "Enter new data: "
                    new_data = check_new_data(num_op, new_data_msg)     # returns validated new data

                    field[num_op - 1] = new_data                        # SWAP present data WITH new data

                    rec_upd_msg("car.txt")                              # rec update message
                new_car_rec_list.append(field)

        overwrite_file("car.txt", new_car_rec_list)                     # write the file, with list of new car records

        ans = try_again("modify another record")                        # try again ?
        if (ans):   # ans == True
            continue
        else:       # ans == False
            break


#   (iv)(a)     [ADMIN Display All Cars Available For Rent]     [VERIFIED]


def car_for_rent():
    while (True):
        with open("car.txt", "r") as car_file:
            all_car_rec_list = car_file.readlines()
            cnt = 0                                     # cnt = 0, a standby variable for NO CAR is AVAILABLE
            for rec in all_car_rec_list:
                field = rec.strip().split(":")
                if (field[5] == "Yes"):
                    cnt = 1                             # cnt = 1, if ONE OR MORE CAR is AVAILABLE
                    heading = "CAR AVAILABLE"
                    display_car_rec(heading, field)

            # cnt == 0, default cnt value means NOT A SINGLE CAR is AVAILABLE.
            if (cnt == 0):
                print("\nSORRY! There are NO AVAILABLE CARS FOR RENT!")
                print("Try searching again in a few hours.")
            ans = try_again("check available cars again")
            if (ans):  # ans == True
                continue
            else:  # ans == False
                break


#   (iv)(b)     [ADMIN Display All Customer Payment for a specific time duration ]      [NOT YET VERIFIED]

# Date Validation
def check_two_dt(stdt_msg, enddt_msg):
    import datetime
    date_obj_list = []
    while (True):
        try:
            sta_date = input("\nEnter " + stdt_msg + " date (YYYY/MM/DD): ").replace(" ", "")
            end_date = input("Enter " + enddt_msg + " date (YYYY/MM/DD): ").replace(" ", "")
            sta_date_obj = datetime.datetime.strptime(sta_date, "%Y/%m/%d")
            end_date_obj = datetime.datetime.strptime(end_date, "%Y/%m/%d")
            if (sta_date_obj > end_date_obj):         # e.g, sta_date 2021/03/03 and end_date 2020/03/03
                print("Invalid Date Range. Try Again.")
                continue
            date_obj_list.append(sta_date_obj.date())       # return the dates only
            date_obj_list.append(end_date_obj.date())       # return the dates only
            return date_obj_list        # return start date and end date in datetime objects
        except:
            print("Invalid Date. Try Again.")
            continue

'''
# Horizontal Heading
def pay_file_heading():
    print("\nCUSTOMER ID\t\t CAR ID\t\t\tAMOUNT PAID\t\tRENT DURATION\t\tBOOKING DATE\t\tRETURN DATE")
    print("============================================================================================"
          "========\n")

# payment file display fields
def pay_file_fields(field):
    print(field[0],
          "\t\t", field[1],
          "\t\t" + "RM " + field[2],
          "\t\t\t", field[3], "days",
          "\t\t\t" + field[4],
          "\t\t\t" + field[5])
'''


# Horizontal Heading
def pay_file_heading():
    print("\nCUSTOMER ID\tCAR ID\t\tAMOUNT PAID\tRENT DURATION\tBOOKING DATE\tRETURN DATE")
    print("===========================================================================================\n")
    

# payment file display fields
def pay_file_fields(field):
    print(field[0],
          "\t" + field[1],
          "\t" + "RM " + field[2],
          "\t\t" + field[3], "days",
          "\t\t" + field[4],
          "\t" + field[5])


# display the stated records
def chg_rec4_to_dtobj_show_srec(all_pay_rec_list, dates_list):
    import datetime
    cnt = 0
    for rec in all_pay_rec_list:
        field = rec.strip().split(":")
        # Converting records into date time objects
        pay_date_obj = datetime.datetime.strptime(field[4], "%Y/%m/%d")     # field[4] is the payment date
        # Comparing the dates in datetime module
        if (dates_list[0] <= pay_date_obj.date() <= dates_list[1]):   # dates_list already in date format (no time)
            cnt = 1                 # cnt = 1, if one or more payments occur between the time duration.
            pay_file_fields(field)  # display record

    if (cnt == 0):
        print("There are no records showing customer payments between these dates.")


def check_customer_payment_by_date():
    with open("payment.txt", "r") as payment_file:
        all_pay_rec_list = payment_file.readlines()
        while (True):
            # Validate Dates
            dates_list = check_two_dt("start", "end")   # gets the st_date and end_date in datetime objects (dates only)

            # Display Heading
            pay_file_heading()              # display the heading for the payment file

            # Compare the dates with the payment date (NOTE : payment date is Booking Date) and DISPLAY records
            chg_rec4_to_dtobj_show_srec(all_pay_rec_list, dates_list)

            ans = try_again("view customer payments from another time duration")

            if (ans):  # ans == True
                continue
            else:  # ans == False
                break

#   (v)(a)      [ADMIN Search Specific Car Booking]     [Verified]
#   ASSUMPTION : Car Booking must have payment record in payment.txt file, because need to pay to confirm booking


def validate_carID_pf(all_payment_rec_list, skey):
    car_ID_list = []                # collects all fields of carID from payment.txt
    for rec in all_payment_rec_list:
        front_carID_marker = rec.find(":")
        end_carID_marker = rec.find(":", front_carID_marker + 1)
        car_ID_index = rec[front_carID_marker + 1:end_carID_marker]
        car_ID_list.append(car_ID_index)
    if (skey not in car_ID_list):     # validation, incorrect Car ID will be directed back to the loop
        print("There is no booking for", skey + ".")
        return "NoBooking"
    else:
        return skey

# double filter (car.txt, payment.txt)
def search_one_car_rec():
    while (True):
        with open("car.txt", "r") as car_file:
            all_car_rec_list = car_file.readlines()             # each line will be assigned to a list
            skey = validate_car_ID(all_car_rec_list)            # RETURNS validated skey comparing with car.txt file

        with open("payment.txt", "r") as payment_file:
            all_pay_rec_list = payment_file.readlines()         # each line will be assigned to a list
            skey = validate_carID_pf(all_pay_rec_list, skey)    # checks if skey(carID) has booking, compare to payment.txt

            if (skey != "NoBooking"):                             # skey RETURNS "SCRSxxx"
                pay_file_heading()                      # display the heading, must be placed outside the loop 
                for rec in all_pay_rec_list:
                    field = rec.strip().split(":")
                    if (skey == field[1]):
                        pay_file_fields(field)                  # display the fields of the record
                        # cannot break here because the same car can be rented out again if available
        ans = try_again("search another car booking")
        if (ans):           # ans == True
            continue
        else:               # ans == False
            break


#   (v)(b)      [ADMIN Search Specific Customer Payment]    [Verified]


# used to validate cus_ID
def validate_cus_ID(all_info_list, msg=""):                         # keyword argument assigned
    cus_ID_list = []                                                # collects all fields of cus_ID
    for rec in all_info_list:
        cus_ID = rec[0:rec.find(":")]                               # since cus_ID is the first field
        cus_ID_list.append(cus_ID)
    while (True):
        skey = input("\nEnter Customer ID" + msg + ": ").replace(" ", "")
        if (skey not in cus_ID_list):                                 # compares the cus_ID with the ID_list
            print("Invalid Customer ID. Try Again.")
            continue
        else:
            return skey

# used to compare cus_ID with payment file to see if there are prior payment records
def validate_cus_ID_pf(all_payment_rec_list, skey):
    cus_ID_list = []                        # collects all fields of cus_ID
    for rec in all_payment_rec_list:
        cus_ID = rec[0:rec.find(":")]       # since cus_ID is the first field
        cus_ID_list.append(cus_ID)
    if (skey not in cus_ID_list):           # validation, incorrect Car ID will be directed back to the loop in function (validate_cus_ID)
        print("There is no payment history for", skey + ".")
        return "NoPaymentHistory"
    else:
        return skey


# double filter (cus_info.txt, payment.txt)
def search_cus_pay(adm_or_cus, username=""):    # admin search ("adm"), customer search ("cus", username=username)
    user_ID = username  # assign the username to user_ID to allow for looping as username is the condition for the loop
    while (True):
        if (username == ""):                    # for admin search (to key in cus_ID)
            with open("cus_info.txt", "r") as cus_file:
                all_cus_rec_list = cus_file.readlines()
                skey = validate_cus_ID(all_cus_rec_list)    # returns validated cus_ID comparing with cus_info.txt
                user_ID = skey                              # assign the validated cus_ID to user_ID
        with open("payment.txt", "r") as payment_file:  # customer search begin here, admin search will continue also
            all_pay_rec_list = payment_file.readlines()
            skey = validate_cus_ID_pf(all_pay_rec_list,
                                      user_ID)          # checks if cus_ID has pay history, compare to payment.txt

            if (skey != "NoPaymentHistory"):            # skey returns cus_ID e.g, avery01
                pay_file_heading()                      # display the heading, have to placed before the loop.
                for rec in all_pay_rec_list:
                    field = rec.strip().split(":")
                    if (skey == field[0]):
                        pay_file_fields(field)          # display the fields of the payment record
                        # cannot break here, because same customer may have > 1 payment history

        if (adm_or_cus == "adm"):                       # if admin search
            ans = try_again("search another customer ID")
            if (ans):                   # ans == True
                continue
            else:                       # ans == False
                break
        else:                           # adm_or_cus == "cus", means customer search
            ans = try_again("view payment history again")
            if (ans):   # ans == True
                continue
            else:       # ans == False
                break


#   (vi)	    [Admin Return a Rented Car]                 [Verified]

def return_car_chg_status():
    while (True):
        new_car_rec_list = []
        with open("car.txt", "r") as car_file:
            all_car_rec_list = car_file.readlines()
            skey = validate_car_ID(all_car_rec_list)
            cnt = 0                                 # initializing a counter, cnt = 0 if there is no match
            for rec in all_car_rec_list:
                field = rec.replace("\n", "").split(":")
                if (skey == field[6] and field[5] == "No"):
                    cnt = 1                         # cnt = 1 if there is a match
                    field[5] = "Yes"                # automatically changed the Availability Status to "Yes"
                    rec_upd_msg("car.txt")
                new_car_rec_list.append(field)      # outside the if block so that other records will append too.
            if (cnt != 1):                          # means Availability Status is already a "Yes"
                print("\nThe Availability Status of", skey, "is already \"Yes\"")

        # OVERWRITE THE FILES
        overwrite_file("car.txt", new_car_rec_list)

        ans = try_again("change the Availability Status of another car")
        if (ans):   # ans == True
            continue
        else:       # ans == False
            break


#   GUEST

#   (i)         [Guest View All Cars Available For Rent]    [Verified]

# car_for_rent()

#   (ii)        [Guest Registration]                        [Verified]


def collect_userID_pwd(list):
    taken_userID_pwd_list = []  # collect list of usernames and password that are used
    for rec in list:
        user_ID_marker = rec.find(":")
        taken_user_ID = rec[:user_ID_marker]
        taken_userID_pwd_list.append(taken_user_ID)
        pwd_marker = rec.find(":", user_ID_marker + 1)
        taken_pwd = rec[user_ID_marker + 1:pwd_marker]
        taken_userID_pwd_list.append(taken_pwd)
    return taken_userID_pwd_list


def crt_userID(taken_userID_pwd_list):
    while (True):
        user_ID = input("\nCreate Username: ").replace(" ", "")
        if (user_ID in taken_userID_pwd_list):
            print("Sorry. Username already taken. "
                  "Try another username.")
        elif (user_ID.find(":") != -1):
            print("\":\" is not allowed in username. ")
            continue
        else:
            return user_ID


def pwd_rules():
    print("\nPASSWORD REQUIREMENTS\n=====================\n")
    print("1. MUST be alphanumeric.")
    print("2. MUST contain between 8 - 30 characters.")


def crt_pwd(taken_userID_pwd_list):
    while (True):
        pwd_rules()                         # display password rules
        password = input("\nCreate Password: ").replace(" ", "")
        if (password in taken_userID_pwd_list):
            print("Sorry. Password already taken. "
                  "Try another password.")
            continue
        elif (password.isalnum() and 8 <= len(password) <= 30):
            return password
        else:
            print("Invalid Password. Try Again.")
            continue


def write_name():
    name_list = []                  # collect first_name and last_name
    while (True):
        first_name = input("\nEnter First Name: ").capitalize().replace(" ", "")
        if (first_name.isalpha()):
            name_list.append(first_name)
            break
        else:
            print("Invalid Name. Try Again.")
            continue
    while (True):
        last_name = input("\nEnter Last Name: ").capitalize().replace(" ", "")
        if (last_name.isalpha()):
            name_list.append(last_name)
            break
        else:
            print("Invalid Name. Try Again.")
            continue
    return name_list


def write_phnum():
    while (True):
        try:
            ph_num = int(input("\nEnter Phone Number: +60"))  # < class 'int' > strip whitespaces by default
            return ph_num
        except:
            print("Invalid phone number. Try again.")
            continue


def check_dob():
    import datetime
    dt_list = []        # collects the string date and the datetime object date
    while (True):
        try:            # expect VALID Dates AND VALID Date Formats (YYYY/MM/DD)
            birth_dt = input("\nEnter Date of Birth in format (YYYY/MM/DD): ").replace(" ", "")
            birth_dt_obj = datetime.datetime.strptime(birth_dt, "%Y/%m/%d")
            dt_list.append(birth_dt)
            dt_list.append(birth_dt_obj)
            return dt_list
        except:         # catches INVALID Dates OR INVALID Date Formats, e.g, 2021/02/31 OR 2021.02.28, etc.
            print("Invalid Date. Try Again.")
            continue

# exit(0)!!!!!!!!!!!!!!!!!!!!!!!1
def check_age(birth_dt_obj):
    import datetime
    age = datetime.date.today().year - birth_dt_obj.date().year  # age is <class 'int'>
    if (age <= 21 or age >= 70):
        print("Sorry. Registration is only applicable "
              "for users between the ages of 22 to 69 years old.")
        return "NotLegal"   # unable to signup for an account, not at legal driving age to rent a car


def append_info_to_file(filename, list):        # for APPENDING customer info OR admin info OR payment info
    with open(filename, "a") as fh:
        str_rec = list[0] + \
                  ":" + list[1] + \
                  ":" + list[2] + \
                  ":" + list[3] + \
                  ":" + list[4] + \
                  ":" + list[5] + "\n"
        fh.write(str_rec)

# filename either "cus_info.txt" or adm_info.txt"
def new_reg(filename):

    with open(filename, "r") as fh:
        all_info_list = fh.readlines()

        # Returns a list containing used_cus_ID and used pwd
        taken_userID_pwd_list = collect_userID_pwd(all_info_list)

        # Comparing the Entered Username with the list
        user_ID = crt_userID(taken_userID_pwd_list)

        # Comparing the Entered Password with the list
        password = crt_pwd(taken_userID_pwd_list)

        # Checking Entered Name
        name_list = write_name()            # Returns Validated Names
        first_name = name_list[0]
        last_name = name_list[1]

        # Checking Entered Phone Number (+60xxxxxxxxxx)
        ph_num = write_phnum()              # Returns INTEGER

        # Checking Entered Date Of Birth and Converting string date to date time object
        birth_dt_list = check_dob()         # Returns two dates, [0] is str date, [1] is datetime object date
        str_birth_dt = birth_dt_list[0]
        dtobj_birth_dt = birth_dt_list[1]

        # Validating Age Requirements
        legal_age = check_age(dtobj_birth_dt)           # UNABLE to signup if age <= 21 or age >= 70
        if legal_age == "NotLegal":
            return "SignUpFail"

        # Append all info into signup_list
        signup_list = []
        signup_list.append(user_ID)
        signup_list.append(password)
        signup_list.append(first_name)
        signup_list.append(last_name)
        signup_list.append(str(ph_num))
        signup_list.append(str_birth_dt)

    # Convert sign_up list into one string record and append to required file ("cus_info.txt" OR "admin_info.txt")

    append_info_to_file(filename, signup_list)

    print("\nAccount Created!. Thanks", user_ID, "for becoming a SCRS member.")
    print("\nTAKE NOTE!\n=========\n"
          "Access to Other Details will be granted upon selecting Registered User and Login from MAIN MENU.")


#   (ii)        [Registered Customer View Personal Rental History]      [Verified]


# search_cus_pay("cus")


#   (iii)       [Registered Customer View Available Cars For Rent]      [Verified]


# car_for_rent()


#   (iv)        [Registered Customer Select and Book A Car]             [Verified]
#   ASSUMPTION : One user can only make one booking at a time and booking slot is for one week only.

# validating the dates AND ensuring the Pick Up date is between present date and date of the following week
def car_booking_dts():
    import datetime
    while (True):
        dt_list = check_two_dt("Pick Up", "Drop Off")   # validate both dates and return dates only in datetime object
        tday = datetime.date.today()                    # getting present date

        tdelta1 = datetime.timedelta(days=1)            # bookings are only available the following day.
        tdelta2 = datetime.timedelta(days=7)            # bookings beyond a week is NOT allowed
        next_day_obj = tday + tdelta1                   # following date (datetime object)
        next_wk_dt_obj = tday + tdelta2                 # date of following week (datetime object)

        next_day_str = datetime.date.strftime(next_day_obj, "%Y/%m/%d")         # following date (string format)
        next_wk_dt_str = datetime.date.strftime(next_wk_dt_obj, "%Y/%m/%d")     # date of following week (string format)

        if (dt_list[0] <= tday):                          # check if Pick Up date is in present date and past dates
            print("\nSorry. Bookings must be made at least 1 day in advance.")
            print("Bookings are only available from", next_day_str, "onwards. Try Again.")
            continue
        elif (dt_list[0] > next_wk_dt_obj):               # check if Pick Up date is beyond a week
            print("\nSorry. Bookings beyond a week is NOT allowed.")
            print("Bookings are only available from", next_day_str, "to", next_wk_dt_str, ". Try Again.")
            continue
        else:
            return dt_list                              # Returns Pick Up date and Drop Off Date in datetime object


def car_booking(username):

    with open("car.txt", "r") as car_file:
        dt_list = car_booking_dts()                     # validate and return dates only in datetime object

        car_for_rent()                                  # Showing Cars Available for Rent
        print("\nWhich car would you like to book ?")   # put outside the loop or else will keep showing this message

        all_car_rec_list = car_file.readlines()

        while (True):
            import datetime
            cnt = 0                     # initialize a control variable
            payment_rec_list = []       # a list to collect duration, start date, end date and username
            new_car_list = []           # a list of new car records for car.txt as availability status of the booked car will be changed to username
            booking = input("\nEnter Car ID (SCRSxxx): ").replace(" ", "")   # car_ID is booking_ID
            for rec in all_car_rec_list:
                field = rec.strip().split(":")
                if (booking == field[6] and field[5] == "Yes"):     # Checking Car ID with car.txt and seeing its status
                    cnt = 1
                    # using username as the unique identifier to recognize car booking later for payment
                    book_finder = username
                    field[5] = book_finder      # change the Availability Status to the username (book_finder)
                new_car_list.append(field)
            if (cnt == 1):
                overwrite_file("car.txt", new_car_list)
                str_collect_dt = datetime.date.strftime(dt_list[0], "%Y/%m/%d")     # Pick Up Date (string format)
                str_return_dt = datetime.date.strftime(dt_list[1], "%Y/%m/%d")      # Drop Off Date (string format)
                print("\nBooking Successful!")
                print("\nReservation for", booking, "has been made from", str_collect_dt, "to", str_return_dt, ".")
                print("Proceed to \"OPTION 4\" to CONFIRM booking.")
                duration = (dt_list[1] - dt_list[0]).days       # duration is INTEGER
                payment_rec_list.append(str(duration))
                payment_rec_list.append(str_collect_dt)
                payment_rec_list.append(str_return_dt)
                payment_rec_list.append(book_finder)            # username to uniquely identify the booked car
                return payment_rec_list    # Returns [duration, start date, end date, username], all elements in string
            else:                          # cnt = 0, means either Car ID entered is wrong or the Car is Not Available.
                print("Booking Failed! Try Again.")
                print("\nPlease enter correct Car ID.")
                continue


#   (v)        [Registered Customer Do Payment to Confirm Booking]      [Verified]


def pay_car_booking(payment_list, username):
    with open("car.txt", "r") as car_file:
        all_car_rec_list = car_file.readlines()
        while (True):
            new_car_list = []
            for rec in all_car_rec_list:
                field = rec.strip().split(":")
                # checking car_ID with record and checking if the status is the book_finder(username)
                if (field[5] == username):      # field[5] is the book_finder
                    booked_car_rec = rec        # the record of the car is assigned to booked_car_rec
                    field[5] = "No"             # Change the field[5] from username to "No"
                new_car_list.append(field)

            overwrite_file("car.txt", new_car_list)         # overwrite the file to change the status to "No"
            break

        # SPLITTING THE FIELDS OF THE SPECIFIC RECORD
        each_field = booked_car_rec.strip().split(":")

        # DISPLAYING EACH FIELD
        heading = "CAR BOOKING"
        display_car_rec(heading, each_field)


    with open("cus_info.txt", "r") as cus_file:
        all_cus_rec_list = cus_file.readlines()

        # CALCULATE AMOUNT
        amount = int(payment_list[0]) * int(each_field[7])      # each_field[7] is the daily rate

        # DISPLAY MESSAGE
        print("\nBooking Confirmed for", username + ". The", each_field[0], "will be available on", payment_list[1])
        print("Total Payment is: RM", str(amount))
        print("\nTAKE NOTE\n=========\n")
        print("Due to the Movement Control Order (MCO),"
              " We kindly ask that you arrange payment via Online Transfer/Bank Transfer as soon as possible.")
        print("\nAccount name : SCRS MALAYSIA SDN BHD\nMaybank account number : 342167547809")
        print("\nPlease enclose proof of payment to \"scrssupport@gmail.com\" once payment has been made.")
        print("\nIMPORTANT: Payment MUST be made on the date of booking. Any delay will VOID your reservation.")

        # LIST OF ALL REQUIRED FIELDS FOR payment.txt
        payment_str_rec_list = []
        payment_str_rec_list.append(username)                   # cus_ID
        payment_str_rec_list.append(each_field[6])              # car_ID
        payment_str_rec_list.append(str(amount))                # total amount
        payment_str_rec_list.append(payment_list[0])
        #payment_str_rec_list.append(str(payment_list[0]))      # duration
        payment_str_rec_list.append(payment_list[1])            # pick up date
        payment_str_rec_list.append(payment_list[2])            # drop off date

        # APPEND THE LIST INTO payment.txt
        append_info_to_file("payment.txt", payment_str_rec_list)



#   ADMIN FUNCTIONALITIES

#       (a)         [Admin Login]                                                       [Verified]

def login(file_name):
    with open(file_name, "r") as fh:
        all_info_list = fh.readlines()
        attempt = 1
        while (attempt <= 3):
            cnt = 0                            # cnt = 0, is the standby variable if login is unsuccessful in 3 tries
            username = input("\nUsername: ").replace(" ", "")
            password = input("Password: ").replace(" ", "")
            for rec in all_info_list:
                field = rec.strip().split(":")
                if (username == field[0] and password == field[1]):
                    print("\nLogin Successful.")
                    cnt = 1                         # cnt = 1, if login successfully logins
            if (cnt == 1):
                login_list = ["SignedIn", username]
                return login_list                   # means successful login
            else:
                print("\nLogin Failed. Try again.")
                print("You have", 3 - attempt, "chances left.")
            attempt = attempt + 1
        return "LoginFail"


#       (b)         [Admin Menu]                                                        [Verified]

def admin_menu():
    while (True):
        op_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
        print("\nADMIN MENU\n==========\n")
        print("1. Add New Car")
        print("2. Modify Car Details")
        print("3. Display All Records")
        print("4. Search Specific Records")
        print("5. Return a Rented Car")
        print("6. Delete Records")
        print("7. Create Admin Account")
        print("8. Go Back to Main Menu\n")
        op = input("Enter option: ").replace(" ", "")
        if (op in op_list):
            break
        else:
            print("\nInvalid Option. Try Again.")
        #   continue ( since it is a while (True) loop )
    return int(op)


#       (c)         [Admin Directory to Each Section After Successful Signing In]       [Verified]

#   for admin option 3 ("Display All Records") MENU
def show_all_rec():
    while (True):
        op_list = ["1", "2", "3"]
        print("\nDISPLAY ALL RECORDS OF:\n=====================\n")
        print("1. Cars Available for Rent")
        print("2. Customer Payment for a Specific Duration")
        print("3. Go Back to Admin Menu\n")
        ans = input("Enter option: ").replace(" ", "")
        if (ans not in op_list):
            print("\nInvalid Option. Try Again.")
            continue
        elif (ans == "1"):
            car_for_rent()
            continue
        elif (ans == "2"):
            check_customer_payment_by_date()
            continue
        else:               # ans == "3"
            break

#   for admin option 4 ("Search Specific Records") MENU
def search_specific_rec():
    while (True):
        op_list = ["1", "2", "3"]
        print("\nSEARCH SPECIFIC RECORDS OF:\n=====================\n")
        print("1. Specific Car Booking")
        print("2. Specific Customer Payment")
        print("3. Go Back to Admin Menu\n")
        ans = input("Enter option: ").replace(" ", "")
        if (ans not in op_list):
            print("\nInvalid Option. Try Again.")
            continue
        elif (ans == "1"):
            search_one_car_rec()
            continue
        elif (ans == "2"):
            search_cus_pay("adm")       # "adm" for admin_search and "cus" for cus_search
            continue
        else:                           # ans == "3"
            break


def delete_car_rec():
    while (True):
        import os
        car_file = open("car.txt", "r")
        temp_file = open("temp.txt", "w")
        all_car_rec_list = car_file.readlines()
        delete_ID = validate_car_ID(all_car_rec_list)   # delete_ID is the unique identifier for which record to delete
        for rec in all_car_rec_list:
            field = rec.strip().split(":")
            if (delete_ID != field[6]):       # only the ID which needs to be deleted will NOT be written to temp.txt
                temp_file.write(rec)        # remaining records are written to temp.txt
        rec_upd_msg("car.txt")
        car_file.close()
        temp_file.close()
        os.remove("car.txt")                # delete the file
        os.replace("temp.txt", "car.txt")   # replace the name of the temp file with "car.txt"
        ans = try_again("delete another car record")
        if (ans):  # ans == True
            continue
        else:  # ans == False
            break


def delete_pay_rec():
    while (True):
        import datetime
        import os
        cus_file = open("cus_info.txt", "r")
        pay_file = open("payment.txt", "r")
        temp_file = open("temp.txt", "w")
        all_cus_rec_list = cus_file.readlines()
        all_pay_rec_list = pay_file.readlines()
        delete_ID = validate_cus_ID(all_cus_rec_list)                   # RETURN validated cus_ID from cus_info.txt
        delete_ID = validate_cus_ID_pf(all_pay_rec_list, delete_ID)     # COMPARE the cus_ID with the payment.txt
        if (delete_ID == "NoPaymentHistory"):                             # means the cus_ID has no prior payment record
            continue
        dt_list = check_two_dt("start", "end")                          # return validated st_dt and end_dt in datetime
        str_st_dt = datetime.date.strftime(dt_list[0], "%Y/%m/%d")      # convert st_dt to string format
        str_end_dt = datetime.date.strftime(dt_list[1], "%Y/%m/%d")     # convert end_dt to string format
        for rec in all_pay_rec_list:
            field = rec.strip().split(":")
            if (delete_ID == field[0] and str_st_dt == field[4] and str_end_dt == field[5]):  # only 1 possibility
                continue
            else:
                temp_file.write(rec)                    # remaining records are written to temp.txt
        rec_upd_msg("payment.txt")                      # update message
        temp_file.close()
        pay_file.close()
        cus_file.close()
        os.remove("payment.txt")                        # delete the file
        os.replace("temp.txt", "payment.txt")           # replace the name of the temp_file with "payment.txt"
        ans = try_again("delete another payment record")
        if (ans):  # ans == True
            continue
        else:  # ans == False
            break


def delete_menu():
    while (True):
        op_list = ["1", "2", "3"]
        print("\nDELETE MENU\n==========\n")
        print("1. Delete Car Records")
        print("2. Delete Payment Records")
        print("3. Go Back to Admin Menu")
        op = input("\nEnter option: ").replace(" ", "")
        if (op in op_list):
            break
        else:
            print("\nInvalid Option. Try Again.")
        #   continue ( since it is a while (True) loop )

    return int(op)


def delete_process():
    while (True):
        admin_ans = delete_menu()           # returns integer 1, 2 or 3
        if (admin_ans == 1):
            delete_car_rec()
            continue
        elif (admin_ans == 2):
            delete_pay_rec()
            continue
        else:                               # admin_ans == 3, head back to "ADMIN MENU"
            break


def admin_action():
    while (True):
        admin_ans = admin_menu()        # returns the number option in  <class integer>
        if (admin_ans == 1):
            add_car_rec()
            continue
        elif (admin_ans == 2):
            mod_car_rec()
            continue
        elif (admin_ans == 3):
            show_all_rec()
            continue
        elif (admin_ans == 4):
            search_specific_rec()
            continue
        elif (admin_ans == 5):
            return_car_chg_status()
            continue
        elif (admin_ans == 6):
            delete_process()
            continue
        elif (admin_ans == 7):
            new_reg("admin_info.txt")
            continue
        else:                       # admin_ans == 8, "Go Back to Main Menu
            break


#   GUEST FUNCTIONALITIES

#       (a)         [Guest Menu]                                                [Verified]


def guest_menu():
    while (True):
        op_list = ["1", "2", "3"]
        print("\nGUEST MENU\n=========\n")
        print("1. View Cars Available For Rent")
        print("2. Sign Up")
        print("3. Exit\n")
        print("Select an option to continue.\n")
        op = input("Enter option: ").replace(" ", "")
        if (op in op_list):
            break
        else:
            print("Invalid option. Try again.")

    return int(op)


#       (b)         [Guest Directory to Each Section in GUEST MENU]             [Verified]

def guest_action():
    while (True):
        guest_ans = guest_menu()                        # returns INTEGER (1, 2 or 3)
        if (guest_ans == 1):
            car_for_rent()
            continue
        elif (guest_ans == 2):
            sign_up_res = new_reg("cus_info.txt")       # guest registration
            if (sign_up_res == "SignUpFail"):
                continue
        else:                                           # guest_ans == 3, "Go Back to Main Menu"
            break


#   REGISTERED USER FUNCTIONALITIES

#       (a)         [Customer Menu]

def cus_menu():                                 # customers are registered users
    while (True):
        op_list = ["1", "2", "3", "4", "5"]
        print("\nCUSTOMER MENU\n==========\n")
        print("1. View Personal Rental History")
        print("2. View Available Cars for Rent")
        print("3. Select and Book a Car")       # for a specific time duration
        print("4. Proceed to Payment")          # to confirm booking
        print("5. Go Back to Main Menu\n")
        op = input("Enter option: ").replace(" ", "")
        if (op in op_list):
            break
        else:
            print("\nInvalid Option. Try Again.")

    return int(op)


def cus_action(username):
    payment_info = []           # important here have to assume the user cannot book more than one car at one sitting
    payment_info.clear()        # so that payment_info list refreshes everytime user wants to make a new car booking
    while (True):
        cus_ans = cus_menu()    # Returns INTEGER, between 1 to 5
        if (cus_ans == 1):
            search_cus_pay("cus", username=username)       # "adm" for admin search, "cus" for customer search, username is keyword argument
            continue
        elif (cus_ans == 2):
            car_for_rent()
            continue
        elif (cus_ans == 3):
            if (len(payment_info) == 0):
                payment_rec_list = car_booking(username)        # return list [duration, start date, end date, username], all in string
                payment_info = payment_rec_list         # assign it to the payment_info (list)
                print("\nChoose option 4 to Proceed with Payment and Confirm Booking.")
                continue
            else:
                print("\nOne customer can only book one car at one sitting.")   # assume one user can only book one car at a time
                continue
        elif (cus_ans == 4):
            if (len(payment_info) == 4):            # since [duration, start date, end date, username] will be here
                payment_info1 = payment_info.copy()     # copy the list into payment_info1
                payment_info.pop()                      # removes an element at the end so that user won't be directed to the function upon selecting option 4 again
                pay_car_booking(payment_info1, username)
                continue
            elif (len(payment_info) == 3):                # Upon removing the last element means if user enter option 4 again, it will just show booking confirmed
                print("\nCar Booking has already been confirmed from", payment_info[1], "to", payment_info[2] + ".")
                continue
            else:
                print("\nCar Booking Not Found!.")
                print("\nChoose option 3 to Select and Book a Car.")
                continue
        else:           # cus_ans == 5
            break


#   [MAIN MENU AND MAIN LOGIC]

while (True):
    print("\nWelcome to SUPER CAR RENTAL SERVICES (SCRS).\n")
    print("MAIN MENU\n=========\n")
    print("1. Admin Staff")
    print("2. Guest User")
    print("3. Registered User")
    print("4. Exit\n")
    print("Select an option to continue.\n")
    op = input("Enter option: ").replace(" ", "")
    if (op == "1"):
        res_list = login("admin_info.txt")      # res_list will return ["SignedIn", username] if login successful
        if (res_list[0] == "SignedIn"):
            admin_action()
            #  continue ( since while(True) loop)
        else:                                   # res_list will return "LoginFail" if login unsuccessful
            continue
    elif (op == "2"):
        guest_action()
        #  continue ( since while(True) loop)
    elif (op == "3"):
        res_list = login("cus_info.txt")
        if (res_list[0] == "SignedIn"):         # res_list will return ["SignedIn", username] if login successful
            cus_action(res_list[1])
        else:                                   # res_list will return "LoginFail" if login unsuccessful
            continue
    elif (op == "4"):
        print("\nThanks for surfing SUPER CAR RENTAL SERVICES (SCRS).")
        print("We hope you had a wonderful experience!")
        break
    else:
        print("Invalid option. Try Again.")
