from dotenv import load_dotenv
import smtplib
import os

load_dotenv()


def send_feedback_mail(
    email: str = "nv9824@srmist.edu.in",
    name: str = "Test User",
    message: str = "Test Message",
) -> None:
    """Sends Result Mail To User

    Args:
        Email: User Email ID
        Name: Name Of User
        Message: User Feedback Message

    Returns:
        None
    """
    backemail_add = os.getenv("BACKEND_MAIL_ADDR")
    backemail_pwd = os.getenv("BACKEND_MAIL_PWD")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(backemail_add, backemail_pwd)

    # User mail subject, body and format of the mail - FROM ADMIN TO USER
    subject1 = "JTVMusicApp: Query/Feedback Received"
    body1 = f"Dear {name} \n\nThank you for reaching out to us! \n\nYour Query/Feedback has been received successfully! \n\nPlease wait until we process the information and get back to you. \n\nHope you have a wonderful day! \n\nWarm Regards, \n\nThe Help Team \nJTVMusicApp"
    msg1 = f"Subject: {subject1}\n\n{body1}"

    server.sendmail(backemail_add, email, msg1)
    server.quit()

if __name__ == "__main__":
    send_feedback_mail()