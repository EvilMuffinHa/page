from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
  return redirect("https://joshwang.me/r/pe", code=302)
  return redirect("https://evilmuffinha.github.io/r/a.html", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
