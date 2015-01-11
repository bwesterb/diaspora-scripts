Some scripts to play with Diaspora

Prerequisites
-------------

    git clone https://github.com/marekjm/diaspy
    sudo python diaspy/setup.py install
    git clone https://github.com/bwesterb/diaspora-scripts
    sudo pip install requests
    cd diaspora-scripts

If you get *hostname doesn't match* errors, run

    sudo apt-get install python-openssl python-pyasn1
    sudo pip install ndg-httpsclient

If you do not like to type your POD url, username and password
everytime, store them in a file named `~/.diaspora` as follows

    https://url.to.pod.com
    username
    password

Don't forget to run `chmod og-r ~/.diaspora`.

`suggest-contacts.py`
--------------------

    $ python suggest-contacts.py 
    I am searching for the contacts of your contacts that aren't your contacts 
    ..............................................
    xxxxx xxxxxx                   (xxxxxxxxxxx@xxxxxxx.com) contact of xxxx, xxxxx, xxxxxxx
    xxx@xxxxxxxxxxxxxxxxxxx        (xxxxxxxx@xxxxxxxxxx.nl) contact of xxxx, xxxxx, xxxxxxx
    xxxx xxx-xxxxxxxx              (xxxxxxxxxxxx@xxxxxx) contact of xxxxx, xxxxxxx
    xxxxx xxxxxxxxxx               (xxxxxxxx@xxxxxxxxxxxxxx) contact of xxxx, xxxxx
