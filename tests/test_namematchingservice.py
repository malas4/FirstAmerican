import json
import pytest
import logging


f= open('C://Users//Nihaan//PycharmProjects//FirstAmerican//FileA.json')
f2= open('C://Users//Nihaan//PycharmProjects//FirstAmerican//FileB.json')
data1 = json.load(f)
data = json.load(f2)



def test_buyer_owner_last_names_matched():
    buyer_names = data1['Buyer']
    owner_names = data['AssessRecord']['Owners']
    for i in range(len(buyer_names)):
        buyer_name = buyer_names[i].split()
        print(buyer_name)
        buyer_last_name = buyer_name[0][0:4]

        for j in range(0, len(owner_names)):
            owner_name = owner_names[j].split()
            print(owner_name)
            temp = owner_name[0][0:4]
            print(temp)
            if buyer_last_name.lower() != temp.lower():
                IsnameMatched = False
                print("names do not match")
                assert False
            else:
                IsnameMatched = True
                assert True
                break














