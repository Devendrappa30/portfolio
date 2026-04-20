from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Optional: Add more routes later if you want to convert the sub-pages into templates too
# @app.route('/services')
# def services():
#     return render_template('service.html')   # example

if __name__ == '__main__':
    app.run(debug=True)
