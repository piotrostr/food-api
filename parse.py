
def parse(s) -> tuple[str, str]:
    words = s.split(' ')

    # case where '15g of chicken' at the start
    if 'g' in words[0]:
        try: 
            grams = float(words[0].replace('g', ''))
            return grams, 'grams'
        except:
            pass

    # case where '2 5g salt'
    for i in range(len(words) - 1):
        w0 = words[i]
        w1 = words[i + 1]
        if 'g' in w1:
            # case where '3.5-4 ounces'
            try:
                if '–' in w0:
                    w00, w01 = w0.split('–')
                    w00 = w00.replace('(', '')
                    w01 = w01.replace(')', '')
                    if (
                        is_number(w00) and 
                        is_number(w01)
                    ):
                        w0 = (w01 + w00) / 2
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

    # case where '2 large eggs'
    qty_words = ['small', 'medium', 'large', 'big']
    if any(w for w in qty_words if w in s):
        for i in range(len(words) - 1):
            if words[i] in qty_words:
                qty = ''
                product = ''
                print(words[i])
                if is_number(words[i - 1]):
                    qty += words[i - 1]
                qty += words[i]
                for word in words:
                    if (
                        is_food(word) or
                        is_food_unit(word)
                    ):
                        product += word
                return qty + ' ' + product, 'unit'

    # case where '3 garlic cloves'
    for i in range(len(words) - 1):
        if (
            is_number(words[i]) and 
            is_food(words[i + 1])
        ):
            qty = words[i]
            product = ''
            for word in words:
                if (
                    is_food(word) or 
                    is_food_unit(word)
                ):
                    product += word
            return qty + ' ' + product, 'unit'


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False


def is_food(word: str):
    if word == 'garlic':
        return True
    return False


def is_food_unit(word: str):
    if word == 'cloves':
        return True
    return False

