


import json


testSubscriptions={
    "test/test1": "Raum1",
    "test/test2": "Raum2",
    "test/test3": "Raum3"
}





try:
    f = open("data\SubscriptionList","wt")

    f.write(json.dumps(testSubscriptions))

    f.close()
except:
    print("LOL")
