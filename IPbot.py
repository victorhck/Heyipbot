import requests
import os

URL = "https://api.telegram.org/"
token = "bot....."
method = "sendMessage"
chatID = 1111111111
folder = os.getcwd()+os.sep+".IP"

def checkIP():
    result = []
    newIP = str(requests.get("https://ifconfig.me/").text)

    if not os.path.exists(folder):
        os.mkdir(folder)

    if os.path.exists(folder+os.sep+"IP.txt"):
        with open(folder+os.sep+"IP.txt","r") as file:
            oldIP = file.read().replace("\n","")
            file.close()

        print("IP antigua: "+oldIP+"\nIP nueva:   "+newIP)

        if newIP != oldIP:
            os.remove(folder+os.sep+"IP.txt")
            with open(folder+os.sep+"IP.txt","w") as file:
                file.write(str(newIP))
                file.close()

            result.append(True)

        else:
            result.append(False)

    else:
        with open(folder+os.sep+"IP.txt","w") as file:
            file.write(str(newIP))
            file.close()
            
        result.append(True)

    result.append(str(newIP))
    return result

def sendmessage(IP):
    data = {'chat_id': chatID, 'text': 'La IP ha cambiado 🔄\nLa nueva IP es: '+str(IP)}
    print(data)
    r = requests.post(URL+token+"/"+method, data).json()
    print(r)

def main():
    IP_has_Changed = checkIP()
    print("¿Ha cambiado la IP? "+str(IP_has_Changed))

    if IP_has_Changed[0]:
        sendmessage(IP_has_Changed[1])

if __name__ == "__main__":
    main()
