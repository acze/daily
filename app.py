from flask import Flask,render_template
import datetime
import random

app = Flask(__name__)
def done():
    when = "Yesterday" if datetime.datetime.today().weekday() != 0 else "On Friday"
    statement = ["I was helping developers with", "I was working on", "I was struggling with"]
    subject = ["AWS", "RDS", "Lambda", "Serverless stuff", "k8s", "IAM", "Linux"]
    objective = ["to improve stability", "to fix a bug", "to bring a new feature", "to improve security"]
    return "{} {} {} {}.".format(when,random.choice(statement),random.choice(subject),random.choice(objective))

def todo():
    today = ["I will pick something else from the backlog", "I have a lot of meetings", "I will continue the efforts", "I want to do some learning"]
    return "Today {}.".format(random.choice(today))

@app.route('/')
def index():
    return render_template('index.html',done=done(),todo=todo())

if __name__ == '__main__':
    app.run(debug=True)
