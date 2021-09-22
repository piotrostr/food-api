from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
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
    # query the database / dataframe held in memory (see speed tradeoff)
    # return json 
    return requirements

