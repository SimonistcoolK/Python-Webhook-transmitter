import requests, time 
print("Transmitter")
msg = input('Enter your message:')
webhook_url = input('Enter your webhook URL:')
data = {
    "content": msg
}
response = requests.post(webhook_url, json=data)
print("sent:", msg, "to webhook no.", webhook_url)

time.sleep(3)
