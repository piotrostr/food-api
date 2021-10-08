
def parse(s):
    words = s.split(' ')
    if 'g' in words[0]:
        try: 
            grams = float(words[0].replace('g', ''))
            return grams, 'grams'
        except:
            pass
    for i in range(len(words) - 1):
        w0 = words[i]
        w1 = words[i + 1]
        if 'g' in w1:
            try:
                if '–' in w0:
                    w00, w01 = w0.split('–')
                    w00 = w00.replace('(', '')
                    w01 = w01.replace(')', '')
                    try:
                        w00 = float(w00)
                        w01 = float(w01)
                        w0 = (w01 + w00) / 2
                    except:
                        pass
                if type(w0) is str:
                    w0 = w0.replace('(', '')
                w1 = w1.replace(')', '')
                w0 = float(w0)
                w1 = w1.replace('g', '')
                w1 = float(w1)
                grams = w0 * w1
                return round(grams, 2), 'g'
            except: 
                continue
    qty_words = ['small', 'medium', 'large', 'big']
    if any(w for w in qty_words if w in s):
        for i in range(len(words) - 1):
            # case where is is 5 eggs / 3 garlic cloves
            if words[i] in qty_words:
                qty = ''
                product = ''
                try:
                    float(words[i - 1])
                    qty += words[i - 1]
                except:
                    pass
                qty += words[i]
                for word in words:
                    if is_food_word(word):
                        product += word
                return qty + ' ' + product, 'unit'


def is_food_word(word: str):
    return False

