import pymongo

global mydb
global mycol

def database_Creation():
    try:

        db_Name = "Polling_Data"
        col_Name = "Trump_Vs_Biden_V1"
        myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        global mydb
        global mycol

        mydb = myClient[db_Name]
        mycol = mydb[col_Name]

        return mycol

    except IndexError as err:
        print("IndexError - Script needs more arguments for MongoDB db and col name:", err)
        quit()


import hashlib
def create_New_Key(key_String):
    new_Key = hashlib.md5(key_String.encode()).hexdigest()
    return new_Key


#function for exporting text file input for

def export_Data(filename, list_Check):

    key_List = ["Poll_Name", "Date", "Sample_Size", "MoE", "Trump", "Biden", "Spread", "State"] #list of keys for each value
    count = 0
    temp_List = []
    output_List = []
    with(open(filename, "r")) as infile: #opening the file of raw data
        for line in infile:
            count += 1
            temp_str = line.strip("\n")
            temp_List.append(temp_str if (temp_str != "--") else "null") #i add each line of infile to this temporary list
            if count % len(key_List)  == 0: #when 8 items are added
                count = 0
                temp_dict = {"_id": None} #create a temporary dictionary
                for key, line in zip(key_List, temp_List): #fill in dictionary key values..
                    temp_dict[key] = line
                temp_dict["_id"] = create_New_Key(temp_dict["Poll_Name"] + temp_dict["Date"] + temp_dict["Sample_Size"] + temp_dict["MoE"] + temp_dict["Spread"])

                temp_List = [] # resetting the temporary dictionary
                if check_If_Duplicate(temp_dict, output_List) == False:

                    database_Insertions(temp_dict, list_Check)
                    output_List.append(temp_dict["_id"])
    print("\n")
    print("___________________________")
    print("Finished Updating Database")
    print("___________________________")
    print("\n")
    for poll in mycol.find():
        print(poll)


#inserting into database (will be changed considerably over time)
from pymongo.errors import BulkWriteError
from datetime import datetime
def database_Insertions(data, list):
    #safe states for dems who dont have rcp averages... will be removed once more polling data and rcp averages are added for each state
    safe_Blue = ["California", "Oregan", "Washington", "Neveda", "Colorado", "New Mexico", "Minnesota", "Illinois", "Maryland", "Delaware", "Connecticut", "Rhode Island", "Connecticut", "Vermont" , "Maine"]
    date_String = data["Date"]
    data["Date"] = datetime.strptime(date_String, '%Y-%m-%d')
    if data["Date"] > datetime.now():
        return
    try:
        data["Biden"] = int(data["Biden"])
        data["Trump"] = int(data["Trump"])
        for sub_List in list:
            if data["State"] == sub_List[0]:
                if "Biden" in sub_List[1]:
                    data["Trump"], data["Biden"] = data["Biden"], data["Trump"]
                    break

        #eventually we wont need these lines of code
        for state in safe_Blue:
            if data["State"] == state:
                data["Trump"], data["Biden"] = data["Biden"], data["Trump"]
                break

        mycol.insert_one(data)
        print(data, "has been inserted")
    except BulkWriteError as bwe:
        print("Duplicate Key Value!, Poll already exists in database wont be written...", bwe.details)
    except TypeError as t:
        print(t, data)


def check_If_Duplicate(data_To_Be_Inserted, list_Of_Ids): #info will be a small list which contains the name and date of the poll being inserted
    duplicate_State = False
    if not list_Of_Ids:
        return duplicate_State

    print(list_Of_Ids)
    if data_To_Be_Inserted["_id"] in list_Of_Ids:
        duplicate_State = True
        print(data_To_Be_Inserted, "is a duplicate and will not be added into the database")
    return duplicate_State




