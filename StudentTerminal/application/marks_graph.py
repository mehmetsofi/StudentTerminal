from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import json;
# import io
# import random
#
# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig
#
# output = io.BytesIO()
# FigureCanvas(create_figure()).print_png(output)
#
module = list()
exam = list()
def create_lists():
    listToReturn = list();
    global module
    global exam
    with open('graphData.json') as json_file:
        try:
            graphData = json.load(json_file)
        except ValueError:
            graphData = []

    for i in range(len(graphData)):
        for (key) in graphData[i]:
            module.append(key)
            exam.append(graphData[i].get(key))
    listToReturn.append(module)
    listToReturn.append(exam)
    return listToReturn


def drawGraph(module,exam,filename):
    # x-coordinates of left sides of bars
    left = list(range(len(exam)))

    # heights of bars
    #height = [10, 24, 36, 40, 5]
    height = exam
    # labels for bars
    #tick_label = ['one', 'two', 'three', 'four', 'five']
    tick_label = module

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.7, color=['orange'])

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')
    # plot title
    plt.title('My bar chart!')

    # function to show the plot
    #plt.show()
    plt.savefig("application/static/"+filename, bbox_inches='tight')





drawGraph(['PPA', 'DBS', 'ELA', 'DST'], [70, 80, 60, 50], 'ghini1')
