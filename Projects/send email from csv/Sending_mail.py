import smtplib
import csv


def get_credentials(filepath):
    with open("credentials.txt", "r") as f:
        Email_Address = f.readline()
        Email_Pass = f.readline()
    return (Email_Address, Email_Pass)


def login(email_address, email_pass, s):
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login(email_address, email_pass)
    print("login")



def Send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    Email_Address, Email_Pass = get_credentials("./credentials.txt")
    login(Email_Address, Email_Pass, s)
    

    # message to be sent
    subject = "Welcome to python"
    body = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
    message = f"Subject : {subject} \n\n {body}"

    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for email in spamreader:
            s.sendmail(Email_Address, email[0], message)
            print("Send To " + email[0])

    # terminating the session
    s.quit()
    print("sent")


if __name__ == "__main__":
    Send_mail()