# 🛰️ Sentinel Pro: Terminal Command Center v2.5

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![OS](https://img.shields.io/badge/platform-windows-lightgrey.svg)

**Sentinel Pro** is a high-performance CLI dashboard that transforms your Windows Terminal into a real-time system-monitoring command center. Designed for engineers who prioritize low-latency hardware diagnostics and API-driven insights.

<img width="1451" height="710" alt="Screenshot 2026-01-14 155927" src="https://github.com/user-attachments/assets/57279718-3057-4376-b278-32232c7ad4b9" />


## 🌟 Viral Features
- **Interactive Handshake:** Enter any GitHub username to dynamically pull project stats via REST API.
- **Smart Resource Watcher:** Real-time monitoring of CPU/RAM with a built-in **Bloatware Alert** system.
- **Network Diagnostic:** Live latency tracking (Ping) to verify connectivity stability.
- **System Health Algorithm:** A proprietary scoring logic that calculates your PC's "Stability Grade."

## 🧠 Technical Architecture
Sentinel Pro is built on the **Rich Layout Engine**, utilizing a non-blocking refresh loop to update hardware metrics without interrupting API data streams.



### The Health Score Formula:
The system calculates performance based on the following weighted logic:
$$Health Score = 100 - (\frac{CPU_{load} + RAM_{usage}}{2})$$

## 📥 Getting Started

### Prerequisites
- Windows Terminal (Recommended for CRT effects)
- Python 3.10+

### Installation
```bash
# Clone the repository
git clone [https://github.com/Tarunjit45/Sentinel-Pro-v2.5.git](https://github.com/Tarunjit45/Sentinel-Pro-v2.5.git)

# Enter directory
cd Sentinel-Pro-v2.5

# Install dependencies
pip install -r requirements.txt

# Run the Command Center
python dossier.py
