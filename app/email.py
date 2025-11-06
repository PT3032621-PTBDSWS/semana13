import os
import requests

API_KEY = os.getenv("MAILGUN_API_KEY", "")
DOMAIN = os.getenv("MAILGUN_DOMAIN", "")

def send_email(to: str, subject: str, text: str) -> bool:
    """
    Envia e-mail via Mailgun.
    Retorna True se status_code estiver 200/201, caso contrário False.
    """
    if not API_KEY or not DOMAIN:
        # Não configurado
        print("Mailgun não configurado (API_KEY ou DOMAIN ausente).")
        return False

    try:
        resp = requests.post(
            f"https://api.mailgun.net/v3/{DOMAIN}/messages",
            auth=("api", API_KEY),
            data={
                "from": f"Sistema <mailgun@{DOMAIN}>",
                "to": [to],
                "subject": subject,
                "text": text
            },
            timeout=10
        )
        if resp.status_code in (200, 201):
            return True
        else:
            print("Mailgun response:", resp.status_code, resp.text)
            return False
    except Exception as e:
        print("Erro ao enviar email:", e)
        return False
