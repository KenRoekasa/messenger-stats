import json
from datetime import datetime
from statistics import mean

import pandas

def convert_to_minutes(x):
    return (x / 1000) / 60

f = open("jsons/rob.json")

y = json.load(f)

reply_times = {}


# create dictionary of participants
for participants in y['participants']:
    reply_times[participants['name']] = []

last_sender = y["messages"][0]["sender_name"]
last_time = y["messages"][0]["timestamp_ms"]

for msg in y["messages"]:

    sender = msg["sender_name"]
    time = msg["timestamp_ms"]
    print(msg)

    # if the sender is different from the last sender
    if last_sender != sender:
        reply_times[last_sender].append((int) (last_time-time))
    # calculate the difference

    #store in array

    last_time = time
    last_sender = sender

# calculate the average of the array
# print(convert_to_minutes(mean(reply_times)))
print(reply_times)
print(convert_to_minutes(mean(reply_times["Robert Turff"])))
print(convert_to_minutes(mean(reply_times["Kenny Roekasa"])))