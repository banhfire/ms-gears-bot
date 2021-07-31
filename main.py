import discord
import os
from replit import db

client = discord.Client()

if "responding" not in db.keys():
  db["responding"] = True


#privatize character gear
#update individual
#update all
#delete individual
#help
#troubleshootin to all commands
# Class
# Lvl
# Arcane Force
# Stat
# 40s BA
# Sacred Force
# Boss Interest
# Preferred Run Times
# Provide image upload for Stat window, 40s BA/Full BA, Character Thumbnail


def new_character(char_msg, name_msg):
  if name_msg in db.keys():
    return False
  else:
    char_dict = {}
    char_dict["class"] = char_msg.split()[1]
    char_dict["level"] = char_msg.split()[2]
    char_dict["arcane force"] = char_msg.split()[3]

    char_dict["stat"] = char_msg.split()[4]
    char_dict["sacred force"] = char_msg.split()[5]
    char_dict["40s BA"] = char_msg.split()[6]

    #Need to adjust to allow spaces
    char_dict["boss interest"] = char_msg.split()[7]
    char_dict["runtimes"] = char_msg.split()[8]
    db[name_msg] = char_dict
    return True

def delete_character(char_name):
  del db[char_name]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if db["responding"]:

    if msg.startswith("$msg new"):
      update_msg = msg.split("$msg new ", 1)[1]
      char_name = update_msg.split()[0]
      added = new_character(update_msg, char_name)
      if added is True:
        embedVar=discord.Embed(title=char_name, description="Thanks for adding your character information.", color=0x109319)
        embedVar.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        #Use this to upload BA, Stat Window
        # Optional method: Go to below link, replace character_name with name_msg, extract all images, find character thumbnail from that
        #https://maplestory.nexon.net/rankings/overall-ranking/legendary?rebootIndex=1&character_name=bnhfr
        #embed.set_thumbnail(url="https://msavatar1.nexon.net/Character/MLDIDHOJHJLJCNHMBAHECEOPHCFJMBKIPEHCIIEKJNJBCJFHJCOBKAIKEGOHIBHOBAFKKGDEJCAFLKAANLPHMIHIGEGENCFKOBBPPOALMCFNKFMFFAHADHLEMMAFABFCEICEOEAEEKEHHLJNAEPHDFCPIMOMMHGPEBHAAJLMKFBIFBEKPBAIEJGGEDGHOHIPBIIAFKFIGKKPHOLOLANDKGMLDECJCADIOFCBOAONEBFNECNHMEBOHFMKHCAPCAJA.png")
        embedVar.add_field(name="Class", value=db[char_name]['class'], inline=True) 
        embedVar.add_field(name="Level", value=db[char_name]['level'], inline=True)
        embedVar.add_field(name="Arcane Force", value=db[char_name]['arcane force'], inline=True) 
        embedVar.add_field(name="Stat", value=db[char_name]['stat'], inline=True)
        embedVar.add_field(name="40s BA", value=db[char_name]['40s BA'], inline=True) 
        embedVar.add_field(name="Sacred Force", value=db[char_name]['sacred force'], inline=True) 
        embedVar.add_field(name="Interested Bosses", value=db[char_name]['boss interest'], inline=False)
        embedVar.add_field(name="Preferred Run Time", value=db[char_name]['runtimes'], inline=False)
        
        await message.channel.send(embed=embedVar)
      else:
        embedVar=discord.Embed(title=char_name, description=char_name+" is already in the database.\n\nHere are examples of how to edit your information: \n- $msg update level 300 \n- $msg update stat 42.0k\n- $msg update AF 1320\n- $msg update BI HLucid\HWill\n- $msg update runtimes Reset-2to+5\n- $msg update BA 2.5T\n- $msg update all.\n\nAdditionally you may want to delete your character, if so type:\n- '$msg del character_name'", color=0x109319)
        await message.channel.send(embed=embedVar)

    if msg.startswith("$msg get"):
      get_msg = msg.split("$msg get ", 1)[1]
      char_name = get_msg.split()[0]

      if char_name in db.keys():
        embedVar=discord.Embed(title=char_name, description="Thanks for adding your character information.", color=0x109319)
        embedVar.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        #Use this to upload BA, Stat Window
        # Optional method: Go to below link, replace character_name with name_msg, extract all images, find character thumbnail from that
        #https://maplestory.nexon.net/rankings/overall-ranking/legendary?rebootIndex=1&character_name=bnhfr
        #embed.set_thumbnail(url="https://msavatar1.nexon.net/Character/MLDIDHOJHJLJCNHMBAHECEOPHCFJMBKIPEHCIIEKJNJBCJFHJCOBKAIKEGOHIBHOBAFKKGDEJCAFLKAANLPHMIHIGEGENCFKOBBPPOALMCFNKFMFFAHADHLEMMAFABFCEICEOEAEEKEHHLJNAEPHDFCPIMOMMHGPEBHAAJLMKFBIFBEKPBAIEJGGEDGHOHIPBIIAFKFIGKKPHOLOLANDKGMLDECJCADIOFCBOAONEBFNECNHMEBOHFMKHCAPCAJA.png")
        embedVar.add_field(name="Class", value=db[char_name]['class'], inline=True) 
        embedVar.add_field(name="Level", value=db[char_name]['level'], inline=True)
        embedVar.add_field(name="Arcane Force", value=db[char_name]['arcane force'], inline=True) 
        embedVar.add_field(name="Stat", value=db[char_name]['stat'], inline=True)
        embedVar.add_field(name="40s BA", value=db[char_name]['40s BA'], inline=True) 
        embedVar.add_field(name="Sacred Force", value=db[char_name]['sacred force'], inline=True) 
        embedVar.add_field(name="Interested Bosses", value=db[char_name]['boss interest'], inline=False)
        embedVar.add_field(name="Preferred Run Time", value=db[char_name]['runtimes'], inline=False)

        await message.channel.send(embed=embedVar)
      else:
        embedVar=discord.Embed(title=char_name, description=char_name+" is not in the database.\n\nUse the following example as a guide: \n- $msg new Pikawu 300 1320 69k N/A 420T Black-Mage -2:Reset:+5'", color=0x109319)
        await message.channel.send(embed=embedVar)



    #if msg.startswith("$msg update level"): 2
    #if msg.startswith("$msg update stat"): 3
    #if msg.startswith("$msg update AF"): 4
    #if msg.startswith("$msg update BA"): 5
    #if msg.startswith("$msg update SF"): 6
    #if msg.startswith("$msg update BI"): 7
    #if msg.startswith("$msg update runtimes"): 8
    #if msg.startswith("$msg update all"): 9
    #if msg.startswith("$msg list"): 10



    if msg.startswith("$msg del"):
      delete_name = msg.split("$msg del ", 1)[1]
      if delete_name in db.keys():
        delete_character(delete_name)
        await message.channel.send("`Character has been deleted.`")
      else:
        await message.channel.send("`Character does not exist in database.`")

    #Print every key except for responding
    if msg.startswith("$msg list"):
      await message.channel.send(db.keys())

  # Add security to enabling/disabling bot
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

client.run(os.getenv("TOKEN"))