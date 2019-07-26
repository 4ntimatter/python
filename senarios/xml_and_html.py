from flask import Flask, render_template, request

app = Flask("ma app")


@app.route('/', methods={"GET", "POST"})
def main_page():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        Weight = float(request.form['w'])
        Height = float(request.form['h'])
        bmi = w / (h ** 2)

        if bmi < 20:

        if 20 < bmi < 25:


        if bmi > 25:

     return render_template("test1.html", javab = bmi)

app.run(host="0.0.0.0")
