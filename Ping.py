import os
import matplotlib.pyplot as plt


def getInput() -> str:
    """This function takes the URL and number of pings and return it as String"""
    url = input('Enter URL: ')
    pingCount = input('How many pings (type "U" if unlimited): ')
    return url, pingCount

def choice(url: str, pingCount: str) -> str:
    """This function takes in the URL and number of pings and create a ping command and returns it as a string output"""
    if pingCount.upper() == 'U':
        ping = os.popen(f"ping -t {url}") 
    else:
        ping = os.popen(f"ping -n {pingCount} {url}")
    return ping

def getMs(ping: str) -> list:
    """This function takes in the ping output and extract the time delay (ms) and return them in an array"""
    ping_array = []
    reply_array = []
    time_array = []

    for line in ping:
        ping_array.append(line)

    for line in ping_array:
        if "REPLY FROM" in line.upper():
            reply_array.append(line)
            lineArray = line.split(" ")
            print(lineArray)
            for line in lineArray:
                if "TIME" in line.upper():
                    time = line.replace("ms", "")
                    time = time.replace("time=", "")
                    time_array.append(int(time))
    return time_array

                
def plot(time_array: list) -> None:
    """Takes in the time array and plot in a line graph"""
    plt.plot(time_array)
    #plt.title
    plt.xlabel("")
    plt.ylabel("Time(ms)")
    plt.show()

if __name__== "__main__":
    url, pingCount = getInput()
    ping = choice(url, pingCount)
    time_array = getMs(ping) 
    plot(time_array)