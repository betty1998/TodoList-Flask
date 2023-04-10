from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__,template_folder="templates")

todos = [{"Task":"Buy batteries","Done":False}]

@app.route("/")
def index():
    return render_template("index.html",todos = todos)

@app.route("/add", methods = ["POST"])
def add():
    todo = request.form['todo']
    todos.append({"Task":todo,"Done":False})
    return redirect(url_for("index"))

    
@app.route("/edit/<int:id>", methods = ["POST","GET"])
def edit(id):
    todo = todos[id]
    if request.method == "POST":
        todo["Task"] = request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html",todo = todo, id = id)
    
@app.route("/check/<int:id>")
def check(id):
    todos[id]["Done"] = not todos[id]["Done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    todos.pop(id)
    return redirect(url_for("index"))
    
    
if __name__ == '__main__':
    app.run(debug = True)
    