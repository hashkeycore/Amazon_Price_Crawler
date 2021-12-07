import smtplib, ssl, os


class MailClient:
    port = 465
    password = os.environ['PASSWORD']
    user = os.environ['USERNAME']
    context = ssl.create_default_context()
    message: str
    sender_mail = "hashiscoding@gmail.com"
    receivers_mail = "hashkey@hotmail.it"

    def set_message(self, price: float, item: str):
        """Sets the parameters for the message"""
        self.message = f"""Subject: {item}, price drop {price}
                        
                        
                        The price of the item you are watching went down, from the
                        original price.
                       """
        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """

    def send_mail(self):
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as mail:
            mail.login(self.user, self.password)
            mail.sendmail(self.sender_mail, self.receivers_mail, self.message)
