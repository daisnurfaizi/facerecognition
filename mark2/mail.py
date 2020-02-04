
# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
#mengirim email ketika ada wajah yang tidak dikenali
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
def tidak():
    fromaddr = "isi email disini yang di gunakan untuk mengirim di sini"
    #toaddr = "bagaswahyuvidiasmoro@gmail.com"
    toaddr = "email penerima"
    #bagaswahyuvidiasmoro@yahoo.com
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    # storing the senders email address   
    msg['From'] = fromaddr 
    #storing the receivers email address  
    msg['To'] = toaddr 
    # storing the subject  
    msg['Subject'] = "Seseorang tidak dikenal berada di dekat rumah anda"
    # string to store the body of the mail 
    body = "Security camera"
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    # open the file to be sent  
    filename = "test.jpg"
    attachment = open('opencv_stranger.jpg', "rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, "Pass word email") 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    # terminating the session 
    s.quit()
#mengirim email ketik ada wajah yang di kenali
def kenal(teman):
    fromaddr = "email pengirim"
    #toaddr = "bagaswahyuvidiasmoro@gmail.com"
    toaddr = "email penerima"
    #bagaswahyuvidiasmoro@yahoo.com
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    # storing the senders email address   
    msg['From'] = fromaddr 
    #storing the receivers email address  
    msg['To'] = toaddr 
    # storing the subject  
    msg['Subject'] = ''+teman+' mengunjungi rumah anda'
    # string to store the body of the mail 
    body = "Security camera"
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    # open the file to be sent  
    filename = "test.jpg"
    attachment = open('opencv'+teman+'.jpg', "rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, "password email pengirim") 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    # terminating the session 
    s.quit() 
