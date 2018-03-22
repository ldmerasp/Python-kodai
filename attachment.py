import time
import picamera
import email
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
def funkcija():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(2)
        camera.capture('photo.jpg')
	camera.start_recording('video.h264')
	time.sleep(10)
	camera.stop_recording()
        lastcapture = datetime.datetime.now()
        toaddr = 'ldme.rasp@gmail.com'
        me = 'ldme.rasp@gmail.com'
        subject = 'Aptiktas judesys! ' + str(lastcapture)
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        msg.preamble = "Photo @ "
        fp = open('photo.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
	att = open('video.h264', 'rb')
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((att).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachement; filename = video.h264")
	msg.attach(part)
        try:
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(user = 'ldme.rasp',password = 'ldmeraspberry')
            s.sendmail(me, toaddr, msg.as_string())
            s.quit()
        except SMTPException as error:
            print ("Error: unable to send email")
