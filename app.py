from flask import Flask, url_for, redirect, render_template, request
from flask import Flask
import requests
from flask_material import Material
from datetime import datetime

now = datetime.now()

app = Flask(__name__)


@app.route('/class', methods=['POST'])
def Class():
    Current_hour = now.hour
    Current_minute = now.minute
    Current_day = now.today().isoweekday()
    Day_List = [1, 2, 3, 4, 5]
    Day = {"1": "Monday", "2": "Tuesday",
           "3": "Wednesday", "4": "Thursday", "5": "Friday"}
    Subject_Link_List = {"TQM": "https://meet.google.com/lookup/bsfyy3ca5f",
                         "ML": "https://meet.google.com/lookup/dtukxqgoiu",
                         "MC": "https://meet.google.com/lookup/aso4v7rnf6",
                         "ST": "https://meet.google.com/lookup/bsczu3muct",
                         "E-Commerce": "https://meet.google.com/lookup/cmifbfu4jh",
                         "MAD": "https://meet.google.com/lookup/cdwdmb7kup"}
    Monday = {"First": "TQM", "Second": "E-Commerce", "Third": "ST"}
    Tuesday = {"First": "MC", "Second": "ML", "Third": "MAD"}
    Wednesday = {"First": "TQM", "Second": "MC", "Third": "ML"}
    Thursday = {"First": "ST", "Second": "MAD", "Third": "ML"}
    Friday = {"First": "E-Commerce", "Second": "TQM", "Third": "MC"}
    Start_Hour_Limit = 11
    Start_Minute_Limit = 35
    First_Period_time = 11
    Second_Period_time = 12
    Third_Period_time = 14
    End_Minute = 45
    if Current_day in Day_List:
        if Current_hour < Start_Hour_Limit or (Current_hour < Start_Hour_Limit - 1 and Current_minute < Start_Minute_Limit):
            return "Your Class starts at 11 AM"
        else:
            if (Current_hour == First_Period_time and Current_minute <= End_Minute) or (Current_hour == First_Period_time - 1 and Current_minute >= Start_Minute_Limit):
                Current_Period = "First"
            elif (Current_hour == Second_Period_time and Current_minute <= End_Minute) or (Current_hour == First_Period_time and Current_minute > End_Minute):
                Current_Period = "Second"
            elif (Current_hour == Third_Period_time and Current_minute <= End_Minute) or (Current_hour == Second_Period_time + 1 and Current_minute > End_Minute):
                Current_Period = "Third"
            elif ((Current_hour > Second_Period_time) or (Current_hour == Second_Period_time and Current_minute > End_Minute)) and (Current_hour < Third_Period_time):
                return "Lunch Time,Eat Heavily! Sleep Happily:)"
            else:
                return "Your Classes Completed,Hapieee Mood Nsoyy !!!"
            Day_Call = Day.get(str(Current_day))
            Subject = eval(Day_Call).get(Current_Period)
            Current_Class_Link = Subject_Link_List.get(Subject)
            return redirect(Current_Class_Link)
    else:
        return "No Worries Enjoyyy Your Holidays"


@app.route('/')
def home():
    return render_template('tt.html')


if __name__ == '__main__':
    app.run(debug=True)
