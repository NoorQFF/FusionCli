import requests

try:
    from utils.__secrets import SLACK_BOT_WEBHOOK  # type: ignore
except ImportError:
    SLACK_BOT_WEBHOOK = None  # or "" depending on your convention

def sendSlackNotificationEmail(message):
    if not SLACK_BOT_WEBHOOK:
        print("⚠️ SLACK_BOT_WEBHOOK is not set. Skipping Slack notification.")
        return

    body = {'text': f'<!channel>\n{message}'}
    try:
        response = requests.post(SLACK_BOT_WEBHOOK, json=body)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Failed to send Slack notification: {e}")
