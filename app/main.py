from flask import Flask
app = Flask(__name__)

#Normal nginx app display
#test123 pipeline
@app.route("/")
def hello():
    return "Hello it's XLR/XLD/K8 deployment with deploy_to_k8  from community repo final test v 2.9.0"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
