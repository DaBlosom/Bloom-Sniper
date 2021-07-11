import aiohttp
import asyncio, sys, time, requests
from datetime import datetime, timedelta

class playerInfo: #class to store data
    def __init__(self, UUID, Bearer_Key, Target_IGN, Password, dropTime):
        self.UUID = UUID
        self.Bearer_Key = Bearer_Key
        self.Target_IGN = Target_IGN
        self.Password = Password
        self.dropTime = dropTime

def nameReserveConformation(): #getting user info
    global Target_IGNR
    global bearerKey
    global auth
    global dropTimeR
    bearerKey = input("[*] Enter Bearer Key: ")
    Target_IGNR = input("[*] Enter your desired IGN: ")
    dropTimeR = input("[*] Enter the time of IGN release: ")
    auth = "Bearer " + bearerKey

def conformation(): #getting user info
    global Target_IGN
    global dropTime
    global Bearer_Key
    global Password
    global playerInfo1
    UUID = input("[*] Enter your UUID: ")
    Bearer_Key = input("[*] Enter your Bearer_Key: ")
    Target_IGN = input("[*] Enter your desired IGN: ")
    Password = input("[*] Enter your account password: ")
    dropTime = input("[*] Enter the time of drop: ")
    playerInfo1 = playerInfo(UUID, Bearer_Key, Target_IGN, Password, dropTime)
    print(f"[*] UUID: [{playerInfo1.UUID}]\n[*] Bearer Key: [{playerInfo1.Bearer_Key}]\n[*] Desired IGN: [{playerInfo1.Target_IGN}]\n[*] Password: [{playerInfo1.Password}]\n[*] Drop Time: [{playerInfo1.dropTime}]")

async def main(): #sniping function
    global auth
    auth = "Bearer " + playerInfo1.Bearer_Key
    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://api.mojang.com/user/profile/{playerInfo1.UUID}/name', headers = {'Authorization': auth}, json = {"name": playerInfo1.Target_IGN,"password": playerInfo1.Password}) as resp:
            print(await resp.text())
            x = resp.status
    if x == 204:
        print(f"[*] {Target_IGN} Acquired!")
    else:
        print(x)
        print("[*] Failure!")

async def reserve(): #reserving fucntion
    global origin
    origin = "https://www.checkout.minecraft.net"
    async with aiohttp.ClientSession() as session:
        async with session.put(f"https://api.mojang.com/user/profile/agent/minecraft/name/{Target_IGNR}", headers = {"Authorization": auth,"Origin": origin}) as resp:
            print(await resp.text())
            x = resp.status
        if x == 204:
            print(f"[*] {Target_IGNR} Reserved!")
        else:
            print(x)
            print("[*] Failiure!")

if __name__ == '__main__':
    choice = input("[*] 1. IGN Sniper 2. IGN Reserver | 1 or 2: ")
    if choice == "1":
        try:
            conformation()
            print(f"[*] Sniping {Target_IGN} at {dropTime}...")
            while True:
                now = datetime.now()
                now = str(now)
                parts = now.split()
                parts1 = parts[1]
                exacTime = parts1.split(".")
                time = exacTime[0]
                if time != dropTime:
                    pass        
                elif time == dropTime:
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(main())
        except:
            print("Something went wrong...\nProgram Closing")
            time.sleep(1)

    elif choice == "2":
        try:
            nameReserveConformation()
            print(f"[*] Reserving {Target_IGNR} at {dropTimeR}...")
            while True:
                now = datetime.now()
                now = str(now)
                parts = now.split()
                parts1 = parts[1]
                exacTime = parts1.split(".")
                time = exacTime[0]
                if time != dropTimeR:
                    pass        
                elif time == dropTimeR:
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(reserve())
        except:
            print("Something went wrong...\nProgram Closing")
            time.sleep(1)

    else:
        print("[*] Invalid Input...\nProgram Closing")
        time.sleep(1)