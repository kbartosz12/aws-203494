from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return "It works!!"

@app.route("/order-animation")
def order_animation():
  return render_template(
  "order.html",
  invitation="Welcome to ani creator")

@app.route('/Upload')
def upload():
  if 'my_file' not in request.files:
    return "something is not yes"
  upl_file = request.files['my_file']
  storage - new S3Storage(os.get, s3)
  storage.save(path="", body=)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True )


