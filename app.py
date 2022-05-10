from flask import Flask, render_template, request, url_for, redirect
from correlator import Correlator

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def root():
  source = None
  destination = None
  correlator_data = None

  if request.method  == 'POST':
    source = request.form['source']
    destination = request.form['destination']
    correlator_data = Correlator(source, destination).search()

  return render_template(
    'root.html',
    source=source,
    destination=destination,
    correlator_data=correlator_data
  )
