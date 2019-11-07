# model scraping for themodelbot

import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = 'https://www.google.co.in/search?hl=en&authuser=0&tbm=isch&source=hp&biw=1536&bih=674&ei=alLJW5DUOZT5rQGH_ImoAw&q=prabhas+photos&oq=prabhas&gs_l=img.3.2.35i39k1j0l9.1401.10161.0.12826.18.15.3.0.0.0.225.1616.0j6j3.9.0....0...1ac.1.64.img..6.12.1631.0...0.rkqXTy2pMCs'
url2="https://www.google.co.in/search?rlz=1C1CHBF_enIN818IN818&biw=1536&bih=674&tbm=isch&sa=1&ei=dEHPW9S6B8aBvgTM14k4&q=prabhas+photos+saaho+hd&oq=prabhas+photos+saa&gs_l=img.3.1.0l2j0i8i30k1l5j0i8i10i30k1j0i8i30k1l2.3514.4374.0.7192.4.4.0.0.0.0.244.551.0j2j1.3.0....0...1c.1.64.img..1.3.548...0i67k1.0.T3B264QQAM8"
# download page for parsing
page = requests.get(url2)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url2 = image['src']
        response = requests.get(url2)
        if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url2).content)
                f.close()
                x += 1
    except:
        pass



