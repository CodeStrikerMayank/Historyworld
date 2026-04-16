# 🌍 CORE SHADOW – Geopolitical Simulation Terminal

A **cinematic, terminal-based geopolitical simulation system** built in Python using the **Rich library**.
Designed to visualize historical global events and simulate **future strategic scenarios** with an immersive war-room interface.

---

## ⚙️ Features

### 🔐 1. Biometric Access Simulation

* Animated **neural scan initialization**
* Typewriter-style identity reveal
* War-room style terminal access system

### 📊 2. Historical Event Engine

* Reads structured data from a **CSV file**
* Displays:

  * Year
  * Strategic Event
  * Leader
  * Power Shift
  * Risk Level

### 📈 3. Dynamic Risk Visualization

* Real-time **tension graph**
* Risk-based color themes:

  * 🔵 Low Risk (0–4)
  * 🟡 Medium Risk (5–7)
  * 🔴 High Risk (8–10)

### 🧠 4. Intelligence Sidebar

Displays contextual insights:

* Geopolitical stakes
* Redacted intelligence
* Key technologies involved

### 🎯 5. Future Scenario Oracle

* Randomized **future predictions**
* Simulates:

  * Risk levels
  * Economic outcomes
  * Survival probability
* Includes cinematic loading + final report

### 🎥 6. Cinematic Terminal UI

* Built with `rich.live`, `layout`, `panels`
* Smooth animations optimized for:

  * Presentations
  * Screen recordings
  * YouTube-style documentaries

---

## 📂 Project Structure

```
project/
│
├── main.py                # Main simulation script
├── major_events.csv      # Input dataset (REQUIRED)
└── README.md             # Documentation
```

---

## 📄 CSV File Format (`major_events.csv`)

Ensure the CSV contains the following headers:

```
Year,Event,Leader,Power_Shift,Risk,Region,Geopolitical_Stakes,Redacted_Fact,Key_Tech
```

### Example Row:

```
2022,Ukraine Conflict,Putin,Regional Instability,8,Europe,Energy crisis escalation,...,...,Missile Systems
```

---

## 🚀 Installation & Setup

### 1. Install Dependencies

```bash
pip install rich
```

### 2. Run the Program

```bash
python main.py
```

---

## ⚠️ Important Notes

* **CSV file must exist**, otherwise simulation will not run.
* Risk values must be **numeric (0–10)**.
* Terminal should support:

  * UTF-8 encoding
  * ANSI colors (recommended: Windows Terminal / VS Code terminal)

---

## 🧠 Design Philosophy

This project is built around:

* **Visual storytelling in terminal**
* **Data-driven geopolitical simulation**
* **Minimal UI, maximum immersion**

---

## 🔧 Possible Improvements

* Add **real-time API data** (news / conflicts)
* Export results to **PDF or logs**
* Add **user input scenarios**
* Integrate **AI-based predictions**

---

## 🛑 Error Handling

Handled cases:

* Missing CSV file
* Keyboard interrupt (safe exit)
* Unexpected runtime errors (logged as `FATAL ERROR`)

---

## 📌 Use Cases

* 🎓 Academic demonstrations
* 🎥 YouTube / content creation
* 🧪 Simulation experiments
* 🛰️ Defense / geopolitics enthusiasts

---

## 👤 Author Signature

```
AUTHOR: Mayank Bhatt
NEURAL SIGNATURE: CORE SHADOW
SYSTEM: WAR_ROOM v13.0
```

---

## 📜 License

Open for educational and personal use. Modify freely.

---

## 🔚 Final Note

> "History is data. The future is probability. Control lies in interpretation."
