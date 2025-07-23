# 🔐 Security Log Analyzer

**A Python-based log analysis tool for detecting suspicious security events — built as a 2nd Year B.Tech Micro Project.**

---

## 📌 Project Overview

This **Security Log Analyzer** is a Python tool developed during the 2nd year of my B.Tech studies as part of a micro project under the Computer Science (Cybersecurity) curriculum. It is designed to automatically parse system log files and detect various security-related events using pattern recognition via regular expressions.

The primary aim is to assist system administrators and security teams in identifying **authentication failures**, **invalid user attempts**, and **web server access events**, and generate a structured report in CSV format for further analysis.

---

## ⚙️ Features

- 🔍 **Log Parsing**: Automatically reads and parses security logs line-by-line.
- 🧠 **Pattern Matching**: Uses regex to identify known patterns (e.g., failed login, invalid user).
- 📊 **CSV Report Generation**: Outputs results with timestamps, IP addresses, usernames, and event types.
- ⚠️ **Warning Logs**: Identifies unmatched or suspicious entries.
- 📁 **Modular Design**: Easy to extend for more log types and formats.

---

## 🧪 Sample Use Case

Analyzing logs such as:


Would output a CSV like:

| timestamp           | ip_address     | event_type    | username |
|---------------------|----------------|----------------|-----------|
| 2025-07-23 10:15:30 | 192.168.1.100  | auth          | admin     |
| 2025-07-23 10:18:55 | 192.168.1.102  | invalid_user  | guest     |

---

## 🛠️ Technologies Used

- **Python 3**
- **Regular Expressions (re)**
- **Pandas**
- **datetime**
- **defaultdict**

---


## 📄 Project Status
✅ Completed as a 2nd-year mini/micro academic project
🚀 Open for improvements: visualization, real-time monitoring, support for more log formats.

## 👨‍💻 Author
Jomin J Joseph
Dept. of CSE (Cybersecurity), 2022-2026 batch,
St. Joseph's College of Engineering and Technology, Palai (SJCET Palai)

## 📚 References
Cybersecurity Essentials by Charles J. Brooks, et al.
Security Log Management by Jacob Babbin
