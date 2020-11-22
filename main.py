from discord.ext import commands
import discord


#画像保存
import requests

#画像トリミング
import cv2
import matplotlib . pyplot as plt

#画像文字化
from PIL import Image
import sys
import pyocr
import pyocr.builders


bot = commands.Bot(command_prefix=['!'])
client = discord.Client()


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('http'):
        print("yes")
        list = (message.content.split())

        URL = list[0]
        image_set = list[1]
        type = list[2]
        print(URL)
        print(image_set)
        file_name = "test.jpg"

        response = requests.get(URL)
        image = response.content

        with open(file_name, "wb") as aaa:
            aaa.write(image)

            img = cv2.imread('test.jpg', 1)
            height = img.shape[0]
            width = img.shape[1]
            if image_set == "flag":
                trim_img1 = img[40:85, 280:425]  # member1
                trim_img2 = img[80:120, 280:425]  # member2
                trim_img3 = img[125:165, 280:425]  # member3
                trim_img4 = img[160:200, 280:425]  # member4
                trim_img5 = img[205:245, 280:425]  # member5
                trim_img6 = img[245:285, 280:425]  # member6
                trim_img7 = img[280:320, 280:425]  # member7
                trim_img8 = img[325:365, 280:425]  # member8
                trim_img9 = img[365:405, 280:425]  # member9
                trim_img10 = img[400:440, 280:425]  # member10
                trim_img11 = img[440:480, 280:425]  # member11
                trim_img12 = img[475:515, 280:425]  # member12
            elif image_set == "3":
                trim_img1 = img[40:85, 280:450]  # member1
                trim_img2 = img[80:120, 280:450]  # member2
                trim_img3 = img[125:165, 280:450]  # member3
                trim_img4 = img[160:200, 280:450]  # member4
                trim_img5 = img[205:245, 280:450]  # member5
                trim_img6 = img[245:285, 280:450]  # member6
                trim_img7 = img[280:320, 280:450]  # member7
                trim_img8 = img[325:365, 280:450]  # member8
                trim_img9 = img[365:405, 280:450]  # member9
                trim_img10 = img[400:440, 280:450]  # member10
                trim_img11 = img[440:480, 280:450]  # member11
                trim_img12 = img[475:515, 280:450]  # member12
            else:
                trim_img1 = img[40:85, 280:470]  # member1
                trim_img2 = img[80:120, 280:470]  # member2
                trim_img3 = img[125:165, 280:470]  # member3
                trim_img4 = img[160:200, 280:470]  # member4
                trim_img5 = img[205:245, 280:470]  # member5
                trim_img6 = img[245:285, 280:470]  # member6
                trim_img7 = img[280:320, 280:470]  # member7
                trim_img8 = img[325:365, 280:470]  # member8
                trim_img9 = img[365:405, 280:470]  # member9
                trim_img10 = img[400:440, 280:470]  # member10
                trim_img11 = img[440:480, 280:470]  # member11
                trim_img12 = img[475:515, 280:470]  # member12

            plt.imshow(trim_img1)
            plt.imshow(trim_img2)
            plt.imshow(trim_img3)
            plt.imshow(trim_img4)
            plt.imshow(trim_img5)
            plt.imshow(trim_img6)
            plt.imshow(trim_img7)
            plt.imshow(trim_img8)
            plt.imshow(trim_img9)
            plt.imshow(trim_img10)
            plt.imshow(trim_img11)
            plt.imshow(trim_img12)

            cv2.imwrite('player1.png', trim_img1)
            cv2.imwrite('player2.png', trim_img2)
            cv2.imwrite('player3.png', trim_img3)
            cv2.imwrite('player4.png', trim_img4)
            cv2.imwrite('player5.png', trim_img5)
            cv2.imwrite('player6.png', trim_img6)
            cv2.imwrite('player7.png', trim_img7)
            cv2.imwrite('player8.png', trim_img8)
            cv2.imwrite('player9.png', trim_img9)
            cv2.imwrite('player10.png', trim_img10)
            cv2.imwrite('player11.png', trim_img11)
            cv2.imwrite('player12.png', trim_img12)

            tools = pyocr.get_available_tools()
            if len(tools) == 0:
                await message.channel.send('image error')
                sys.exit(1)

            tool = tools[0]

            langs = tool.get_available_languages()
            lang = langs[0]

            member1 = tool.image_to_string(
                Image.open('player1.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member2 = tool.image_to_string(
                Image.open('player2.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member3 = tool.image_to_string(
                Image.open('player3.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member4 = tool.image_to_string(
                Image.open('player4.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member5 = tool.image_to_string(
                Image.open('player5.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member6 = tool.image_to_string(
                Image.open('player6.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member7 = tool.image_to_string(
                Image.open('player7.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member8 = tool.image_to_string(
                Image.open('player8.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member9 = tool.image_to_string(
                Image.open('player9.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member10 = tool.image_to_string(
                Image.open('player10.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member11 = tool.image_to_string(
                Image.open('player11.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )
            member12 = tool.image_to_string(
                Image.open('player12.png'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )

            if type == "1":
                num = "1 2 3 4 5 6 7 8 9 10 11 12"
            elif type == "2":
                num = "1 2 3 4 5 6"
            elif type == "3":
                num = "1 2 3 4"
            elif type == "4":
                num = "1 2 3"
            elif type == "5":
                num = "1 2"

            if member1 == "":
                member1 = "error"
            elif member2 == "":
                member2 = "error"
            elif member3 == "":
                member3 = "error"
            elif member4 == "":
                member4 = "error"
            elif member5 == "":
                member5 = "error"
            elif member6 == "":
                member6 = "error"
            elif member7 == "":
                member7 = "error"
            elif member8 == "":
                member8 = "error"
            elif member9 == "":
                member9 = "error"
            elif member10 == "":
                member10 = "error"
            elif member11 == "":
                member11 = "error"
            elif member12 == "":
                member12 = "error"

            send_message_content = "!update" + " " + type + " " + member1 + ", " + member2 + ", " + member3 + ", " + member4 + ", " + member5 + ", " + member6 + ", " + member7 + ", " + member8 + ", " + member9 + ", " + member10 + ", " + member11 + ", " + member12 + "; " + num

            await message.channel.send(send_message_content)
    await bot.process_commands(message) 


bot.run("")
