from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="📜 Справка бота"
        ),
        BotCommand(
            command="roadmap",
            description="🗺️ Дорожная карта"
        ),
        BotCommand(
            command="test",
            description="📝 Проверить свои знания"
        ),
        BotCommand(
            command="quizze",
            description="🧩 Задачи"
        ),
        BotCommand(
            command="cancel",
            description="↩️ Отмена"
        ),
        BotCommand(
            command="settings",
            description="⚙️ Настройки"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
