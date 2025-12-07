
---

# ✅ **README.md**

````markdown
# zabbix_mock_data_sender

A lightweight utility script for sending **mock (hardcoded) metrics** to a Zabbix server using the `zabbix_sender` command-line tool.  
This script is useful for:

- Testing Zabbix trapper items  
- Verifying metric ingestion from local systems  
- Debugging Zabbix monitoring pipelines  
- Demonstrating Zabbix sender usage in labs, demos, or automation setups  

No real business logic is included. All values are intentionally hardcoded for testing purposes.

---

## 🔧 Features

- Sends multiple Zabbix trapper values in one execution  
- Uses `zabbix_sender` under the hood  
- Clean output showing the executed command and response  
- Configurable host, server IP, sender binary path, and trapper keys  
- Minimal, readable Python code ready for modification  
- Suitable for open-source and educational usage  

---

## 📦 Requirements

- Python **3.6+**
- Zabbix sender installed locally  
  Example (Debian/Ubuntu):

```bash
sudo apt install zabbix-sender
````

---

## ⚙️ Configuration

Edit the following variables inside the script:

```python
zabbix_sender_path = "/usr/bin/zabbix_sender"
zabbix_server_ip   = "x.x.x.x"
zabbix_hostname    = "HOSTNAME"
```

Make sure:

* `HOSTNAME` matches the host name defined in Zabbix frontend
* Trapper items exist for each key you plan to send

Example keys used:

```python
key_status = "sms.job.status"
key_time_str = "sms.job.time_str"
key_individual = "sms.job.individual_value"
```

---

## ▶️ Usage

Run the script directly:

```bash
python3 zabbix_mock_data_sender.py
```

Example output:

```
Running command: /usr/bin/zabbix_sender -z x.x.x.x -s HOSTNAME -k sms.job.status -o 1
Exit code: 0
STDOUT:
info from server: "processed: 1; failed: 0; total: 1; seconds spent: 0.0001"
```

---

## 🧪 What Gets Sent?

The script sends:

* a numeric test value (`status_value`)
* a timestamp (`time_value`)
* another numeric metric (`individual_value`)

All are mock/test values only.

---

## 📄 License

This project is released under the **MIT License**.
You may freely modify and reuse it in other projects.

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome!

* Add CLI arguments
* Add JSON/YAML config loader
* Add bulk metric sending
* Add error handling or logging

Open an issue or submit a pull request.

---

## 📬 Contact

If you have questions or need improvements, feel free to open an issue on GitHub.

pasha.koroghli@gmail.com

```

---

