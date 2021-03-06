#A Simple Code to forward all messages, files... from one channel to another.
#Use Your Secondary account for this.(Forwarding bulk messages may result you in flood wait and ban)

#pyrogram v<=1.0.7
import asyncio
from pyrogram.errors import FloodWait

from_channel = -1001312356344 #From Channel ID
to_channel = -1005382636286 #To Channel ID
async for message in client.search_messages(from_channel, filter="empty"): #You can change filter value according to your need.
        try:
            await message.forward(to_channel, as_copy=True) #Use "as_copy=False" if you want to forward with tag.
            asyncio.sleep(3) #You can Change it according to your need.
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except:
            pass

#pyrogram v>1.0.7
#Without Tag
import asyncio
from pyrogram.errors import FloodWait

from_channel = -1001312356344 #From Channel ID
to_channel = -1005382636286 #To Channel ID
async for message in client.search_messages(from_channel, filter="empty"): #You can change filter value according to your need.
        try:
            await message.copy(to_channel) #Without Tag
            asyncio.sleep(3) #You can Change it according to your need.
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except:
            pass
#With Tag
import asyncio
from pyrogram.errors import FloodWait

from_channel = -1001312356344 #From Channel ID
to_channel = -1005382636286 #To Channel ID
async for message in client.search_messages(from_channel, filter="empty"): #You can change filter value according to your need.
        try:
            await message.forward(to_channel) #With Tag
            asyncio.sleep(3) #You can Change it according to your need.
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except:
            pass
