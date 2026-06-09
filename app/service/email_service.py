from fastapi_mail import FastMail,MessageSchema
from app.config import conf


async def send_invite_by_email(email:str,invite_link: str):
    message = MessageSchema(
        subject="Workspace Invitation",
        recipients=[email],
        body=f"""
        You have been invited to join the workspace.

        Role: MEMBER

        Click the below link to accept the invitation:

        {invite_link}

        The invitation expires in 7 days.
        """,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)