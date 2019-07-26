from flask import Flask
app = Flask("ma app")


def render_html(filename):
    f = open(filename)
    text = f.read()
    f.close()
    return text


@app.route('/')
def main_page ():
    return render_html("antimatter.html")


app.run()