import requests # type: ignore

def sendSlackNotificationEmail(message):
    url = 'https://hooks.slack.com/services/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'
    body = {'text': f'<!channel>\n{message}'}
    requests.post(url, json = body)