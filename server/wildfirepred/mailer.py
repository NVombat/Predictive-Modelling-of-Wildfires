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
    MAILGUN_EMAIL = os.getenv("MAILGUN_EMAIL")
    MAILGUN_PWD = os.getenv("MAILGUN_PWD")

    try:
        server = smtplib.SMTP("smtp.mailgun.org", 587)
        server.login(MAILGUN_EMAIL, MAILGUN_PWD)
    except:
        print("Error Connecting To Mail Server")

    # User mail subject, body and format of the mail - FROM ADMIN TO USER
    subject = "Predictive Modelling of Wildfires: Prediction Results"
    body = f"Dear {name} \n\nThank you for using our services! \n\nResult: The probability of a wildfire occurring is {result} % \n\nHope you have a wonderful day! \n\nWarm Regards, \n\nThe Help Team \nWildfire Prediction Team"
    msg = f"Subject: {subject}\n\n{body}"

    try:
        server.sendmail(MAILGUN_EMAIL, email, msg)
    except:
        print("Error Sending Mail")

    server.quit()


if __name__ == "__main__":
    send_feedback_mail()
