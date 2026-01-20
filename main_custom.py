import requests, time
msg = input('Enter your message:')
webhook_url = "https://discord.com/api/webhooks/..." #paste your webhook url here!
data = {
    "content": msg
}
response = requests.post(webhook_url, json=data)
print("sent:", msg)
time.sleep(3)
