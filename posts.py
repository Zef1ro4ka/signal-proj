from typing import  Literal
from fastapi import APIRouter
from pydantic import BaseModel, Field
from aiogram.types import Message
from bot import  bot, chats_id
router = APIRouter()

class host(BaseModel):
    state_10_0_0_5: Literal[0, 1] = Field(..., description="Only 0 or 1 allowed", example=0) #Встановлення лімітів вводу
    state_10_0_0_50: Literal[6, 9]  = Field(..., description="Only 6 or 9 allowed", example=6)
    
ip_1, ip_2 = '10.0.0.5', '10.0.0.50'
old_date_1, old_date_2 = 0, 6
@router.post("/")
async def cmd_start(
    inpud_date: host
):  
    global old_date_1, old_date_2
    new_date_1,new_date_2 = inpud_date.state_10_0_0_5, inpud_date.state_10_0_0_50 #Присвоєння значеннь які надійшли із json
    if str(old_date_1) != str(new_date_1) and str(old_date_2) != str(new_date_2):
        old_date_1, old_date_2 = new_date_1, new_date_2
        for chat in chats_id: #  відправлення повідомлення якщо одночано авторизовано >1 користувача
            await bot.send_message(chat, f"Зміни зафіксовані в {ip_1} статус змінився на {new_date_1}, в {ip_2} статус змінився на {new_date_2} ")
    elif str(old_date_1) != str(new_date_1):
        old_date_1 = new_date_1
        for chat in chats_id:
            await bot.send_message(chat, f"Зміни зафіксовані в {ip_1} статус змінився на {new_date_1}")
 
    elif str(old_date_2) != str(new_date_2):
        old_date_2 = new_date_2
        for chat in chats_id:
            await bot.send_message(chat, f"Зміни зафіксовані в {ip_2} статус змінився на {new_date_2} ")
    else:
        return {"result": "ok"}