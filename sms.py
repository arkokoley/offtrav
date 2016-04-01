class SMS(dict):
  def __init__(self,request):
    self.sender = request.form['from']
    self.message = request.form['message']
    self.secret = request.form['secret']
    self.sentTime = request.form['sent_timestamp']
    self.sentTo = request.form['sent_to']
    self.messageID = request.form['message_id']
    self.deviceID = request.form['device_id']
    self.success = False
    self.error = ""

  def check(self):
    if len(self.sender) > 0 and len(self.message) > 0 and len(self.sentTime) > 0:
      if self.secret == '123456':
        self.success = True
        return True
      else:
        self.error = "The secret value sent from the deviceID."
        return False

  def read(self):
    if self.check() == False:
      return self.error

  def respond(self):
    return "Thanks."+self.message

