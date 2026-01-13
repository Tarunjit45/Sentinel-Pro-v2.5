\# 🛰️ Sentinel Pro: Terminal Command Center



!\[Python](https://img.shields.io/badge/python-3.12-blue.svg)

!\[License](https://img.shields.io/badge/license-MIT-green.svg)

!\[Build](https://img.shields.io/badge/build-passing-brightgreen.svg)



\*\*Sentinel Pro\*\* is a high-performance CLI dashboard that transforms your Windows Terminal into a system-monitoring command center. Built for developers who live in the terminal.



\## 🚀 Real-World Utility

\- \*\*Bloatware Detection:\*\* Automatically flags processes consuming >10% RAM.

\- \*\*Network Diagnostic:\*\* Real-time latency tracking to Cloudflare (1.1.1.1).

\- \*\*System Health Scoring:\*\* A proprietary algorithm to determine hardware stability.

\- \*\*GitHub Intelligence:\*\* Live API integration to track repository engagement.



\## 🛠️ Architecture

The system utilizes a multi-threaded layout engine to render hardware metrics and API data simultaneously without UI blocking.







\## 📥 Installation

```bash

git clone \[https://github.com/YOUR\_USERNAME/GhostPortfolio.git](https://github.com/YOUR\_USERNAME/GhostPortfolio.git)

cd GhostPortfolio

pip install -r requirements.txt

python dossier.py





---



\### Step 3: Package it for Recruiters (.exe)

Now, let’s create that standalone file so recruiters can run it without needing Python. Run this command:



```powershell

pip install pyinstaller

pyinstaller --onefile --name "Sentinel\_Pro" dossier.py

