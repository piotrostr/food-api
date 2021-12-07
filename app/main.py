from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)

class Requirements(BaseModel):
    # dietary
    vegetarian: bool
    vegan: bool
    nut_free: bool
    lactose_free: bool
    halal: bool
    shellfish_allergy: bool

    # quality
    free_range: bool
    organic: bool
    rspca_assured: bool
    red_tractor: bool


@app.post('/foods')
async def foods(requirements: Requirements):
    print(requirements.vegan)
    return requirements

# TODO

# implement authentication (used for both health handler and premiere)

# add each of the requirements to columns 
# so it doesnt need to be evaluated at runtime

# evaluate all measurements to grams

# based on the products quantities use the 
# USDA table and add the macros per each of the meals

# ? classify each of the meals as breakfast etc
# could be done programatically based on the calories of each meal

# add estimated cost of each of the meals

# algorithmically generate another table of meal-plans

# query the dataframe/database held in memory for matching meals
