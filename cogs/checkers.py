import os

from dotenv import load_dotenv
from discord.ext import commands
from discord.channel import DMChannel

load_dotenv()


def committee_channel_check():
    def predicate(context):
        return context.channel.id == int(os.getenv('COMMITTEE_CHANNEL_ID'))
    return commands.check(predicate)


def voting_channel_check():
    def predicate(context):
        return context.channel.id == int(os.getenv('VOTING_CHANNEL_ID')) or isinstance(context.channel, DMChannel)
    return commands.check(predicate)


def voting_channel_only():
    def predicate(context):
        return context.channel.id == int(os.getenv('VOTING_CHANNEL_ID'))
    return commands.check(predicate)


def committee_member_check():
    def predicate(context):
        if isinstance(context.channel, DMChannel):
            return False
        else:
            return int(os.getenv('COMMITTEE_ROLE_ID')) in [role.id for role in context.author.roles]
    return commands.check(predicate)
