from database_Design import *

mycol = database_Creation()


def find_Averages():
    states = mycol.distinct("State")

    Averages = {}

    for state in states:
        trump_Nums = []
        biden_Nums = []

        pipeline = [
            {"$match": {"State": state}},
            {"$sort": {"Date": -1}},
            {"$limit": 5}
        ]

        recent_Polls = mycol.aggregate(pipeline)

        for each in recent_Polls:
            trump_Nums.append(each["Trump"])
            biden_Nums.append(each["Biden"])

        trump_Average = sum(trump_Nums) / len(trump_Nums)
        biden_Average = sum(biden_Nums) / len(biden_Nums)

        spread = get_Spread(trump_Average, biden_Average)

        Averages[state] = [round(trump_Average), round(biden_Average), spread]
    return Averages


def get_Spread(trump_Num, biden_Num):
    if trump_Num - biden_Num < 1 and trump_Num - biden_Num > 0:
        return "Tie"
    else:
        if trump_Num - biden_Num > 0:
            num = trump_Num - biden_Num
            return "Trump + %d" % num
        else:
            num = biden_Num - trump_Num
            return "Biden + %d" % num

