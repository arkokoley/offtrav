from flask import Flask, render_template, request, url_for

from messageRequest import MessageRequest

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/', methods=['POST'])
def respond():
  success = False
  error = null
  sender = request.form['from']
  message = request.form['message']
  secret = request.form['secret']
  sentTime = request.form['sent_timestamp']
  sentTo = request.form['sent_to']
  messageID = request.form['message_id']
  deviceID = request.form['device_id']
  if sender.len() > 0 and message.len() > 0 and sentTime.len() > 0:
    if secret == '123456':
      success = True
    else:
      error = "The secret value sent from the deviceID."
    send_response(sender,message)
  return render_template('form_action.html', name=name, email=email)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )

