import discord
import random
import string
import asyncio
import datetime
import requests
import os
import json
import pyfiglet
import random

from termcolor import colored
from colorama import Fore

from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")

def scale(time):
    defined = 60
    for unit in ["m", "h"]:
        if time < defined:
            return f"{time:.2f}{unit}"
        time /= defined

def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is invalid\n\n"+Fore.RESET)
            exit()

def rnd1(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
def rnd2(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

os.system('cls')
result = pyfiglet.figlet_format("""Discord Tools""", font = "graceful"  )
print (colored(result, 'blue'))
ip = requests.get('https://api.ipify.org').text
x = datetime.datetime.now()
print (colored('''Created by: YSA DEV - YSA DEV - YSA DEV - YSA DEV - YSA DEV''', 'cyan', attrs=['bold'])) 
print (colored('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••', 'green', attrs=['bold']))
print (colored(f"Ξ Follow myGithub : https://github.com/yudhasaputra \nΞ START           : {x} \nΞ Your IP         : {ip} ", 'green', attrs=['bold']))
print (colored('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• \n', 'green', attrs=['bold']))
print (colored('+===================== BOT START! ========================+', 'red', attrs=['bold']))
print (colored('Write ON DISCORD: \n!levelup <number of messages> to Start Level UP', 'cyan', attrs=['bold']))


@client.command()
async def levelup(ctx,amount: int,lay: int,proje):
    kata = [
        "This crypto project is the perfect example of how a project should be run correctly.",
        "The quality of the development team for this crypto project is truly outstanding.",
        "The vision and mission of this crypto project are very inspiring and motivating.",
        "The roadmap for this crypto project is very detailed and helps in understanding the project's goals.",
        "The source code for this crypto project is open and properly audited, showing a high level of transparency.",
        "The community for this crypto project is very active and involved in the development of the project, which is a sign of success.",
        "This crypto project has a transparent mechanism for managing the funds collected, which is a sign of high trust from users.",
        "The documentation for this crypto project is very comprehensive and easy to understand, making it easy for users to understand the project.",
        "The development team for this crypto project is very responsive to user feedback and needs, showing a commitment to the quality of the project.",
        "The marketing strategy for this crypto project is very effective in reaching the right audience.",
        "This crypto project has adequate contingency plans to address potential risks, showing a high level of caution.",
        "This crypto project works with reputable and experienced partners to help develop the project.",
        "The track record for this crypto project is very solid in managing previous projects, showing proven ability in project management.",
        "This crypto project has an effective mechanism for managing conflicts of interest, showing a high level of professionalism.",
        "This crypto project has a clear strategy for increasing adoption and usage of the project, showing a commitment to the sustainability of the project.",
        "The security system for this crypto project is very secure and tested, ensuring the security of user funds.",
        "The privacy policy for this crypto project is very clear and protects user privacy well.",
        "{} merupakan proyek kripto yang sempurna dan terpercaya.".format(proje),
        "Tim pengembang {} sangat profesional dan berpengalaman.".format(proje),
        "Visi dan misi {} sangat inspiratif dan memotivasi.".format(proje),
        "Roadmap {} terperinci dan jelas, memudahkan pemahaman tujuan proyek.",
        "Kode sumber {} terbuka dan teraudit dengan baik, menunjukkan tingkat transparansi yang tinggi.".format(proje),
        "Komunitas {} sangat aktif dan terlibat dalam pengembangan proyek.".format(proje),
        "Mekanisme pengelolaan dana {} transparan dan terpercaya.".format(proje),
        "Dokumentasi {} lengkap dan mudah dipahami.".format(proje),
        "Tim pengembang {} responsif terhadap masukan dan kebutuhan pengguna.".format(proje),
        "Strategi pemasaran {} efektif dalam menjangkau audiens yang tepat.".format(proje),
        "{} is a reliable and perfect crypto project.".format(proje),
        "The development team for {} is highly professional and experienced.".format(proje),
        "The vision and mission of {} are very inspiring and motivating.".format(proje),
        "The roadmap for {} is detailed and clear, making it easy to understand the project's goals.".format(proje),
        "The source code for {} is open and properly audited, showing a high level of transparency.".format(proje),
        "The community for {} is very active and involved in the development of the project.".format(proje),
        "The mechanism for managing funds in {} is transparent and trustworthy.".format(proje),
        "The documentation for {} is comprehensive and easy to understand.".format(proje),
        "The development team for {} is responsive to user feedback and needs.".format(proje),
        "The marketing strategy for {} is effective in reaching the right audience.".format(proje),
        "{} has a secure and tested security system.".format(proje),
        "The privacy policy for {} is clear and protects user privacy well.".format(proje),
        "{} works with reputable and experienced partners.".format(proje),
        "The track record for {} is very solid in managing previous projects.".format(proje),
        "{} has an effective mechanism for managing conflicts of interest.".format(proje),
        "{} has a clear strategy for increasing adoption and usage of the project.".format(proje),
        "This project has an active and involved community in the development of the project.".format(proje),
        "{} continues to update and improve its features to provide maximum benefit for its users.".format(proje),
        "{} has a responsive customer support team that helps in resolving any issues that may arise.".format(proje),
        "{} continues to develop and improve the quality of the project to provide the best value for its users.".format(proje),
        "{} is one of the leading crypto projects in the market today.".format(proje),
        "The value of {}'s token has significantly increased in the past few months.".format(proje),
        "{} has innovative and unique technology that sets it apart from other crypto projects.".format(proje),
        "{} has a team of experts in their field that ensures the success of the project.".format(proje),
        "{} has received support from leading investors in the crypto industry.".format(proje),
        "{} has successfully implemented its projects with success.".format(proje),
        "{} continues to develop its ecosystem to provide more value to its users.".format(proje),
        "{} has an integrated marketing strategy that helps in increasing public knowledge about the project.".format(proje),
        "{} continues to innovate and improve its products to provide the best value for its users.".format(proje),
        "{} has received recognition from various reputable media in the crypto industry.".format(proje),
        "{} is an innovative and leading crypto project in the industry.".format(proje),
        "{} has a team of skilled experts in their field.".format(proje),
        "{} has a clear vision to make this project a future financial solution.".format(proje),
        "{} has shown a strong commitment to transparency and user trust.".format(proje),
        "{} continues to develop and improve its features to provide maximum benefits to its users.".format(proje),
        "{} has set high standards in the industry with its high-quality products.".format(proje),
        "{} has an effective marketing strategy to reach the right audience.".format(proje),
        "{} has a strong security system to protect user funds.".format(proje),
        "{} is continually expanding its reach in the global market.".format(proje),
        "{} has a clear privacy policy to protect user privacy.".format(proje)
    ]
    await ctx.message.delete()
    msgsend = amount
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Sending {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}messages\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Estimated Time: {Fore.WHITE}{scale(msgsend)}\n")
    while msgsend > 0:
        try:
            msgsend -= 1
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Message sent! | Messages left to send: {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}| Estimated Time: {Fore.WHITE}{scale(msgsend)}")
            if msgsend == 0:
                print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All messages was sent")
            output = kata[random.randint(0, 46)]
            # output = rnd1(5) + " " + rnd2(5) + "-" + rnd2(5) + " " + rnd2(5) + "-" + rnd2(5) + " " + rnd1(5)
            message = await ctx.send(output)
            # await asyncio.sleep(2)
            # await message.delete()
        except:
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot send message {Fore.WHITE}#{msgsend}")
            pass
        await asyncio.sleep(1)
        async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
                
            except:
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot delete message {Fore.WHITE}#{msgsend}")
                pass
        await asyncio.sleep(lay) #setdelayhere(s)
    return


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}{error_str}"+Fore.RESET)


Init()
