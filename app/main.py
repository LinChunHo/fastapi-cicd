from typing import Optional
from fastapi import FastAPI
import aiohttp

app=FastAPI()

# exp1
# @app.get('/')
# def read_root():
#     return {"hello":"hello app2"}

@app.get("/")
async def slow_route():
    # async with aiohttp.ClientSession() as session:
    #     async with session.get("http://fastapi_ms_app5c_1:85") as resp:
    #         data = await resp.text()
    #         print(data)
    #         return data
    return "hello123"
            # do something with data


@app.get('/item/{item_id}')
def read_item(item_id:int,q:Optional[str]=None):
    return {"item_id":item_id,"q":q}

# docker command .
# docker run -d --name app2c --network app_network -p 81:80 app2
# docker build -t app2 .

# docker vulume
#