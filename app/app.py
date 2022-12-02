from flask import (
    Flask,
    current_app,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    url_for
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"


#define quetion generator model
from transformers import pipeline

model_path = "sonoisa/t5-base-japanese-question-generation"
pipe = pipeline("text2text-generation", model_path)


#routing
@app.route("/")
def input():
    response = make_response(render_template("input.html"))
    return response


@app.route("/complete", methods=["GET", "POST"])
def input_complete():
    if request.method == "POST":
        context = request.form["context"]
        answer = request.form["answer"]

        #validatioin check
        is_valid = True
        if not context:
            flash("context is necessary")
            is_valid = False

        if not answer:
            flash("answer is necessary")
            is_valid = False

        if not is_valid:
            return redirect(url_for("input"))

        input = generate_input(answer, context)
        question = question_generator(input)

        flash(question)

        return redirect(url_for("input_complete"))
    return render_template("complete.html")   


def generate_input(answer, context):
    answer = 'answer: ' + str(answer)
    context = 'context: ' + str(context)
    input = answer + ' ' + context
    return input

def question_generator(input):
    question = pipe(input)
    return question