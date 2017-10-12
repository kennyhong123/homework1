from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
@app.route("/miles-to-km")
def render_miles():
    return render_template('miles-to-km.html')
@app.route("/C-to-F")
def render_celcius():
    return render_template('C-to-F.html')
@app.route("/lbs-to-kg")
def render_lbs():
    return render_template('lbs-to-kg.html')

@app.route("/response")
def render_response():
    miles= float(request.args['miles'])
    if 'miles' in request.args:
        reply = float(request.args['miles'])*1.60934
    return render_template('response.html', response = reply)
if __name__=="__main__":
    app.run(debug=False, port=54321)
