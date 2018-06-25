#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import logging
import discord
from discord.ext import commands
import asyncio
import random
import os

logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix='$')


@bot.listen()
async def on_ready():
          print(f'Logging in as... {bot.user.name}')
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='$help'))

def guild_owner_only():
    def check(ctx):
        return ctx.guild and ctx.guild.owner == ctx.author
    return commands.check(check)


@commands.cooldown(1, 60, commands.BucketType.user)
@guild_owner_only()
@bot.command()
async def announce(ctx, *, message):
    async def maybe_send(member):
        try:
            await member.send(message)
            await ctx.message.delete()
        finally:
            return

    await asyncio.gather(*[maybe_send(m) for m in ctx.guild.members])




@bot.command(name='8ball')
async def l8ball(ctx):
    await ctx.send(random.choice(['● It is certain.', '● It is decidedly so.', '● Without a doubt.', '● Yes - definitely.', '● You may rely on it', '● As I see it, yes.', '● Most likely.', '● Outlook good.', '● Yes.', '● Signs point to yes.', '● Reply hazy, try again', '● Ask again later.', '● Better not tell you now.', '● Cannot predict now.', '● Concentrate and ask again.', '● Don`t count on it.', '● My reply is no.', '● My sources say no', '● Outlook not so good.', '● Very doubtful.' ]))
    

    

    

bot.run(os.getenv("TOKEN"))
