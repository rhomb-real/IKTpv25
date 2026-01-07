import smtplib, ssl
#import imghdr
from email.message import EmailMessage
#njvq lzcd kdvm mgra
def saada_email(saaja_email):
    kiri="Tere! See on test e-kiri Pythonist."
    teema="Test e-kiri Pythonist"
    saatja_email="guskovkostya.15@gmail.com"
    parool=input("Sisesta rakenduse parool: ")
    smtp_server="smtp.gmail.com"
    port=587 #465
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri, subtype='html')
    msg["Subject"]=teema
    msg["From"]=saatja_email
    msg["To"]=saaja_email
    # with open('image.jpg', 'rb') as file:
    #     image_data = file.read()
    # msg.add.attachment(image_data, maintype='image'),
    # subtype=imghdr.what(None, image_data)
    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email, parool)
            server.send_message(msg)
        print("E-kiri saadetud!")
    except Exception as e:
        print(f"Midagi läks valesti... {e}")

kellele=input("Sisesta saaja e-posti aadress: ")
print("Saadan e-kirja...")   
saada_email(kellele)

#oleinik.marina@gmail.coms