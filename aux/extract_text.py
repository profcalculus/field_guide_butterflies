import io
import os
from bs4 import BeautifulSoup
from nltk import word_tokenize

def get_text(fname):
    with open(fname) as f:
        soup = BeautifulSoup(f.read())
        for itals in soup.find_all('i'):
            if itals.string:
                txt = unicode(itals.string)
                txt = '[i]'+txt+'[/i]'
                itals.string.replace_with(txt)
        return soup

def extract(outfilename='all_text.txt'):
    infiles = [f for f in os.listdir('.') if f.endswith('.htm')]
    with io.open(outfilename, 'w', encoding='utf8') as outfile:
        for f in infiles:
            soup = get_text(f)
            outfile.write(unicode(soup.get_text()))

def unique_words(outfilename = 'unique_words.txt', fulltextfilename= 'all_text.txt'):
    with io.open(fulltextfilename, encoding='utf8') as infile:
        text = infile.read();
    words = word_tokenize(text);
    words = [w.strip() for w in words]
    unique_words = sorted(list(set(words)))
    with io.open(outfilename, 'w', encoding='utf8') as outfile:
        for w in unique_words:
            outfile.write('%s\n' % w)

if __name__ == '__main__':
    extract()
    unique_words()
