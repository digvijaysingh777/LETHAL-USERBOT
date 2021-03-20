

import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from var import Var

from userbot import CMD_LIST, LOAD_PLUG, LOGS, SUDO_LIST, bot
from userbot.helpers.exceptions import CancelProcess
from userbot.Config import Config

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from userbot.Config import Config
else:
    if os.path.exists("config.py"):
        from config import Development as Config



def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userbot.utils

        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:
        import userbot.utils

        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.Var = Var
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for UNIBORG
        sys.modules["uniborg.util"] = userbot.utils
        mod.Config = Config
        mod.borg = bot
        mod.lethalbot = bot
        mod.edit_or_reply = edit_or_reply
        mod.delete_hell = delete_hell
        # support for hellbot originals
        sys.modules["raider.utils"] = userbot.utils
        sys.modules["RAIDER"] = userbot
        
        sys.modules["userbot.events"] = userbot.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["userbot.plugins." + shortname] = mod
        LOGS.info("Successfully imported " + shortname)
