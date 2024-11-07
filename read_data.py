import json
from datetime import datetime
import random


with open('data.json', 'r', encoding='utf-8') as file:
    parsed_data = json.load(file)


def azkarElsabah():
    data = []
    for item in parsed_data["أذكار الصباح"]:
        if len(item["content"])< 500:
            data.append(item["content"])
    return data


def azkarElmasaa():
    data= []
    for item in parsed_data["أذكار المساء"]:
        if len(item["content"])< 500:
            data.append(item["content"])
    return data


def azkarB3dAlsalamMnElsalah():
    data = []
    for item in parsed_data["أذكار بعد السلام من الصلاة المفروضة"]:
        if len(item["content"])< 500:
            data.append(item["content"])
    return data


def tasabeh():
    data = []
    for item in parsed_data["تسابيح"]:
        if len(item["content"])< 500:
            data.append(item["content"])
    return data


def ad3iaQuraniah():
    data = []
    for item in parsed_data["أدعية قرآنية"]:
        if len(item["content"])< 500:
            data.append(item["content"])
    return data


def ad3iatElanbiaa():
    data = []
    for item in parsed_data["أدعية الأنبياء"]:
        if len(item["content"])< 500:
            data.append(item["content"])
    return data


def get_data():
    data = []
    data.extend(ad3iaQuraniah())
    data.extend(azkarB3dAlsalamMnElsalah())
    data.extend(ad3iatElanbiaa())
    data.extend(tasabeh())
    current_time = datetime.now().time()
    if current_time < datetime.strptime('12:00 PM', '%I:%M %p').time():
        data.extend(azkarElsabah())
    else:
        data.extend(azkarElmasaa())
    return random.choice(data)







