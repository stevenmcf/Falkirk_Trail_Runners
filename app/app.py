from flask import Flask, render_template

from controllers.runners_controller import runners_blueprint

app = Flask(__name__)

app.register_blueprint(runners_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title = "Falkirk Trail Runners")

if __name__ =='__main__':
    app.run(debug=True)