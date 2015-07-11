import string
import random


def strip_cover(infile):
    #  strip header and footer, then store the whole book as a string
    wholebook = infile.read(-1)
    start_string = 'SIR ARTHUR CONAN DOYLE'
    end_string = 'End of the Project Gutenberg EBook'
    start = wholebook.find(start_string)
    end = wholebook.find(end_string)
    content = wholebook[start + len(start_string):end]
    return content


def break_paragraph_into_list(infile):
    # break the whole book into list of paragraphs
    content = strip_cover(infile)
    # DOS text
    # plist = re.split('\n\n', content)
    plist = content.split('\n\n')
    return plist


def scrub_text(infile):
    # clean up text until only words are left in each paragraph
    plist = break_paragraph_into_list(infile)
    delchars = string.punctuation
    # remove any paragraph that is less than 3 words, or empty
    for e in plist:
        if (len(e.strip().split()) < 3):
            plist.remove(e)
    for i in range(len(plist)):
        p = plist[i]
        # remove white spaces and line break
        p = p.strip().replace('\n', ' ')
        # replace -- with space, and preserve hyphenation
        p = p.replace('--', ' ').replace('-', '')
        # remove puctuation
        p = p.translate(str.maketrans('', '', delchars))
        # store lowercase scrubbed text back into list
        plist[i] = p.lower()
    return plist


def store_trigram(infile):
    # build a dictionary of trigrams
    plist = scrub_text(infile)
    t = {}
    w = []
    for p in plist:
        w = p.split()
        i = 0
        while (i < (len(w) - 2)):
            t.setdefault((w[i], w[i + 1]), []).append(w[i + 2])
            i = i + 1
    return t


def gen_text(infile, number_sentences=10):
    # generate a paragraph of n sentences, default to 10
    t = store_trigram(infile)
    n = 0
    paragraph = ''
    while (n <= number_sentences):
        # randomize sentence length between 5 to 35
        slength = random.randrange(5, 36)
        for i in range(slength):
            slist = []
            wkeys = random.sample(list(t.keys()), slength)
            # generate sentence
            for j in wkeys:
                wlist = t[j]
                word = wlist[random.randrange(len(wlist))]
                slist.append(word)
        slist[0] = slist[0].capitalize()
        slist[-1] = slist[-1] + '. '
        sentence = ' '.join(slist)
        paragraph = paragraph + sentence
        n = n + 1
    return paragraph


if (__name__ == '__main__'):
    original = open('sherlock.txt', 'r')
    print(gen_text(original))
    original.close()
