import requests
from requests.api import request
# from bs4 import BeautifulSoup 


url = 'https://visualstudio.microsoft.com/wp-content/uploads/2017/02/Packages-1.png'
file_name = 'img_random' +'.jpg'
try:
    
    r = requests.get(url, allow_redirects=True)


    print(r.headers.get('content-type'))
    open(file_name, 'wb').write(r.content)
except:
    print("ça a merder")




# ------ utilise pytube --------
# import pytube

# url = 'https://youtu.be/VXn53EqJRAY'

# youtube = pytube.YouTube(url)
# video = youtube.streams.first()
# video.download('E:\python')