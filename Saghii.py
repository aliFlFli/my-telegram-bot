import requests
import asyncio
from telegram import Bot

# 🎯 توکن ربات و شناسه کانال (chat_id)
TOKEN = "7713579289:AAHPfiXND7GebfmzYB-Z16ybPe-Ha4w9SWg"
CHANNEL_ID = "-1002024025907"  # یا عدد chat_id کانال

# 🏦 تابع دریافت قیمت دلار از نوبیتکس
def get_usdt_price():
    url = "https://api.nobitex.ir/v2/orderbook/USDTIRT"
    response = requests.get(url)
    data = response.json()

    if "asks" in data and len(data["asks"]) > 0:
        price = int(float(data["asks"][0][0]))  # حذف ا>
        price //= 10  # تبدیل ریال به تومان
        return f"{price:,}"  # اضافه کردن جداکننده‌ی هزا>
    return "خطا در دریافت قیمت"

# 📡 تابع ارسال پیام به کانال
async def send_price_to_channel():
    bot = Bot(token=TOKEN)
    while True:
        price = get_usdt_price()
        message = f"💵 قیمت لحظه‌ای دلار: {price} تومان"

        try:
            await bot.send_message(chat_id=CHANNEL_ID, >
            print("✅ پیام ارسال شد:", message)
        except Exception as e:
            print("❌ خطا در ارسال پیام:", e)

        await asyncio.sleep(60)  # ⏳ صبر به مدت 60 ثان>

# 🚀 اجرای حلقه‌ی ارسال خودکار
async def main():
    await send_price_to_channel()

if __name__ == "__main__":
    asyncio.run(main())