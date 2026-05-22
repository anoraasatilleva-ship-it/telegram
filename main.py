# import asyncio
# import logging
# import sys

# from aiogram import Bot, Dispatcher
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.types import Message

# TOKEN = "8491951094:AAEJ24j8Ljel1aoowmWjp9i8UHwesZCMiHo"

# dp = Dispatcher() 

# @dp.message() 
# async def salom(message: Message):
#     print(f"Bu foydalanuvchi yozgan xabar: {message.text}")
    
#     if message.text:
#         await message.answer("Bu matn. Siz matn yozdingiz")
#     elif message.photo:
#         await message.answer("Siz rasm yubordingiz")
#     elif message.video:
#         await message.answer("Siz video yubordingiz")

# async def main() -> None:
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import os

BOT_TOKEN = os.getenv("8491951094:AAFFN6LJyUG_PFL1D5fYUuZGXyIW5Sb9_44")

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):

    text = (
        "✨ Assalomu alaykum!\n"
        "Botimizga xush kelibsiz.\n\n"

        "📚 Darslar ro‘yxati:\n\n"

        "/Malibu - Malibu\n"
        "/Gentra - Gentra\n"
        "/Nexia - Nexia\n"
        "/Audi - Audi\n"
        "/Mercedes - Mercedes"
    )

    await message.answer(text)


@router.message(Command("Malibu"))
async def python_darslar(message: Message):

    await message.answer_video(
        video="BAACAgQAAxkBAAOeahAHjZuIkLI9K3m7R3z0wxLjMqAAAgkLAAIFgjxQx6Ske6RtMd87BA",
        caption="Malibu2 35.000$ 💸"
    )
    await message.answer_video(
        video="BAACAgIAAxkBAAObahAHjY5nlMoepUQ5E5lKWorRufEAAg-PAAKMJhhLtgU8y4_ElEw7BA",
        caption="Malibu2 32.000$ 💸"
    )
    await message.answer_video(
        video="BAACAgIAAxkBAAOdahAHjQgZ72-7sIERSgKhl0f-OZ0AAn6VAAKgFjhI3pD5hEyqlcc7BA",
        caption="Malibu2 30.000$ 💸"
    )

@router.message(Command("Gentra"))
async def telegram_bot(message: Message):

    await message.answer_video(
        video="BAACAgQAAxkBAAOnahAH2cAIsAKLSugRL1TSoisc1rkAAqYLAALna_RTU3T7bRdag3g7BA",
        caption="Qora Gentra Kokand ⚡"
    )
    await message.answer_video(
        video="BAACAgQAAxkBAAOmahAH2UYxR0AV3U_EdFoNBsK62JkAAs8JAAKeiZVTwKQjQW5XETY7BA",
        caption="Qora Gentra Tashkent ⚡"
    )
    await message.answer_video(
        video="BAACAgQAAxkBAAOlahAH2YChNLr6EW7gCaxJhPEbHY0AAskKAAKXcaRTGAMcnIThC7o7BA",
        caption="Qora Gentra Samarkand ⚡"
    )


@router.message(Command("Nexia"))
async def django_darslar(message: Message):

    await message.answer_video(
        video="BAACAgIAAxkBAAPMahAIyLk2OqY1sTdhQ6TxfoXsod4AAuyaAAKMkVBJKF6SD-QJIQI7BA",
        caption=" Nexia2 Turbo⚡ "
    )
    await message.answer_video(
        video="BAACAgQAAxkBAAPGahAIuSPFdv-4e8merK9Fw9ZhGH0AApQKAAKQytVSRZT4dPg6hvc7BA",
        caption=" Nexia2 Turbo ⚡"
    )
    await message.answer_video(
        video="BAACAgIAAxkBAAPEahAIubzgg1BofA3TwiU6GSEuBasAAuqLAAIiRmhKMAOEA8_81Ig7BA",
        caption=" Nexia2 Turbo ⚡"
    )


@router.message(Command("Audi"))
async def aiogram_darslar(message: Message):

    await message.answer_video(
        video="BAACAgIAAxkBAAOyahAH_pu4SU794PDLOKN-GfYJ7EkAAjx0AAJCIaBJUZEShtmL_xA7BA",
        caption="⚡ Audi"
    )
    await message.answer_video(
        video="BAACAgIAAxkBAAOvahAH_oUdfwABNAIi9tjXqZ3mLYRgAALeYAACW5TwSg6epeLbLgPUOwQ",
        caption="⚡ Audi"
    )
    await message.answer_video(
        video="BAACAgIAAxkBAAOxahAH_s9NCvOqQWt1utvu3AQMS-QAAu5xAAIWkIBLQMw2OvWW-7Q7BA",
        caption="⚡ Audi"
    )


@router.message(Command("Mercedes"))
async def baza_darslar(message: Message):

    await message.answer_video(
        video="BAACAgIAAxkBAAO4ahAIehyUD2tdz0Wlhui7l7b7-hkAApVyAALsMDhIhMPAUGrJ4VY7BA",
        caption="🗂 Mercedes"
    )
    await message.answer_video(
        video="BAACAgIAAxkBAAO6ahAIejMHc0_EXkA6-GW6guqjoVQAArhzAAK_fFBKZ0XztFr8LwABOwQ",
        caption="🗂 Mercedes"
    )
    await message.answer_video(
        video="BAACAgIAAxkBAAO5ahAIevVMKkJHpEzX3NvQZ_sPGNQAAv52AALuf7hJpCIqubWc5Cg7BA",
        caption="🗂 Mercedes"
    )

@router.message(F.video)
async def get_video_id(message: Message):

    await message.answer(
        f"📹 Video file_id:\n\n{message.video.file_id}"
    )


@router.message()
async def other_messages(message: Message):

    await message.answer(
        "❌ Buyruq noto‘g‘ri.\n/start ni bosing."
    )


async def main():

    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout
    )

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    dp.include_router(router)

    print("✅ Bot ishga tushdi...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())