from flask import Flask,render_template,Markup,session,request
import random

app = Flask(__name__)
app.secret_key = '2021'

@app.route("/")
def index():
    number = random.randint(1,100)
    print(number)
    if "num" not in session:
        session["num"] = number
    return render_template("index.html")

@app.route("/checknum", methods=["POST"])
def checkNumber():
    number_input = int(request.form["input_num"])
    random_num = session["num"]
    boxText = ""
    boxColor = ""
    resetButton = ""


    if number_input == random_num:
        boxColor = "green"
        boxText = "You've Guessed the number!"
        resetButton = Markup('<a href="/"><button type="submit" class="btn btn-primary subbut" value="Submit">Try Again</button><a>')
        session.clear()
        return render_template("index.html",boxColor=boxColor, boxText=boxText, resetButton=resetButton)


    if number_input < random_num:
        boxColor = "red"
        boxText = "Too low"
        return render_template("index.html",boxColor=boxColor, boxText=boxText)

    if number_input > random_num:
        boxColor = "red"
        boxText = "Too high"
        return render_template("index.html",boxColor=boxColor, boxText=boxText)





if __name__=="__main__":
    app.run(debug=True)