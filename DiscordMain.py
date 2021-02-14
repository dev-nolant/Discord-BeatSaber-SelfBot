from websocket import create_connection
from discord.ext import commands
import discord
from discord.ext.commands import Bot
bot = commands.Bot(">>>", self_bot=True)
import json, time, sys
try:
    def Connection_Commit():
        global names
        try:
            ws = create_connection("ws://localhost:2946/BSDataPuller/MapData")
            wsL = create_connection("ws://localhost:2946/BSDataPuller/LiveData")
            ws.send("Update")
            wsL.send("Update")
            json_data =  ws.recv()
            parsed_json = (json.loads(json_data))
            json_dataL =  wsL.recv()
            parsed_jsonL= (json.loads(json_dataL))
            global Misses
            Misses = parsed_jsonL["Misses"]
            global Map_Difficulty
            Map_Difficulty = parsed_json["Difficulty"]
            global Song_Name
            Song_Name = parsed_json["SongName"]
            previous = Song_Name
            sys.path.append(".")
            print("CHP 2")
            names = ('Playing: '+str(Song_Name)+" on "+str(Map_Difficulty)+" - "+str(Misses)+" Misses")
            return names
        except Exception as e:
            print(e)
            names = None
    @bot.event
    async def on_ready():
        print("Bot Ready")
        while True:
            print("CHP 1")
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=str(Connection_Commit())))
            time.sleep(5)
            print(Connection_Commit())
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=str(Connection_Commit())))
            print("Status Updated")

    bot.run("key", bot=False)
except KeyboardInterrupt:
    ws.close()
    wsl.close()
    quit()
except Exception as e:
    print(str(e))
