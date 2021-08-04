from flask import Flask,render_template,request
import requests



app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method =="POST":
        return render_template("index.html",info = indexPOST())
    else:
        return render_template("index.html")


def indexPOST():
    d_1 = request.form.get("d-1")
    d_2 = request.form.get("d-2")
    miktar = request.form.get("miktar")
    url = "http://data.fixer.io/api/latest?access_key=56e4f46c90223458fde9fd92e590d51e&format=1"
    response = requests.get(url)
    json_data = response.json()
    result = float(miktar) *( json_data["rates"][d_2] / json_data["rates"][d_1])
    info = {
        "d_1":d_1,
        "d_2":d_2,
        "miktar":miktar,
        "result":str(result),
    }
    return info




if __name__ == "__main__":
    app.run(debug=True)