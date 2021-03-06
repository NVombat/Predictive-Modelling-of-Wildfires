from dotenv import load_dotenv
import smtplib
import os

load_dotenv()


def send_feedback_mail(
    result: str, email: str = "nv9824@srmist.edu.in", name: str = "Test User"
) -> None:
    """Sends Result Mail To User

    Args:
        Email: User Email ID
        Name: Name Of User
        Message: User Result Message

    Returns:
        None
    """
    backemail_add = os.getenv("BACKEND_MAIL_ADDR")
    backemail_pwd = os.getenv("BACKEND_MAIL_PWD")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(backemail_add, backemail_pwd)

    # User mail subject, body and format of the mail - FROM ADMIN TO USER
    subject1 = "Predictive Modelling of Wildfires: Prediction Results"
    body1 = f"Dear {name} \n\nThank you for using our services! \n\nResult: The probability of a wildfire occurring is {result} % \n\nHope you have a wonderful day! \n\nWarm Regards, \n\nThe Help Team \nWildfire Prediction Team"
    msg1 = f"Subject: {subject1}\n\n{body1}"

    server.sendmail(backemail_add, email, msg1)
    server.quit()


if __name__ == "__main__":
    send_feedback_mail()
