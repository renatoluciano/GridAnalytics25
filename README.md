# 🏎️ GridAnalytics25 - F1 Telemetry Dashboard

[![Python](https://shields.io)](https://python.org)
[![Django](https://shields.io)](https://djangoproject.com)
[![Docker](https://shields.io)](https://docker.com)
[![FastF1](https://shields.io)](https://github.com)

**GridAnalytics25** is a web-based telemetry dashboard built with **Django** and **Docker** designed to track and analyze driver position variations (Starting Grid vs. Final Race Finish) across all circuits of the **2025 Formula 1 season**. 

The application utilizes the **FastF1** library to hook into official data, **Pandas** for data engineering, and **Chart.js** to render rich interactive telemetry matrix flows and charts.

---

## 📊 Key Features

* **Dynamic 2025 Calendar:** Automatically fetches and maps the official 2025 Grand Prix event schedule.
* **Position Shift Matrix:** Deep analytics tracking exactly where drivers started vs. where they finished.
* **Net Overtake Differential:** Aggregated real-time metrics showing total positions gained per session.
* **Instant Filter & Search:** Client-side live search filtering drivers or constructors instantaneously.
* **Interactive Charting:** Built-in charts displaying progression flow maps and bar distributions.
* **Persistent Data Caching:** Custom volume mapping within Docker to prevent API throttling and accelerate loading times.

---

## 📂 Project Architecture

```text
GridAnalytics25/
│
├── core/                  # Main Django configuration directory
│   ├── settings.py        # Global settings (Allowed Hosts updated)
│   └── urls.py            # Global routing index
│
├── analisador/            # Core application folder
│   ├── static/
│   │   └── analisador/
│   │       ├── css/f1_styles.css  # Premium custom dark F1 theme
│   │       └── js/f1_charts.js    # Chart.js charting & loading engine
│   ├── templates/
│   │   └── analisador/dashboard.html
│   ├── f1_service.py      # FastF1 interface layer & pipeline
│   ├── urls.py            # Local app endpoints
│   └── views.py           # Backend metric aggregation controller
│
├── data_cache/            # Shared volume for fast persistent F1 API data
├── Dockerfile             # Multi-stage python environment compiler
├── docker-compose.yml     # Multi-container conductor orchestration
└── requirements.txt       # Stack dependencies
```

---

## 🚀 Getting Started (Quick Run)

### Prerequisites
Make sure you have [Docker Desktop](https://docker.comproducts/docker-desktop/) installed on your machine (Windows, Mac, or Linux).

### 1. Clone the Repository
```bash
git clone https://github.com
cd GridAnalytics25
```

### 2. Launch the Application Container
Run the orchestration engine to compile the environment and spin up the internal Django server:
```bash
docker compose up --build
```

### 3. Access the Telemetry Deck
Open your preferred browser and navigate to:
👉 **[http://localhost:8000](http://localhost:8000)**

> 💡 **Note on First Load:** When pulling telemetry for a specific circuit the very first time, the screen might take a moment to respond. This is normal behavior, as the backend is downloading large official log archives into the `data_cache/` folder. Subsequent loads of that circuit will be instantaneous.

---

## 🔧 Technologies Used

* **Backend Framework:** Django (v5.0)
* **Data Telemetry Engine:** FastF1 Python Library
* **Data Wrangling:** Pandas & NumPy
* **Containerization:** Docker & Docker Compose
* **Frontend UI:** Bootstrap (v5.3) & Custom CSS
* **Data Visualization:** Chart.js (v4.x) via CDN

---

## 🛑 Stopping the System

To shut down the live hot-reloading development container, simply press `Ctrl + C` inside your active terminal window, or clean the container resources using:
```bash
docker compose down
```

---

## 📄 License
This project is for portfolio and educational tracking display purposes. All Formula 1 data metrics belong to their respective official providers via the FastF1 framework integration API.
