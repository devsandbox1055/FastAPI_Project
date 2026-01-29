from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse
from app.routes import router

app = FastAPI()

#GLOBAL exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Kitchen has problem, please try again",
                 "path": str(request.url)
                 }
    )
app.include_router(router)