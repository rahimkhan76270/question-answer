from flask import Flask,render_template,request,jsonify

app=Flask(__name__)
answer=""
question=""
@app.route("/",methods=['GET',"POST"])
def hello():
    if request.method=="POST":
       global answer,question
       answer=request.form.get("ans")
       question=request.form.get("question")
    return render_template("./index.html")

@app.route("/ans",methods=["GET"])
def ans():
    global answer,question
    return jsonify({"q":question,"ans":answer})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)