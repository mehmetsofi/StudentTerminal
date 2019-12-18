from application import app, exchange_currency, exchange_graph, marks_graph
from flask import render_template, request, json, Response, abort
import datetime
import re
import json
#from marks_graph import create_lists, drawGraph


class Campus:
    def __init__(self, key, name, lat, long):
        self.key = key
        self.name = name
        self.lat = lat
        self.long = long

class Transport:
    def __init__(self, key, name):
        self.key = key
        self.name = name


# ---------- MANVI ----------
campuses = {
    Campus('gc',  'Guys Campus', 51.503508, -0.087974),
    Campus('sc',  'Strand ', 51.511393, -0.116142),
    Campus('wc',  'Waterloo', 51.506027, -0.113730),
    Campus('Dhc',  'Denmark Hill', 51.468558, -0.091978)
}

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", campuses=campuses )

transports = {
    Transport('w',  'walking'),
    Transport('c',  'cycling'),
    Transport('d',  'driving'),
    Transport('dt', 'driving-traffic')
    }

campus_by_key = {campus.key:campus for campus in campuses}
transport_by_key = {transport.key:transport for transport in transports}

@app.route("/distanceToKings")
def distanceToKings():
    return render_template('distanceToKings.html', campuses=campuses)


campuscode = ''
@app.route("/distanceToKings/<campus_code>")
def select_mode(campus_code):
    campus = campus_by_key .get(campus_code)
    campuscode=campus_code
    if campus:
        return render_template('transport.html',campuscode = campuscode, transports=transports)
    else:
        abort(404)

@app.route('/distanceToKings/<campuscode>/<transport_code>')
def show_campus(campuscode, transport_code):
    campus = campus_by_key.get(campuscode)
    transport = transport_by_key.get(transport_code)
    if campus:
        return render_template('map.html', campus=campus, transport=transport)
    else:
        abort(404)

# ------------- MEHMET -------------
@app.route('/weather')
def weather():
    return render_template('weather.html')


@app.route('/exchange')
def exchange():
    return render_template('exchange.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        # vals = (result.items()).copy()
        print(result['from'])
        # print(result.items().values())
        filename = str(datetime.datetime.now())
        pattern = re.compile('[\W_]+')
        filename = pattern.sub('', filename)
        money = exchange_currency.conversion(result['from'], result['target'], float(result['amount']))
        exchange_graph.graph(result['from'], result['target'], 5, filename)
        return render_template("result.html",result = result, money = money, filename = filename)

# ------------- GHINI -------------
with open('application/graphData.json') as json_file:
    try:
        graphData = json.load(json_file)
    except ValueError:
        graphData=[]

@app.route('/marks_test')
def marks_test():
    return render_template('marks_test.html')

@app.route('/marks',methods = ['POST','GET'])
def marks():
    #if request.method == 'POST':
    courseworks = request.form.get('coursework')
    global module
    module = request.form.get("module")
    courseworks = int(courseworks)
    return render_template("courseworks.html" , courseworks = courseworks, module = module)


@app.route('/requiredMark' , methods = ['POST','GET'])
def requiredMark():
    allCourseworks = request.form
    newList = list()
    for key in allCourseworks.keys():
        newList.append(key)
    sum = 0
    i = 0
    marksLeft = 100
    while(i < len(newList)):
        sum = sum + int(allCourseworks.get(newList[i])) * int(allCourseworks.get(newList[i+1])) / 100
        marksLeft = marksLeft - int(allCourseworks.get(newList[i+1]))
        i = i+2

    return render_template("target_mark.html" , currentMark =sum, marksLeft = marksLeft, module = module)


@app.route('/targetMark', methods = ['POST','GET'])
def targetMark():
    targetMark = request.form
    marksLeftForTarget = float(targetMark.get("targetMark")) - float(targetMark.get("currentMark"))
    achieve = 0
    if marksLeftForTarget > float(targetMark.get("marksLeft")):
        achieve = -1;
    elif(marksLeftForTarget < 0):
        achieve = 0
    else:
        achieve = marksLeftForTarget

    graphData.append({module: float(targetMark.get("marksLeft"))})
    with open('graphData.json', 'w') as json_file:
        json.dump(graphData,json_file)
    return render_template("marks_result.html", achieve = achieve, exam = float(targetMark.get("marksLeft")), module = module)


@app.route('/drawGraph', methods=['POST'])
def drawGraph():
    return render_template("graphs_marks.html")
