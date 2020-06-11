import pymongo

def database_Creation():
    try:

        db_Name = "Polling_Data"
        col_Name = "Trump_Vs_Biden_V1"
        myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        global mydb
        global mycol
        mydb = myClient[db_Name]
        mycol = mydb[col_Name]

    except IndexError as err:
        print("IndexError - Script needs more arguments for MongoDB db and col name:", err)
        quit()


import hashlib
def create_New_Key(key_String):
    new_Key = int(hashlib.sha256(key_String.encode('utf-8')).hexdigest(), 16) % 10**8
    return new_Key

#function for exporting text file input for

def export_Data(filename):
    export_List = [] #list that will contain the dictionary values of the data
    key_List = ["Poll_Name", "Date", "Sample_Size", "MoE", "Biden (D)", "Trump(R)", "Spread", "State"] #list of keys for each value
    count = 0
    temp_List = []
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
                if check_If_Duplicate(temp_dict) == True:
                    print("Poll entry", temp_dict, "is already in database, moving to next entry")
                else:
                    export_List.append(temp_dict) #appending dictionary to final list
    return export_List


#inserting into database (will be changed considerably over time)
from pymongo.errors import BulkWriteError
def database_Insertions(data):
    try:
        mycol.insert_many(data)
    except BulkWriteError as bwe:
        print("Duplicate Key Value!, Poll already exists in database wont be written...", bwe.details)

    for x in mycol.find():
        print(x)

def check_If_Duplicate(data_To_Be_Inserted): #info will be a small list which contains the name and date of the poll being inserted
    duplicate_State = False
    print(data_To_Be_Inserted)
    print(data_To_Be_Inserted["_id"])

    all_Ids = mycol.find({}, {"_id": 1})
    output_List = [i.get("_id") for i in all_Ids]
    if data_To_Be_Inserted["_id"] in output_List:
        duplicate_State = True
    return duplicate_State




