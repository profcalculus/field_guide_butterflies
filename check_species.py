#!/bin/bash/python

import os

files = [f for f in os.listdir('.') if f.endswith('.htm')]
count = 0
for f in files:
    lines = open(f).readlines()
    count = count + 1
    h5=[l for l in lines if l.startswith('<h5><i>')][0]
    sciname = h5[len('<h5><i>'):-len('</i></h5>')-2]
    genustag = '<b>Genus</b>'
    genus = [l for l in lines if l.startswith(genustag)][0]
    genus = genus[len(genustag)+5:-len('</i><br/>')-2]
    speciestag = '<b>Species</b>'
    species = [l for l in lines if l.startswith(speciestag)][0]
    species = species[len(speciestag)+5:-len('</i><br/>')-2]
    subspeciestag = '<b>Subspecies</b>'
    subspecies = [l for l in lines if l.startswith(subspeciestag)]
    if subspecies:
        subspecies = subspecies[0]
        subspecies = subspecies[len(subspeciestag)+5:-len('</i><br/>')-2]
    else:
        subspecies = ''
    fullname = ' '.join((genus, species, subspecies)).strip()
    if fullname != sciname:
        print 'ERROR in %s: sciname="%s", fullname="%s"' %(f, sciname, fullname)
print '%d files processed' % count
