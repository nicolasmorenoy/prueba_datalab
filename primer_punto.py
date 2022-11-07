import requests

from flask import Flask, render_template


app = Flask(__name__)

URL = 'https://catfact.ninja/facts'
response = requests.get(URL)
data = response.json()

results = data["data"]
cat_list = [i["fact"] for i in results]

print(cat_list)



@app.route('/main', methods= ['GET'])
def main():
    return render_template("plantilla.html", result = cat_list)
    #return results

# @app.route('/cats', methods= ['GET'])
# def cats():
#     return cat_api

if __name__ == '__main__':
    app.run(debug=True, port=5000)

