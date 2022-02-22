from flask import Flask

app = Flask(__name__)

@app.route("/main", methods = ["POST"])
def main():
    return "Hello Elice!"

@app.route("/Page1", methods = ["POST"])
def Page1():
    return 

@app.route("/Page2", methods = ["POST"])
def Page2():
    return 

@app.route("/Page3", methods = ["POST"])
def Page3():
    return 


if __name__=="__main__":
    app.run('0.0.0.0', port = 5000, debug=True)