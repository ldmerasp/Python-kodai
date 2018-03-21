import time
import picamera
import email
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
def funkcija():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('photo[i].jpg')
        lastcapture = datetime.datetime.now()
        toaddr = 'ldme.rasp@gmail.com'    # redacted
        me = 'ldme.rasp@gmail.com' # redacted
        subject = 'Aptiktas judesys! ' + str(lastcapture)
        #f_time = datetime.now().strftime('%a %d %b @ %H:%M')
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        msg.preamble = "Photo @ " #+ f_time
        fp = open('photo.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
        try:
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(user = 'ldme.rasp',password = 'ldmeraspberry')
            #s.send_message(msg)
            s.sendmail(me, toaddr, msg.as_string())
            s.quit()
            #except:
            #   print ("Error: unable to send email")
        except SMTPException as error:
            print ("Error: unable to send email")