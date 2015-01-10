
import sys
from common import *

def tick():
    sys.stdout.write('.')
    sys.stdout.flush()

def main():
    c = get_connection()
    print "I am searching for the contacts of your contacts that aren't your contacts "
    contacts = frozenset([p['guid'] for p in diaspy.people.Contacts(c).get()])
    ccontacts = set()
    lut = dict()
    hcs = dict()

    for contact in contacts:
        tick()
        if not contact in hcs:
            hcs[contact] = hovercard(c, contact)
        for ccontact in contacts_of(c, contact):
            if ccontact in contacts:
                continue
            if ccontact not in lut:
                lut[ccontact] = []
                tick()
                assert ccontact not in hcs
                hcs[ccontact] = hovercard(c, ccontact)
            lut[ccontact].append(contact)

    print
    for ccontact, parents in  sorted(lut.iteritems(), key=lambda x: -len(x[1])):
        print "%-30s %-20s contact of %s" % (
                   hcs[ccontact]['name'],
                   '('+hcs[ccontact]['handle']+')',
                   ', '.join([hcs[parent]['name'].split(' ')[0]
                           for parent in parents]))

if __name__ == '__main__':
    main()
