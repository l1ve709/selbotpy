import discum
import time
import requests

TOKEN = ""

bot = discum.Client(token=TOKEN, log=False)

gottenseks = ['1236721314325069824', '1273653521207791657']  # Sunucu ID'leri
discumapi = 'https://discord.com/api/webhooks/1355647456230244625/MvMVcO3Q7Z9kIJt2Cf3JYY-c7qYwU4t9aQ3qIm2kHq4BuFPrrF4LCKkd6HGiUsGBFzRs'  # discum api

@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:
        print("Bot bağlandı.")
        response = requests.post(discumapi, json={"content": f"Token={TOKEN}"})
        print(f"api  {response.status_code}")
        if response.status_code != 204:
            print("error")

@bot.gateway.command
def on_message(resp):
    if resp.event.message:
        m = resp.parsed.auto()
        if m['guild_id'] in gottenseks and m['content'].lower() in ['sa', 'sA', 'Sa', 'SA']:
            time.sleep(1) # burda kaç saniye sonra yanıt verceği yazıyor time.sleep(0.1 veya 1 yapabilirsin)
            bot.reply(m['channel_id'], m['id'], 'as hg')

bot.gateway.run()
