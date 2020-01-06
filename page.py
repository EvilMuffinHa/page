from flask import Flask, render_template, url_for #ok
#ok
app = Flask(__name__)
#ok
@app.route('/')
def index():
  #page
  return render_template("index.html")

#ok
if __name__ == "__main__":
  #page
    app.run(host="0.0.0.0", port=80)

#ok
