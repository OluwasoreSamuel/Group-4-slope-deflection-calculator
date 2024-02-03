from Website import create_app,render_template,Blueprint

app = create_app()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/mainpage")
def mainpage():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)