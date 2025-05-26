from fastapi import FastAPI
from contextlib import asynccontextmanager
from bot import dp, bot
import uvicorn, asyncio
from posts import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(dp.start_polling(bot)) #запуск телеграм бота
    yield
    

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True) #Щоб можна було запускати проект з команди python main.py