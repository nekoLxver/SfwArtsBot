import requests

tags_list = ['kitsune', 'neko', 'waifu']


def get_image(temp_url):
    response = requests.get(temp_url)
    if response:
        return response.json()
    else:
        return False
