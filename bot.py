import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8466271055:AAFJHcvJ3WR2oAI7g1Xky2760qLgM68WXMM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Storage for user activity logs
user_data = {}

# /start command
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "欢迎使用打卡机器人 ✅\n请选择操作：",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="上班"), types.KeyboardButton(text="下班")],
                [types.KeyboardButton(text="吃饭"), types.KeyboardButton(text="上厕所")],
                [types.KeyboardButton(text="回座"), types.KeyboardButton(text="抽烟")]
            ],
            resize_keyboard=True
        )
    )

# Handle activity check-ins
@dp.message()
async def handle_activity(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    activity = message.text.strip()
    log = f"✅ {user_name} ({user_id}) 打卡成功: {activity}"

    if user_id not in user_data:
        user_data[user_id] = []
    user_data[user_id].append((activity, message.date))

    await message.answer(log)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
