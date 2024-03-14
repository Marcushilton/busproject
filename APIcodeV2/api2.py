from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
app = Flask(__name__)

from read_sql import read_MySQL
bus_schedules = []
@app.route("/busSchedule", methods=['GET'])
def searchTask():
    global bus_schedules
    bus_schedules = []
    bus_schedule_list = read_MySQL('buses')
    print(bus_schedule_list)
    print(request.args)
    busRoute = request.args.get("bus_route")
    busTimeStr = request.args.get("bus_time")#time_object = datetime.strptime(time_string, "%H:%M:%S").time()
    #busTime = datetime.strptime(busTimeStr, "%H:%M").time() if busTimeStr != '' else ''
    print(busRoute)
    #print(busTime)
    #print(type(busTime))
    print(bus_schedule_list[0]['ArrivalTime'])
    print(type(bus_schedule_list[0]['ArrivalTime']))
    for el in bus_schedule_list:
        if busTimeStr == '':
            if el['BusStopID'] == busRoute:
                bus_schedules.append(el)
        else:
            busTime = datetime.strptime(busTimeStr, "%H:%M").time()
            time_object = datetime.strptime(el['ArrivalTime'], "%H:%M:%S").time()
            if el['BusStopID'] == busRoute and time_object >= busTime:
                bus_schedules.append(el)
		
    return render_template("index.html",bus_schedules=bus_schedules)

if __name__ == "__main__":
    print("Running app...")
    app.run(debug=True)
