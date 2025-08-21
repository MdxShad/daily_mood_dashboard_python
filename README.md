# 🧘‍♂️ Daily Mood & Productivity Dashboard

A fully automated personal mood tracker and productivity logger — powered by GitHub Actions, `matplotlib`, `Chart.js`, and calplot. Visualize your emotional journey and productivity trends over time, automatically updated daily!

---

## 🌟 Features

- ✅ **Randomized Mood & Productivity Log**
- 📈 **Mood + Productivity Line Chart**
- 📆 **Calendar Heatmap**
- 💬 **Motivational Quote of the Day**
- 🌓 **Dark Mode Toggle**
- 📊 **Weekly Averages & Interactive UI**
- ⚙️ **GitHub Actions Automation**

---

## 📁 Project Structure

```
daily-mood-dashboard/
├── .github/workflows/    # GitHub Actions workflow
│   └── update.yml
├── plots/                # Python scripts and generated plots
│   ├── generate_plot.py
│   └── generate_calendar.py
├── docs/                 # GitHub Pages assets (auto-copied)
│   ├── dashboard.html
│   ├── mood_trend.png
│   ├── mood_calendar.png
│   └── log.md
├── log.md                # Main mood and productivity log
├── README.md             # This file
└── LICENSE
```

---

## 🚀 How It Works

1. **Every day at 04:15 UTC**, GitHub Actions runs:
   - Picks a random mood (`😞` to `😄`)
   - Picks a random productivity level (`Low`, `Medium`, `High`)
   - Adds a motivational quote
   - Appends to `log.md`

2. Python scripts generate:
   - A **line chart** of mood/productivity trends
   - A **calendar heatmap** of mood scores

3. All files are copied to the `docs/` folder, powering GitHub Pages.

---

## 📦 Setup Instructions

> If you're forking or customizing this:

1. **Clone this repo:**

```bash
git clone https://github.com/Mohdshaadsonofvakeel/daily_mood_dashboard_python
cd daily-mood-dashboard
```

2. **Install dependencies (locally for testing):**

```bash
pip install matplotlib pandas calplot
```

3. **Run scripts manually if needed:**

```bash
python plots/generate_plot.py
python plots/generate_calendar.py
```

4. **Start committing!** GitHub Actions will take over from there.

---

## ⚙️ GitHub Actions Workflow

**`.github/workflows/update.yml`** does all the automation:

- Schedules a run daily
- Randomly generates mood & productivity log entries
- Adds a motivational quote
- Generates plots
- Pushes results to `docs/`

No manual work required once set up.

---

## 🎨 UI Highlights

- 📊 Interactive mood & productivity chart (via `Chart.js`)
- 📆 Clean heatmap calendar (via `calplot`)
- 🌓 Light/Dark mode toggle
- ✨ Smooth transitions & typography with Google Fonts
- 💬 Auto-updating motivational quotes
- 📘 Log viewer with weekly stats

---

## 🌐 View My Live Dashboard

You can view my live, auto-updating dashboard hosted on GitHub Pages here:

👉 **[https://github.com/Mohdshaadsonofvakeel/daily_mood_dashboard_python/dashboard.html](https://github.com/Mohdshaadsonofvakeel/daily_mood_dashboard_python/dashboard.html)**

Explore:
- 📈 Mood & Productivity Trends  
- 📆 Calendar Heatmap  
- 🧠 Motivational Quotes  
- 🌓 Dark Mode & Interactive UI  
- 💬 Mood Logs & Weekly Summary

---

## ❤️ Credits

- Built with 💻 Python, 🧠 GitHub Actions & 🎨 HTML/CSS/JS
- Inspired by journaling, mental health, and developer dashboards
- Dashboard UI designed by [Mohd SHAD](https://github.com/Mohdshaadsonofvakeel)

---

## 📜 License

[MIT](LICENSE)
