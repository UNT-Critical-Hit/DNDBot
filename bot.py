import importlib

import discord
from discord.ext import commands
import sqlite3
from modules import CampaignBuilder, CampaignSQLHelper, CampaignPlayerManager


class DNDBot(commands.Bot):
    def __init__(self, db: sqlite3.Cursor, connection: sqlite3.Connection, config: dict, **kwargs):
        super().__init__(**kwargs)
        self.db = db
        self.connection = connection
        self.config = config
        self.all_cogs, self.loaded_cogs, self.unloaded_cogs = [], [], []
        self.COG_FILE = "COGS.txt"
        self.traceback = {}

        with open(self.COG_FILE, "r") as cogs:
            self.all_cogs = [i.rstrip() for i in cogs.readlines()]

        self.CampaignBuilder = CampaignBuilder(self)
        self.CampaignSQLHelper = CampaignSQLHelper(self)
        self.CampaignPlayerManager: CampaignPlayerManager = None
