from flask import Flask, render_template, request
import weather


app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")
    
@app.route("/predict", methods = ["GET","POST"])
def predict():
    show = 0
    img_lo = 'img/cntct.jpg'
    if request.method == "POST":
        pcp = request.form["pcp"]
        tmx = request.form["tmx"]
        tmn = request.form["tmn"]
        wind = request.form["wind"]
        test = [pcp,tmx,tmn,wind]
        predict = weather.model_api(test)
        show = predict
    
        if show[1] == 'drizzle':
            img_lo = 'img/light-rain.png'
        elif show[1] == 'fog':
            img_lo = 'img/clouds.png'
        elif show[1] == 'rain':
            img_lo = 'img/rain-3.png'
        elif show[1] == 'snow':
            img_lo = 'img/snow.png'
        elif show[1] == 'sun':
            img_lo = 'img/sun.png'
        
    return render_template("predict.html", para = show , img_lo=img_lo)
    

""" @app.route("/sub", methods = ["POST"])
def submit():
    if request.method == "POST":
        name = request.form["username"]
    return render_template("sub.html", n = name) """



if __name__ == "__main__":
    app.run(debug=True) 