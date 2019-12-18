from forex_python.converter import CurrencyRates
from datetime import date
import dateutil.relativedelta
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


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

def graph(curFrom, curTo, days, filename):
    #delete the existing graph if exists


    c = CurrencyRates()
    # print(date.today())
    # time = str(date.today())[5:7]
    time2 = date.today()

    # print(time)
    d2 = time2 - dateutil.relativedelta.relativedelta(days=1)
    # print(d2)
    values = []
    dates = []
    i = 0
    while i <= int(days):
        # num = int(str(date.today())[5:7])-1
        ex_rate = c.get_rate(curFrom, curTo, time2)
        #print(ex_rate)
        values.insert(0, ex_rate)
        dates.insert(0, time2)  # str(date.today())[5:7]
        time2 = time2 - dateutil.relativedelta.relativedelta(days=1)
        i -= -1

    # x axis dates in list dates
    # y axis rates in list values

    # setting x and y axis range
    plt.ylim(min(values)*0.998, max(values)*1.002)
    plt.xlim(min(dates), max(dates))
    #
    # plotting the points
    plt.plot(dates, values, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # naming the x axis
    plt.xlabel('date')
    # naming the y axis
    plt.ylabel('exchange rate')

    # giving a title to my graph
    plt.title('Exchange rate last ' + str(days) + ' days.')

    # function to show the plot
    #plt.show()
    print("application/static/"+filename)
    plt.savefig("application/static/"+filename, bbox_inches='tight')

# graph("GBP", "EUR", 5, str(date.today()))
