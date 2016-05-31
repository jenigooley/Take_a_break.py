from twilio.rest import TwilioRestClient

account_sid = "************"
auth_token = "*************"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
     body="I want to bend you over and spank your bare bottom with a hot spatula    ",
    to="9703190852",
    from_="+15162104090 ")

