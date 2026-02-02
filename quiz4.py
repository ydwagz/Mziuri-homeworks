#1
from math import *
# i added seat embarks 'c' 'q' 's'

with open("titanic.txt", "r") as tic:
    c = 0
    q = 0
    s = 0
    fare_1 = []
    fare_2 = []
    fare_3 = []
    tickets_1 = 0
    tickets_2 = 0
    tickets_3 = 0
    male_survivors = 0
    female_survivors = 0
    males = 0
    females = 0

    for line in tic:
        data = line.strip().split(",")
        if data[4] == "female":
            if data[1] == "1":
                if data[2] == "3":
                    if data[-1] == "S":
                        s += 1
                    tickets_3 += 1
                    fare_3.append(float(data[-3]))
                elif data[2] == "2":
                    if data[-1] == "C":
                        c += 1
                    fare_2.append(float(data[-3]))
                    tickets_2 += 1
                else:
                    if data[-1] == "Q":
                        q += 1
                    tickets_1 += 1
                    fare_1.append(float(data[-3]))
                female_survivors += 1
            females += 1
        else:
            if data[1] == "1":
                if data[2] == "3":
                    if data[-1] == "S":
                        s += 1
                    fare_3.append(float(data[-3]))
                    tickets_3 += 1
                elif data[2] == "2":
                    if data[-1] == "C":
                        c += 1
                    fare_2.append(float(data[-3]))
                    tickets_2 += 1
                else:
                    if data[-1] == "Q":
                        q += 1
                    fare_1.append(float(data[-3]))
                    tickets_1 += 1
                male_survivors += 1
            males += 1

    print(f"amount of male passengers: {males} there are {floor(males * 100/(males + females))}% of males on the beard")
    print(f"amount of female passengers: {females} there are {floor(females * 100/(males + females))}% of females on the beard")
    print(f"{male_survivors} male passenger survived {floor(male_survivors * 100/(male_survivors + female_survivors))}% of survivors were male")
    print(f"{female_survivors} female passenger survived {floor(female_survivors * 100/(male_survivors + female_survivors))}% of survivors were female")
    print(f'1st class tickets sold: {tickets_1} - {floor(tickets_1 * 100/(tickets_1 + tickets_2 + tickets_3))}% average = {sum(fare_1) / len(fare_1)}')
    print(f'2nd class tickets sold: {tickets_2} - {floor(tickets_2 * 100/(tickets_1 + tickets_2 + tickets_3))}% average = {sum(fare_2) / len(fare_2)}')
    print(f'3rd class tickets sold: {tickets_3} - {floor(tickets_3 * 100/(tickets_1 + tickets_2 + tickets_3))}% average = {sum(fare_3) / len(fare_3)}')


data_base = {
    "passengers":{
        "male": males,
        "female": females,
        "male female passengers %":{
            "male %": (floor(males * 100/(males + females))),
            "female %": (floor(females * 100/(males + females)))
        },
        "male survivors": male_survivors,
        "female survivors": female_survivors,
        "survivors %": {
            "male survivors %": floor(male_survivors * 100/(male_survivors + female_survivors)),
            "female survivors %": floor(female_survivors * 100/(male_survivors + female_survivors)),
        },
    "tickets":{
        "1st class": tickets_1,
        "2nd class": tickets_2,
        "3rd class": tickets_3,
        "tickets %":{
            "1st class": floor(tickets_1 * 100/(tickets_1 + tickets_2 + tickets_3)),
            "2nd class": floor(tickets_2 * 100/(tickets_1 + tickets_2 + tickets_3)),
            "3rd class": floor(tickets_3 * 100/(tickets_1 + tickets_2 + tickets_3))
        },
    "embarks":{
        "S": s,
        "Q": q,
        "C": c,
        }
    }



    }
}


# თეაორია

# 1
#'read', 'write', 'append'
#2
#შეიქმნება ახალი ფაილი ეგეთი სახელით
#3