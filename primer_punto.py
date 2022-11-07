import requests

from flask import Flask, render_template


app = Flask(__name__)

url = 'https://catfact.ninja/facts'
response = requests.get(url)
data = response.json()

results = data["data"]
cat_list = []
for i in results:
    cat_list.append(i["fact"])

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

