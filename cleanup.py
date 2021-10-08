
def cleanup(ingredients: list[str]):
    res = []
    for s in ingredients:
        s = s.lower()
        if s.count('-'):
            s = s[::-1].replace('-', ' ')[::-1]
        if 'gs' in s:
            print('huj', s)
        s = s.replace('one', '1')
        s = s.replace('two', '2')
        s = s.replace('three', '3')
        s = s.replace('four', '4')
        s = s.replace('five', '5')
        s = s.replace('six', '6')
        s = s.replace('seven', '7')
        s = s.replace('eight', '8')
        s = s.replace('nine', '9')
        s = s.replace('lb.', 'lb')
        s = s.replace('gs', 'g')
        s = s.replace('lb', 'pound')
        s = s.replace('pounds', 'pound')
        s = s.replace('½', '.5')
        s = s.replace('¾', '.75')
        s = s.replace('¼', '.25')
        s = s.replace('cups', 'cup')
        s = s.replace('cup', '128g')
        s = s.replace('tsp.', 'tablespoon')
        s = s.replace('tbsp.', 'tablespoon')
        s = s.replace('tablespoons', 'tablespoon')
        s = s.replace('tablespoon', '21.25g')
        s = s.replace('teaspoons', 'teaspoon')
        s = s.replace('teaspoon', '5.7g')
        s = s.replace('pound', '453.6g')
        s = s.replace('ounces', 'oz.')
        s = s.replace('oz.', '28g')
        s = s.replace('⅓', '0.33')
        s = s.replace('loafs', 'loaf')
        s = s.replace('loaf', '400g')
        s = s.replace('pinches', 'pinch')
        s = s.replace('pinch', '0.35g')
        s = s.replace('sticks', 'stick')
        s = s.replace('stick', '113g')
        s = s.replace('pints', 'pint')
        s = s.replace('pint', '474g')
        res.append(s)
    return res

