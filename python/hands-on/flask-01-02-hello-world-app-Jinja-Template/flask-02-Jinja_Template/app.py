from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html", number1 = 7000, number2 = 9000)

@app.route("/function")
def function():
    variable1 = 12
    variable2 = 5
    return render_template("body.html", num1 = variable1, num2= variable2, multp = variable1 * variable2)

if __name__=="__main__":
    app.run(debug=True)