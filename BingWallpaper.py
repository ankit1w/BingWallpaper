from requests import get
import os


def get_wallpaper_data():
    res = get(f'{base_url}HPImageArchive.aspx?format=js&n=1').json()

    return res['images'][0]['url'], res['images'][0]['hsh']


def hashes_differ(hsh):
    if os.path.exists('BingWallpaper.jpg'):
        with open('BingWallpaper.jpg', 'rb') as wall:
            wall.seek(-32, 2)
            old_hsh = wall.read().decode()

            if hsh == old_hsh:
                return False
    return True


def set_wallpaper(url, hsh):
    with open('BingWallpaper.jpg', 'wb') as wall:
        wall.write(get(base_url+url).content)
        wall.write(hsh.encode())

    os.popen('WallpaperChanger.exe BingWallpaper.jpg')


if __name__ == '__main__':
    base_url = 'http://www.bing.com/'
    os.chdir(os.path.dirname(__file__))

    url, hsh = get_wallpaper_data()

    if hashes_differ(hsh):
        set_wallpaper(url, hsh)
