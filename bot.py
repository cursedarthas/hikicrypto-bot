import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import URLInputFile
from aiogram.enums import ParseMode

from main import cryptocurrency

# Объект бота
bot = Bot(token="7127023392:AAE8eeQrs6gFNrzXwWXggxlfTTCFej3_Q5c")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    file_ids = []
    # Отправка файла по ссылке
    image_from_url = URLInputFile("https://kartinki.pics/uploads/posts/2021-07/1627154060_28-kartinkin-com-p-publichnii-dom-anime-anime-krasivo-29.jpg")
    result = await message.answer_photo(
        image_from_url,
        caption="Привет, я бот проекта <b>hikicrypto</b>\n\nАирдропы: @hikicrypto\nНовсоти бота: @hikidemonenok\n", parse_mode=ParseMode.HTML
    )
    file_ids.append(result.photo[-1].file_id)
    await message.answer("<b>Список всех моих команд:</b>\n\n1. /start - Перезапуск бота\n2.\
 /airdrops - Актуальные аирдропы\n3. /cryptoinfo - получение цен криптовалют",\
                         parse_mode=ParseMode.HTML)

# /cryptoinfo
@dp.message(Command("cryptoinfo"))
async def get_cryptoinfo(message: types.Message):
    # Формируем строку с информацией о криптовалютах
    info_str = ""
    for currency, info in cryptocurrency.items():
        price, change, market_cap = info
        info_str += f"{currency}:\nPrice: {price}\nChange: {change}\nMarket Cap: {market_cap}\n\n"
    
    # Отправляем сформированную строку в качестве ответа на сообщение
    await message.answer(info_str)

# /airdrops
@dp.message(Command("airdrops"))
async def get_airdrops_summary(message: types.Message):
    airdrops_info = """
    🔥 *Сводка всех аирдропов\n*
🚀 [xBlast](https://t.me/XBlastAppBot/App?startapp=QZMJUC) - запущен 14 марта 
😈 [Near Wallet](https://t.me/herewalletbot/app?startapp=6911495) - запущен 15 марта 
👾 [PocketFI](https://t.me/pocketfi_bot/Mining?startapp=5770702341) - запущен 5 апреля 
🟢 [Grass](https://app.getgrass.io/register/?referralCode=mluJ11f1g33nU97) - начало 4 эпохи 
    *\nКликеры/тапалки*:
🕊 [MemeFI Coin](https://t.me/memefi_coin_bot?start=r_5d1b26229f) - запущен в апреле 
🎁 [Hamster Kombat](https://t.me/hamster_kombat_bot?start=kentId5770702341) - запущен в апреле \n
*Кошачья ферма*:
😼 [Catizen](https://t.me/catizenbot/gameapp?startapp=r_979_2658209) - запущен с 19 марта \n
*Быстрые аирдропы с изи условиями*: 🙃
🍾 [PEPE TON COIN](https://t.me/pepetondrop_bot?start=r02341161684) - листинг 15 апреля 
⚡ [Kingy GM](https://t.me/kingyGMbot/gmgm?startapp=ref_287616) - запущен в апреле 
    """
    await message.answer(airdrops_info, parse_mode=ParseMode.MARKDOWN)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())