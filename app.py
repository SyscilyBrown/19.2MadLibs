from distutils.log import debug
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.debug = True
#Key  is made up, and is a requirement for debug toolbar
app.config['SECRET_KEY'] = "here's the secret key"
toolbar = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """get story prompts"""
    prompts = story.prompts
    return render_template("questions.html", prompts = prompts)


@app.route("/story")
def show_story():

    text = story.generate(request.args)
    return render_template("story.html", text = text)