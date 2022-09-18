import time
import requests

while True:
        def dw_img(img_name: str) -> None:
                url = "https://picsum.photos/1920/1080"
                headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                        'accept-language': 'ru-KZ,ru;q=0.9,en-GB;q=0.8,en;q=0.7,kk-KZ;q=0.6,kk;q=0.5,az-AZ;q=0.4,az;q=0.3,ru-RU;q=0.2,en-US;q=0.1,sm;q=0.1',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                }
                response = requests.get(url=url, headers=headers)
                with open(f'images/{img_name}.jpeg', mode="wb") as file:
                        file.write(response.content)
                time.sleep(0.1)


        for i in range(1, 11):
                dw_img(f'imgn{i}')
