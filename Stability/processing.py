# read and graph the number of events completed from stabilityLog.txt
import matplotlib.pyplot as plt
import datetime, pytz

# convert a UTC timestamp to an ET datetime object
def utc_to_et(utc_dt):
    # add the UTC timezone information to the datetime object
    utc_dt = utc_dt.replace(tzinfo=pytz.utc)
    # convert the UTC datetime object to an ET datetime object
    et_dt = utc_dt.astimezone(pytz.timezone('US/Eastern'))
    # return the ET datetime object
    return et_dt

# main method
id = input("Day: ")
with open(f"Stability\{id}.txt", "r") as f:
    lines = f.readlines()
    x = [] # timestamps
    y = [] # evetns per second
    for line in lines:
        if "UTC" in line:
            # the timestamp string with two spaces
            ts_str = line.strip()
            # remove the extra space from the string
            ts_str = ts_str.replace('  ', ' ')
            # convert it to a datetime object with no extra space in the format code
            ts_dt = datetime.datetime.strptime(ts_str, '%a %b %d %H:%M:%S %Z %Y')
            # add the UTC timezone information
            ts_dt = ts_dt.replace(tzinfo=pytz.utc)
            # convert it to ET
            et_dt = utc_to_et(ts_dt)
            # convert the datetime object to a string
            et_str = et_dt.strftime("%m/%d %H:%M")
            x.append(et_str)
        elif "events per second" in line:
            data = line.strip().split(" ")
            y.append(float(data[-1]))
    # scatter plot
    plt.scatter(x, y, s=1)
    plt.xticks(x[::75],  rotation='vertical')
    plt.xlabel("Time")
    plt.ylabel("Events per second")
    plt.title("Stability Test")
    plt.tight_layout()
    plt.savefig(f"Stability\{id}_{len(x)}.png")
    plt.show()
