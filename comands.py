from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def bot_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="starting bot"
        ),
        BotCommand(
            command="menu",
            description="menu of this bot"
        ),
        BotCommand(
            command="help",
            description="more information"
        )
    ]
    
    await bot.set_my_commands(commands, BotCommandScopeDefault)