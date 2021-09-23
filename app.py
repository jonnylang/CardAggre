from flask import Flask, render_template, url_for 
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/card')
def card():
    return render_template("card.html")

if __name__ == "__main__":
    app.run(debug=True)
