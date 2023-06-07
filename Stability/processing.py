# read and graph the number of events completed from stabilityLog.txt
import matplotlib.pyplot as plt
id = input("Day: ")
with open(f"Stability\{id}.txt", "r") as f:
    lines = f.readlines()
    x = [] # timestamps
    y = [] # evetns per second
    for line in lines:
        if "Jun" in line:
            data = line.strip().split(" ")[4] # timestamp
            # convert UTC to ET
            if int(data.split(':')[0]) < 4:
                data = f"{int(data.split(':')[0]) + 20}:{data.split(':')[1]}"
            else:
                data = f"{int(data.split(':')[0]) - 4}:{data.split(':')[1]}"
            # convert 24 hour time to 12 hour time
            if int(data.split(':')[0]) > 12:
                data = f"{int(data.split(':')[0]) - 12}:{data.split(':')[1]} PM"
            elif int(data.split(':')[0]) == 0:
                data = f"12:{data.split(':')[1]} AM"
            else:
                data = f"{int(data.split(':')[0])}:{data.split(':')[1]} AM"
            if "Mon" in line:
                data = "Mon " + data
            elif "Tue" in line:
                data = "Tue " + data
            elif "Wed" in line:
                data = "Wed " + data
            x.append(data)
        elif "events per second" in line:
            data = line.strip().split(" ")
            y.append(float(data[-1]))
    # scatter plot
    plt.scatter(x, y, s=1)
    plt.xticks(x[::75],  rotation='vertical')
    plt.xlabel("Time")
    plt.ylabel("Events per second")
    plt.title("Stability Test")
    plt.savefig(f"Stability\{id}_{len(x)}.png")
    plt.show()
