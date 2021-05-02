from pathlib import Path
import webbrowser

from pychartjs import BaseChart, ChartType, Color
import jinja2

class MyBarGraph(BaseChart):

    type = ChartType.Bar

    class data:
        label = "Numbers"
        data = [12, 19, 3, 17, 10]
        backgroundColor = Color.Green

chart = MyBarGraph()

environment = jinja2.Environment(loader=jinja2.FileSystemLoader('./pychart'))

template = environment.get_template('templates/template.html')

renderedPage = template.render(title='Test Page', chartJSON=chart.get())

outputFileName = Path('pychart/output/index.html')

with open (outputFileName, 'w') as outputFile:
    outputFile.write(renderedPage)

webbrowser.open(outputFileName.resolve().as_uri())
