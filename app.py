from flask import Flask, request, render_template
app = Flask(__name__)

# 1. Open both methods, GET, POST
@app.route('/add_food', methods=["GET", "POST"])
def add_food():
  if request.method == "GET":
    return render_template("food_form.html")
  elif request.method == "POST":
    form = request.form
    t = form["title"]
    l = form["link"]
    # Create
    print(t, l)
    return "POST"

@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("register_form.html")
  elif request.method == "POST":
    form = request.form
    u = form["username"]
    p = form["password"]
    print(u, p)
    return "Registered"

if __name__ == '__main__':
  app.run(debug=True)