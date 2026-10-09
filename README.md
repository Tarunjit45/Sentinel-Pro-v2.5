# 🛰️ Sentinel Pro v2.5 — Real-Time Terminal Command Center & Diagnostics

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Rich](https://img.shields.io/badge/UI-Rich%20Live%20Terminal-E91E63?style=for-the-badge)](https://rich.readthedocs.io/)
[![Hardware](https://img.shields.io/badge/Diagnostics-psutil-009688?style=for-the-badge)](https://psutil.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Sentinel Pro v2.5** is a terminal-based system monitoring command center built in Python. Designed for developers and system administrators who demand low-latency hardware diagnostics, network health probes, and active process tracking—all rendered in a live, colorized **Rich** terminal layout.

---

## ✨ Features

* 📊 **Live Hardware Telemetry:** Dynamic gauges for CPU utilization, RAM consumption, and disk partition saturation.
* 🌐 **Network Health Probe:** Solves the *"Is my internet slow?"* problem with real-time ping latency checks and gateway reachability.
* ⚙️ **Process Dossier:** Real-time top process inspector with memory and CPU hog identification.
* 🎨 **Colorized Terminal Layout:** Multi-panel dashboard using `rich.live` and `rich.layout` that auto-refreshes without terminal flickering.

---

## 📁 Repository Structure

```text
Sentinel-Pro-v2.5/
├── dossier.py          # Core monitoring loop, Rich layout engine & diagnostic probes
├── requirements.txt    # Dependencies (psutil, rich, requests)
├── LICENSE             # MIT License
└── README.md
```

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/Tarunjit45/Sentinel-Pro-v2.5.git
cd Sentinel-Pro-v2.5

pip install -r requirements.txt
```

### 2. Run Sentinel Pro
```bash
python dossier.py
```

Press `Ctrl+C` to cleanly exit the command center.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
