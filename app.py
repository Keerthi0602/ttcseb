from flask import Flask, url_for, redirect, render_template, request
from flask import Flask
import re
import os
import pytz
import requests
from datetime import datetime

now = datetime.now(pytz.timezone('Asia/Kolkata'))

app = Flask(__name__)


@app.route('/class', methods=['POST'])
def Class():
    if Current_Class_Link != "":
        return redirect(Current_Class_Link)


@app.route('/')
def home():
    global Day
    global Current_day
    global Current_Period
    global Current_Class_Link
    Current_Class_Link = "/"
    Current_hour = now.hour
    Current_minute = now.minute
    Current_day = now.today().isoweekday()
    Day_List = [1, 2, 3, 4, 5, 6]
    Day = {"1": "Monday", "2": "Tuesday",
           "3": "Wednesday", "4": "Thursday", "5": "Friday"}
    Subject_Link_List = {"PE": "https://meet.google.com/lookup/fss2xwvboq",
                         "BEA": "https://meet.google.com/lookup/gkdm57btgy",
                         "SQA": "https://meet.google.com/lookup/aaclg4o7su",
                         "ED": "FREE",
                         "SPM": "https://meet.google.com/ifc-eshv-ffp",
                         }
    Monday = {"First": "PE", "Second": "BEA",
              "Third": "SPM", "Fourth": "ED", "Fifth": "SQA"}
    Tuesday = {"First": "SPM", "Second": "PE",
               "Third": "SQA", "Fourth": "BEA", "Fifth": "ED"}
    Wednesday = {"First": "SPM", "Second": "ED",
                 "Third": "BEA", "Fourth": "SQA", "Fifth": "PE"}
    Thursday = {"First": "BEA", "Second": "SQA",
                "Third": "SPM", "Fourth": "PE", "Fifth": "ED"}
    Friday = {"First": "SQA", "Second": "ED",
              "Third": "PE", "Fourth": "SPM", "Fifth": "BEA"}
    Start_Hour_Limit = 8
    Start_Minute_Limit1 = 45
    Start_Minute_Limit2 = 00
    First_Period_time = 9
    Second_Period_time = 10
    Third_Period_time = 11
    Fourth_Period_time = 12
    Fifth_Period_time = 14
    End_Minute1 = 00
    End_Minute2 = 45
    if Current_day in Day_List:
        if Current_day == 6:
            return render_template('tt.html', sub="https://meet.google.com/lookup/fuiwflhayp", name="PROJECT", double=False, Monday=Monday, Tuesday=Tuesday, Wednesday=Wednesday, Thursday=Thursday, Friday=Friday)
        elif (Current_hour < Start_Hour_Limit) or (Current_hour == Start_Hour_Limit and Current_minute < Start_Minute_Limit1):
            return render_template('tt.html', name="Your Class starts at 9.00 AM", double=False, Monday=Monday, Tuesday=Tuesday, Wednesday=Wednesday, Thursday=Thursday, Friday=Friday)
        else:
            if (Current_hour == First_Period_time and Current_minute <= End_Minute2) or (Current_hour == First_Period_time - 1 and Current_minute >= Start_Minute_Limit1):
                Current_Period = "First"
            elif (Current_hour == Second_Period_time and Current_minute <= End_Minute2) or (Current_hour == First_Period_time and Current_minute > End_Minute2):
                Current_Period = "Second"
            elif (Current_hour == Third_Period_time and Current_minute >= End_Minute1) or (Current_hour == Second_Period_time and Current_minute > Start_Minute_Limit1):
                Current_Period = "Third"
            elif (Current_hour == Fourth_Period_time and Current_minute >= End_Minute1) or (Current_hour == Third_Period_time and Current_minute >= End_Minute1):
                Current_Period = "Fourth"
            elif (Current_hour == Fifth_Period_time and Current_minute >= End_Minute1) or (Current_hour == Fourth_Period_time + 1 and Current_minute > End_Minute2):
                Current_Period = "Fifth"
            elif (Current_hour > Fourth_Period_time and Current_minute < End_Minute2):
                return render_template('tt.html', name="Lunch Time,Eat Heavily! Sleep Happily:)", double=False, Monday=Monday, Tuesday=Tuesday, Wednesday=Wednesday, Thursday=Thursday, Friday=Friday)
            else:
                return render_template('tt.html', name="Your Classes Completed,Hapieee Mood Nsoyy !!!", double=False, Monday=Monday, Tuesday=Tuesday, Wednesday=Wednesday, Thursday=Thursday, Friday=Friday)
            Day_Call = Day.get(str(Current_day))
            Subject = eval(Day_Call).get(Current_Period)
            """if "/" in Subject:
                Sub_Split = re.split("/", Subject)
                Current_Class_Link1 = Subject_Link_List.get(Sub_Split[0])
                Current_Class_Link2 = Subject_Link_List.get(Sub_Split[1])
                return render_template('tt.html', sub1=Current_Class_Link1, sub2=Current_Class_Link2, name=Subject, double=True)
            else:"""
            if Subject == "ED":
                return render_template('tt.html', name="FREE PERIOD", double=False, Monday=Monday, Tuesday=Tuesday, Wednesday=Wednesday, Thursday=Thursday, Friday=Friday)
            else:
                Current_Class_Link = Subject_Link_List.get(Subject)
                return render_template('tt.html', sub=Current_Class_Link, name=Subject, double=False, Monday=Monday, Tuesday=Tuesday, Wednesday=Wednesday, Thursday=Thursday, Friday=Friday)
    else:
        return render_template('tt.html', name="No Worries Enjoyyy Your Holidays", double=False, Monday=Monday, Tuesday=Tuesday, Wednesday=Wednesday, Thursday=Thursday, Friday=Friday)


if __name__ == '__main__':
    app.run(debug=1)
