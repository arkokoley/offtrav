from flask import Flask, make_response, request, url_for, jsonify
from sms import SMS
import smssync
import json

# Initialize the Flask application
app = Flask(__name__)
app.debug = True

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/', methods=['POST'])
def respond():
  # method = request.form.get('_method', '').upper()
  # if method == 'POST'
  print request.args.get('task')
  print SMS(request)
  ret = {}
  if request.args.get('task') and request.args.get('task') == 'result':
      print request
      ret = smssync.getDeliveryReport(request)
  elif request.args.get('task') and request.args.get('task') == 'sent':
      print request
      ret = smssync.getSentUUIDs(request)
  else:
      print request
      ret = smssync.getMessage(request)
  ret = json.dumps(ret)
  response = make_response(ret)
  response.headers["Cache-Control"] = "no-cache, must-revalidate"
  response.headers["Expires"] = "Sat, 26 Jul 2016 05:00:00"
  response.headers["Content-type"] = "application/json; charset=utf8"
  print response
  return response

@app.route('/',methods=['GET'])
def get():
  print request.args.get("task")
  ret = smssync.sendTask(request,"Hello")
  ret = json.dumps(ret)
  response = make_response(ret)
  response.headers["Cache-Control"] = "no-cache, must-revalidate"
  response.headers["Expires"] = "Sat, 26 Jul 2016 05:00:00"
  response.headers["Content-type"] = "application/json; charset=utf8"
  print response
  return response

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("8080")
  )

