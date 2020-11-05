import smtplib
import os

def send_email():

    USER = 'loot.price.check@gmail.com'
    APP_PASSWORD = os.environ.get('APP_PASSWORD')

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USER, APP_PASSWORD)

        subject = 'Test'
        body = 'This is a test'

        msg = f'Subject: {subject}\n\n{body}'

        server.sendmail(USER, 'iarchive@hotmail.com', msg)
        
        #server.quit()


#send_email('awood@student.wethinkcode.com', "Test", "This is a test")