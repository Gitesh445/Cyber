import smtplib, ssl



def sendemail(message) :
    smtp_server ="smtp.gmail.com"
    port = 587
    sender_email = ""
    password = ""
    reciever_email = ""

    context =ssl.create_default-context()


    try :
        server =smtplib.SMTP(smtp_server ,port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email , password)
        server.sendemail(sender_email,reciever_email,message)

    except Exception as e:
        print(e)
    finally:
        server.quit()        
