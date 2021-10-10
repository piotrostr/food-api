import pandas as pd

from cleanup import cleanup
from parse import parse
from pprint import pprint


if __name__ == '__main__':
    df = pd.read_csv('app/data/data.csv')
    for _ingredients in df['Ingredients'].iloc:
        ingredients = eval(_ingredients)
        print()
        pprint(ingredients)
        print()
        clean = cleanup(ingredients)
        for s in clean:
            print(f'{s:100} {parse(s)}')
        print()

# for large could say that one is 1.2*regular
# and units shall be times the given thing
# so post parse, there will be second round 
# of unit based parsing for 1 egg n stuff

# the current algo is ok efficient, 
# but it is a good idea to pre-evaluate all recipes
# so that it takes no time on the clientside to retrieve

