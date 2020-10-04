from flask import Flask, render_template

# from controllers.segments_controller import segments_blueprint

app = Flask(__name__)

# app.register_blueprint(segments_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title = "Falkirk Trail Runners")

if __name__ =='__main__':
    app.run(debug=True)