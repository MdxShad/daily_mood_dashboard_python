#empty
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
import os

# Read log file
if not os.path.exists("log.md"):
    print("log.md not found.")
    exit()

dates = []
moods = []
productivity = []

with open("log.md", "r", encoding="utf-8") as f:
    current_date = None
    for line in f:
        if line.startswith("## Log Entry:"):
            timestamp = line.replace("## Log Entry:", "").strip()
            try:
                current_date = datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y")
            except:
                current_date = datetime.utcnow()
        elif "Mood:" in line and "Productivity:" in line:
            mood = line.split("Mood:")[1].split("|")[0].strip()
            prod = line.split("Productivity:")[1].split("|")[0].strip()

            mood_score = {"😞": 1, "🙁": 2, "😐": 3, "🙂": 4, "😄": 5}.get(mood, 3)
            prod_score = {"Low": 1, "Medium": 2, "High": 3}.get(prod, 2)

            moods.append(mood_score)
            productivity.append(prod_score)
            dates.append(current_date)

if dates and moods and productivity:
    df = pd.DataFrame({"Date": dates, "Mood": moods, "Productivity": productivity})
    df.sort_values("Date", inplace=True)

    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Mood"], marker='o', label="Mood", color='teal')
    plt.plot(df["Date"], df["Productivity"], marker='s', label="Productivity", color='orange')
    
    plt.ylim(0, 6)
    plt.yticks([1, 2, 3, 4, 5], ["Very Low", "Low", "Neutral", "Good", "Great"])
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.title("Mood & Productivity Trends")
    plt.grid(True)
    plt.legend()

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()

    os.makedirs("plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("plots/mood_trend.png")
    plt.close()
