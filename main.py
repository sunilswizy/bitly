from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from random import randint
from redis_client import redis_client, check_redis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from db import get_db

class ShortenBody(BaseModel):
    longUrl: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_event():
    await check_redis()

def generate_random_url():
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    short_url = ''
    for _ in range(6):
        short_url += chars[randint(0, len(chars) - 1)]
    return short_url


@app.get("/api") 
def hello_world():
    return {
        "message": "Hello",
        "status": 200
    }

@app.post("/api/shorten")
async def shorten(payload: ShortenBody, db: AsyncSession = Depends(get_db)):
    if not payload.longUrl: return "Long URL is required"


    while True:
        short_url = generate_random_url()
        result = await db.execute(text("SELECT long_url from shorten where short_url = :url"), { "url": short_url})
        item = result.fetchone()
        if item is None:
            break
    
    await db.execute(
        text("""
        INSERT INTO shorten (short_url, long_url)
        VALUES (:short_url, :long_url)
        """),
        {"short_url": short_url, "long_url": payload.longUrl}
    )

    await db.commit()
    
    return {"short_url": short_url}

@app.get('/api/{short_url}')
async def redirection(short_url: str, db: AsyncSession = Depends(get_db)):
    async def update_used_count():
        await db.execute(text('UPDATE shorten SET used_count = used_count + 1 where short_url= :url'), { "url": short_url })
        await db.commit()


    cached = await redis_client.get(short_url)
    if cached:
        await update_used_count()
        return RedirectResponse(url=cached)

    result = await db.execute(text("SELECT long_url from shorten where short_url = :url"), { "url": short_url})
    item = result.fetchone()

    if item is None:
        return "Invalid URL"

    await redis_client.set(short_url, item[0])
    await update_used_count()

    return RedirectResponse(url=item[0])


