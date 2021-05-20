from os import listdir
import os
import re
from bs4 import BeautifulSoup
import requests


class Torrent:
    def __init__(self):
        self.session = requests.session()
        self.basePATH = os.getcwd()
        self.CREDENTIALS = {
            # 'uid': os.getenv('UNAME'),
            # 'pwd': os.getenv('PSWRD')
            'uid': os.environ.get('UNAME'),
            'pwd': os.environ.get('PSWRD')
        }
        self.baseURL = 'https://chd4.com/'
        self.indexURL = self.baseURL+'index.php?page='

    def login(self):
        try:
            s = self.session.post(
                f'{self.indexURL}login',
                data=self.CREDENTIALS
            )
            print('\nLogin Successfully....\n')
            return 'OK'
        except Exception as e:
            print('\nLogin Failed....')
            print(f'{e}\n')
            return 'ERROR'

    def get_Torr(self, key: str):
        status = self.login()
        keyword = {'search': key}
        resObj = {'_status': status, 'result': []}

        try:
            s = self.session.post(
                f'{self.indexURL}searchlist',
                data=keyword
            )
            print('\nSearched Successfully...\n')
        except Exception as e:
            resObj['_status'] = 'ERROR'
            print('\nSearch Falied...')
            print(f'{e}\n')

        soup = BeautifulSoup(s.text, 'html.parser')
        results = soup.findAll("a", {"onmouseout": "return nd();"})
        print(f'\nfound {len(results)} results, for keyword {key}\n')

        if len(results) == 0:
            resObj['result'].append(
                {'message': f'No torrent found for key={key}'})

        for r in results:
            resObj['result'].append({
                'title': f'{r.text}',
                'id': f'{r["tfid"]}'
            })

        return resObj

# --------------------------------------------------------------------------------
    def downTorr(self, id: str):
        self.login()
        print(self.basePATH)

        allFile = os.listdir(self.basePATH)
        for file in allFile:
            if file.endswith(".torrent"):
                os.remove(os.path.join(self.basePATH, file))

        title = self.getTitle(id)

        # Downloading the torrent
        url = f'{self.baseURL}download.php?id={id}'
        try:
            s = self.session.get(url, allow_redirects=True)
            soup = BeautifulSoup(s.text, 'html.parser')

            # Checking if the torrent is valid or not
            if s.text == 'Can&rsquo;t find torrent file!':
                print(f'Invalid ID: {id}.................')
                return None
            # else save the file
            else:
                open(f'{self.basePATH}/{title}.torrent', 'wb').write(s.content)
                print('\nTorrent Downloaded successfully.......')
        except Exception as e:
            print('\nFile Saving Failed......\n')
            print(e)
        return title

    def getRecent(self):
        self.login()
        s = self.session.post(self.baseURL)
        resObj = {'_status': 'OK', 'result': []}
        soup = BeautifulSoup(s.text, 'html.parser')
        a = soup.find('ul', {'id': 'crazysl'})
        allTorr = a.findAll('a')
        for i in allTorr:
            id = i['tfid']
            title = self.getTitle(id)
            resObj['result'].append({'title': title, 'id': id})
        return resObj

    def getTitle(self, id: str):
        url = f'{self.indexURL}topics&id={id}'
        try:
            s = self.session.get(url, allow_redirects=True)
            soup = BeautifulSoup(s.text, 'html.parser')
            title = soup.find('h3', {'class': 'torrent-title text-primary'})
            title = title.get_text()
            return title
        except Exception as e:
            # print(e)
            return None
# />
