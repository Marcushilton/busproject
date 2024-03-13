from flask import Flask, render_template, redirect, url_for, request
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
    print(busRoute)
    for el in bus_schedule_list:
        if el['bus_route'] == busRoute:
            bus_schedules.append(el)
    return render_template("index.html",bus_schedules=bus_schedules)

if __name__ == "__main__":
    print("Running app...")
    app.run(debug=True)
