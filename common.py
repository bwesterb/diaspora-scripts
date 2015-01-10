import os.path
import logging
import getpass
import diaspy
import bs4

def get_connection():
    c = diaspy.connection.Connection(**_get_login())
    c.login()
    return c

def _get_login():
    login_file = os.path.expanduser('~/.diaspora')
    if os.path.exists(login_file):
        with open(login_file) as f:
            return {'pod': f.readline()[:-1],
                    'username': f.readline()[:-1],
                    'password': f.readline()[:-1]}
    return {'pod': raw_input('pod: '),
            'username': raw_input('username: '),
            'password': getpass.getpass('password: ')}

def contacts_of(c, guid):
    """ Finds the contacts of the user with given GUID """
    ret = set()
    i = 1
    while True:
        found_any = False
        soup = bs4.BeautifulSoup(c.get('people/%s/contacts?page=%s'
                                            % (guid, i)).text)
        for elt in soup.find(id='people_stream').find_all('a'):
            link = elt.get('href')
            if not link.startswith('/people/'):
                continue
            ret.add(link[len('/people/'):])
            found_any = True
        i += 1
        if not found_any:
            break
    return ret

def hovercard(c, guid):
    """ Returns the data on the hovercard for the user with given GUID """
    return c.get('people/%s/hovercard' % guid,
                    headers={'accept': 'application/json'}).json()

