import pymongo

#function for exporting text file input for
def export_Data(filename):
    export_List = [] #list that will contain the dictionary values of the data
    key_List = ["Poll_Name", "Date", "Sample_Size", "MoE", "Biden (D)", "Trump(R)", "Spread"] #list of keys for each value
    count = 0
    temp_List = []
    with(open(filename, "r")) as infile: #opening the file of raw data
        for line in infile:
            count += 1
            temp_str = line.strip("\n")
            temp_List.append(temp_str if (temp_str != "--") else "null") #i add each line of infile to this temporary list
            if count % len(key_List) == 0: #when 7 items are added
                temp_dict = {} #create a temporary dictionary
                for key, line in zip(key_List, temp_List): #fill in dictionary key values..
                    temp_dict[key] = line
                temp_List = [] # resetting the temporary dictionary
                export_List.append(temp_dict) #appending dictionary to final list
    return export_List

#inserting into database (will be changed considerably over time)
def database_Insertions(data):
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myClient["Polling_Data"]
    mycol = mydb["Trump_Vs_Biden"]

    mycol.insert_many(data)
    for x in mycol.find():
        print(x)







