from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageFont
import random

user_name = input("Please enter your name: ")

image = Image.new('RGBA', (1500, 1500))
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
draw = ImageDraw.Draw(image)
draw.rectangle([(450, 450), (800, 850)], fill = "black")
draw.rectangle([(500, 500), (750, 750)], fill = random.choice(colors))
draw.ellipse([(550, 575), (575, 600)], fill = "white")
draw.ellipse([(675, 575), (700, 600)], fill = "white")
draw.arc([(500, 650), (675, 675)], 0, 90, fill = "white")
draw.text((600, 800), user_name, fill = "white")

image.save("hw02_netflix.png") 
