import time

import redis.asyncio as aioredis
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

app = FastAPI()
rd = aioredis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


@app.middleware("http")
async def rate_limit_and_timing(request: Request, call_next):
    client_ip: str = request.client.host  # type: ignore

    # Rate limit: 100 запросов в минуту на IP
    current = await rd.get(client_ip)
    if current is None:
        await rd.setex(client_ip, 60, 1)
    elif int(current) >= 100:
        return JSONResponse(status_code=429, content={"detail": "Too Many Requests"})
    else:
        await rd.incr(client_ip)

    start = time.perf_counter()
    response: Response = await call_next(request)
    process_time = time.perf_counter() - start
    response.headers["X-Process-Time"] = f"{process_time:.4f}s"
    return response    
    

if __name__ == "__main__":
    uvicorn.run(
        "app", 
        host="0.0.0.0", 
        port=8000,
        reload=True
    )
