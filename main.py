import random
import datetime
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/test/')
def test():
    return render_template('Pdraw.html', utc_dt=datetime.datetime.utcnow())
@app.route('/')
def hello():
    return render_template('hello.html', utc_dt=datetime.datetime.utcnow())
@app.route('/about/')
def about():
    return render_template('about.html', utc_dt=datetime.datetime.utcnow())
@app.route('/play/')
def play():
    return render_template('play.html', utc_dt=datetime.datetime.utcnow())
@app.route('/rock/')
def rock():
    e=random.randrange(3)
    if e==0:
        return render_template('Rdraw.html', utc_dt=datetime.datetime.utcnow())
    elif e==1:
        return render_template('Rlose.html', utc_dt=datetime.datetime.utcnow())
    elif e==2:
        return render_template('Rwin.html', utc_dt=datetime.datetime.utcnow())
    else:
        return render_template('error.html', utc_dt=datetime.datetime.utcnow())
@app.route('/paper/')
def paper():
    e=random.randrange(3)
    if e==0:
        return render_template('Pdraw.html', utc_dt=datetime.datetime.utcnow())
    elif e==1:
        return render_template('Plose.html', utc_dt=datetime.datetime.utcnow())
    elif e==2:
        return render_template('Pwin.html', utc_dt=datetime.datetime.utcnow())
    else:
        return render_template('error.html', utc_dt=datetime.datetime.utcnow())
@app.route('/scissors/')
def scissors():
    e=random.randrange(3)
    if e==0:
        return render_template('Sdraw.html', utc_dt=datetime.datetime.utcnow())
    elif e==1:
        return render_template('Slose.html', utc_dt=datetime.datetime.utcnow())
    elif e==2:
        return render_template('Swin.html', utc_dt=datetime.datetime.utcnow())
    else:
        return render_template('error.html', utc_dt=datetime.datetime.utcnow())
app.run(host='0.0.0.0', port=5000)