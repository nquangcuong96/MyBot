import discord
import logging
import dictionary

"""
client id: 613970064424828945
url = https://discordapp.com/api/oauth2/authorize?client_id={client it}&scope=bot&permissions={permission}
guideBot infor:
    Token: NjEzOTcwMDY0NDI0ODI4OTQ1.XV4qbg.qq2g9elOjT3Ywmqh9qGt0X22u2g
    Permission: 8
    bot url = https://discordapp.com/api/oauth2/authorize?client_id=613970064424828945&scope=bot&permissions=8
"""

logging.basicConfig(level = logging.INFO)

guideBot = discord.Client()

@guideBot.event
async def on_ready():
    print(f"{guideBot.user} is ready")

@guideBot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if message.content.lower() in dictionary.hello_text:
        await message.channel.send(f"Chào {message.author.name}, chúc bạn một ngày vui vẻ", delete_after = 5.0)
        await message.channel.send("Vui lòng vào kênh hướng dẫn sử dụng bot để biết cách dùng", delete_after = 5.0)

    elif message.content.lower() in dictionary.check_text:
        await message.channel.send(f"{message.author.name}, tôi có thể giúp gì cho bạn:", delete_after = 5.0)
        for guide in dictionary.guide_dict:
            await message.channel.send(guide + dictionary.guide_dict[guide], delete_after = 10.0)
        await message.channel.send(f"{message.author.name}, vui lòng dùng lệnh help + số thứ tự để yêu cầu:", delete_after = 5.0)
    
    elif message.content.lower() in dictionary.help_dict:
        for help_text in dictionary.help_dict:
            if message.content.lower() == help_text:
                await message.channel.send(f"{message.author.name}, " + dictionary.help_dict[help_text], delete_after = 15.0)


    elif str(message.author) in dictionary.admin and message.content.lower() in dictionary.logout_text:
        await message.channel.send(f"{guideBot.user} is offline, ask admin to turn me on", delete_after = 5.0)
        await guideBot.close()


guideBot.run("NjEzOTcwMDY0NDI0ODI4OTQ1.XV4qbg.qq2g9elOjT3Ywmqh9qGt0X22u2g")
