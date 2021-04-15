import discord
from discord.ext import tasks
import os
import json
from datetime import datetime
import sheets
import responses
import movie
import command
import eventManager
import act

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} ready hai bhau!".format(client))
    reminder.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return 0

    if command.recUpdateBet(message.content):
        status = act.updateBet(message)
        if status:
            await message.channel.send(responses.betNotPlaced())
        else:
            await message.channel.send(responses.betPlaced())
    elif command.recShowMyPoints(message.content):
        embed = act.getMyPointsEmbed(message)
        await message.channel.send(embed=embed)
    elif command.recShowMentionPoints(message.content):
        if len(message.mentions) != 0:
            embed = act.getPointsEmbed(message)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(responses.noUserMentioned())
    elif command.recShowLeaderboard(message.content):
        embed = act.getLeaderboard(message)
        await message.channel.send(embed=embed)
    elif message.content.lower().find("bunty help") != -1:
        embed = act.getCommands()
        await message.channel.send(embed=embed)
    elif command.recShowBets(message.content):
        embed = act.showBets()
        await message.channel.send(embed=embed)
    elif command.recShowMatch(message.content):
        embed = act.getMatches()
        await message.channel.send(embed=embed)
    elif command.recAddMovie(message.content):
        if movie.addMovie(message.content):
            await message.channel.send(responses.addMovieAbsent())
        else:
            await message.channel.send(responses.addMoviePresent())
    elif command.recShowMovie(message.content):
        embed = act.showMovieList()
        await message.channel.send(embed=embed)
    elif command.recShowMovieInfo(message.content):
        embed = act.showMovieInfo(message)
        await message.channel.send(embed=embed)


class var:
    def __init__(self):
        with open('config.json') as configObj:
            config = json.load(configObj)

        self.channel = config['IPL_channelID']

        self.antiRepeat = ''
        self.fetchEvents()

    def fetchEvents(self):
        with open('events.json') as eventsObj:
            self.events = json.load(eventsObj)

    def attainTime(self):
        return datetime.now().strftime('%H:%M')

    def attainSched(self):
        day = datetime.now().strftime('%A')
        return self.events[day]

    def attainLastMod(self):
        LMFloat = os.path.getmtime('events.json')
        return datetime.fromtimestamp(LMFloat).strftime('%H:%M')


rem = var()


@tasks.loop(seconds=30)
async def reminder():
    rem.fetchEvents()
    current_time = rem.attainTime()
    print("Current Time: ", current_time)

    if rem.antiRepeat != current_time:
        sched = rem.attainSched()
        print("sched: ", sched)
        currEvent = [sched[i] for i in sched if i == current_time]
        print("currEvent: ", currEvent)

        if currEvent:
            reminder_channel = client.get_channel(rem.channel)
            if currEvent[0][0] == "Warning":
                await reminder_channel.send(act.warning() + currEvent[0][1])
            elif currEvent[0][0] == "Allocate":
                allot = sheets.allotPoints()
                sheets.updateRow()
                if len(allot.keys()) == 0:
                    await reminder_channel.send(responses.allotBet())
                else:
                    msg = "Bhau jin jin logo ne bet nhi lagayi thi unko maine ye random point dediye hai:\n\n"
                    for user in allot.keys():
                        msg += user + " : " + str(allot[user]) + "\n"
                    await reminder_channel.send(msg)
            elif currEvent[0][0] == "Set Reminders":
                eventManager.addEvent()
                await client.get_channel(id).send("Reminders Set")
            else:
                await reminder_channel.send(currEvent[0][1])

    rem.antiRepeat = current_time

client.run('<TOKEN HERE>')
