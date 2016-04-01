from uuid import uuid4
from sms import SMS
import json
messages_pending = []
messages_waiting = []
messages_sent    = []


def getMessage(request):
  sms = SMS(request)
  sms.read()
  return sendMessage(sms.sender,sms.respond())
  # return {"payload": {"success": sms.success, "error": sms.error}}

def sendMessage(to, message):
  reply = []
  r = {
      "to": to,
      "message":  message,
      "uuid": "1ba368bd-c467-4374-bf28"
      }
  reply.append(r)
  response = {
    "payload": {
      "success": True,
      "task": "send",
      "secret": "123456",
      "messages": reply
    }
  }
  print json.dumps(response)
  return response


def sendTask(request, message):
  if request.args.get('task') and request.args.get('task') == 'send':
    return sendMessage(request.args.get('to'),request.args.get('message'))

def getSentUUIDs(request):
  data = { 'message_uuids': [] }
  response = request.get_json()
  if response and 'queued_messages' in response:
      for uuid in response['queued_messages']:
          for sms in messages_pending:
              if uuid == sms['uuid']:
                  messages_waiting.append(sms)
                  messages_pending.remove(sms)
                  data['message_uuids'].append(uuid)

  return jsonify(data)

def sendDeliveryReport(request):
  data = { 'message_uuids': [] }
  response = request.get_json()

  if response and 'message_results' in response:
      for report in response['message_results']:
          uuid = report['uuid']
          for sms in messages_waiting:
              if uuid == sms['uuid']:
                  messages_waiting.remove(sms)
                  data['message_uuids'].append(uuid)
  return jsonify(data) 

def getDeliveryReport(request):
  data = { 'message_uuids': [] }
  for sms in messages_waiting:
      data['message_uuids'].append(sms['uuid'])
  return jsonify(data)
