import nltk
from nltk.corpus import mac_morpho, stopwords

def simplify_tag(t):
    if '+' in t:
        return t[t.index('+')+1]
    else:
        return t

class pos_tagger(object):
    def __init__(self):
        self.lang = 'portuguese'
        self.t0 = None
        self.t1 = None
        self.t2 = None
        self.t3 = None
        self.train = None
        self.test = None
        self.initialize_dataset()
        self.initialize_taggers()

        self.definitions = {
            'ART': 'artigo',
            'ADJ': 'adjetivo',
            'N': 'nome',
            'NPROP': 'nome proprio',
            'NUM': 'numeral',
            'PROADJ': 'pronome adjetivo',
            'PROSUB': 'pronome substantivo',
            'PROPESS': 'pronome pessoal',
            'PRO-KS': 'pronome conectivo subordinativo',
            'PRO-KS-REL': 'pronome conectivo subordinativo relativo',
            'ADV': 'adverbio',
            'ADV-KS': 'adverbio conectivo subordinativo',
            'ADV-KS-REL': 'adverbio relativo subordinativo',
            'KC': 'conjuncao cordenativa',
            'KS': 'conjuncao subordinativa',
            'PREP': 'preposicao',
            'IN': 'interjeicao',
            'V': 'verbo',
            'VAUX': 'verbo auxiliar',
            'PCP': 'participio',
            'PDEN': 'palavra denotativa',
            'CUR': 'simbolo de moeda corrente'
        }

        self.complement = {
            'EST': 'estrangeirismo',
            'AP': 'apostos',
            'DAD': 'dados',
            'TEL': 'telefone',
            'DAT': 'data',
            'HOR': 'hora',

        }

        self.connectors = {
            '|': 'complemento',
            '|+': 'contracoes e eclises',
            '|!': 'mesoclise',
        }

    def initialize_dataset(self):
        tagged_sentences = mac_morpho.tagged_sents()
        self.train = tagged_sentences[100:]
        self.test = tagged_sentences[:100]

    def initialize_taggers(self):
        self.t0 = nltk.DefaultTagger('unk')
        self.t1 = nltk.UnigramTagger(self.train, backoff=self.t0)
        self.t2 = nltk.BigramTagger(self.train, backoff=self.t1)
        self.t3 = nltk.TrigramTagger(self.train, backoff=self.t2)
        print self.t3.evaluate(self.test)

    def split_into_relevant_words(self, text, bRemoveStopwords = False):
        sentences = nltk.sent_tokenize(text, self.lang)
        words = []
        for sent in sentences:
            for w in nltk.word_tokenize(sent, self.lang):
                words.append(w)

        sws = stopwords.words(self.lang)
        if bRemoveStopwords:
            relevant = []
            for w in words:
                if w not in sws:
                    relevant.append(w)
        else:
            relevant = words
        return relevant


    def tag_text(self, text, bRemoveStopwords):
        words = self.split_into_relevant_words(text)
        return self.t3.tag(words)

    def tag_word(self, word):
        return self.t3.tag([unicode(word)])