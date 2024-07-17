import discord
from discord.ext import commands 
import random
import os 
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def mem(ctx):
    lista_de_imagenes = os.listdir('images')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'images/{image_aleatoria}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def que_es_contaminacion(ctx):
    await ctx.send("La contaminación ambiental es la presencia de componentes nocivos, bien sean de naturaleza biológica, química o de otra clase, en el medioambiente, de modo que supongan un perjuicio para los seres vivos que habitan un espacio, incluyendo, por supuesto, a los seres humanos.")
cont = os.listdir("cont_images")

@bot.command()
async def imagenes_de_contaminacion(ctx):
    img_cont = random.choice(cont)
    with open(f'cont_images/{img_cont}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file = picture)
 




bot.run(" TOKEN")
