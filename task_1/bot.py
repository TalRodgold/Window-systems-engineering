class bot:
    _language="english"
    def __init__(self,sender,maxlength=50):
        self.sender=sender
        self.maxlength=maxlength
    def send(self,message):
        if len(message)<=self.maxlength:
            print(f"sending the message {message} on behalf of{self.sender} using {bot._language}")
        else:
            print("it's too long, can't send")