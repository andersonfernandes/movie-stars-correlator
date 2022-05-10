from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def root():
  return render_template('root.html')
