from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    miles= float(request.args['miles'])
	x=1
    if miles == 0:
        reply = 0
    else:
        reply = miles*0.621371
    return render_template('response.html', response = reply)
if __name__=="__main__":
    app.run(debug=False, port=54321)