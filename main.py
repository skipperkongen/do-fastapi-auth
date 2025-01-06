from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello world'}


@app.get('/title/std')
async def make_title():
    return {'title_case': 'this is the standard message'.title()}


@app.get('/title/{message}')
async def make_title2(message: str):
    return {'title_case': message.title()}

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@app.get('/items')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
