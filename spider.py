import json
from requests import get

def GetPic():
    api_url = r'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    api = get(api_url)
    json_data = json.loads(api.text)
    pic_url = r'https://www.bing.com{0}'.format(json_data['images'][0]['url'])
    start_date = json_data['images'][0]['startdate']
    open(r'./tmp/json/{0}.json'.format(start_date), 'wb').write(api.content)
    print('Create Json Success!')
    pic = get(pic_url, stream=True)
    if(pic.status_code == 200):
        open(r'./tmp/pic/{0}.png'.format(start_date), 'wb').write(pic.content)
        print('Create Image Success!')
    else:
        print('Create Image Faild!')
    str = '111'
    open('./README.md', 'wb').write(str.encode())
    print('Create md Success!')

if __name__ == "__main__":
    GetPic()