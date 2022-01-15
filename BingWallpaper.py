import requests
import os


def get_wallpaper_data():
    res = requests.get('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1').json()

    return f"http://www.bing.com{res['images'][0]['url']}", res['images'][0]['hsh']


def hashes_differ(hsh):
    if os.path.exists('BingWallpaper.jpg'):
        with open('BingWallpaper.jpg', 'rb') as wall:
            wall.seek(-32, 2)
            new_hsh = wall.read()

            if hsh.encode() == new_hsh:
                return False
    return True

def set_wallpaper(url, hsh):
    with open('BingWallpaper.jpg', 'wb') as wall:
        wall.write(requests.get(url).content)
        wall.write(hsh.encode())

    os.system('WallpaperChanger.exe BingWallpaper.jpg')


if __name__ == '__main__':
    url, hsh = get_wallpaper_data()

    if hashes_differ(hsh):
        set_wallpaper(url, hsh)
        