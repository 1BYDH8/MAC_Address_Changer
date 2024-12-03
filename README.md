# 🛠️ MAC Address Changer

A Python script to modify the MAC (Media Access Control) address of a network interface, enhancing privacy, aiding in network setup testing, or debugging connectivity issues.

---

## 🚀 Features
- 🔄 **MAC Address Modification**: Change the MAC address for any specified interface.
- ✅ **Verification**: Confirms the success of the MAC address change.
- 📟 **Command-Line Interface**: Simple and easy to use.

---

## 📋 Requirements
- 🐍 **Python 3.x**  
- 🔑 **Root/Administrator Privileges**  
- 💻 `ifconfig` Command (Available on Unix/Linux)

---

## 🛠️ Installation and Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the script's directory.
3. Run the script using the following format:

```bash
python3 mac_changer.py -i <interface> -m <new_mac>
```
## Example

```bash
python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

# 🔍 How It Works

1. Input Handling: The user provides:
    - Interface name (`-i`)
    - New MAC address (`-m`)
2. MAC Check: Displays the current MAC address.
3. Change Execution: Updates the MAC address.
4. Validation: Verifies and reports success or failure.

# 🖥️ Sample Output
```plaintext
Current MAC = 12:34:56:78:9A:BC
[+] Changing MAC Address for eth0 to 00:11:22:33:44:55
[+] MAC address was successfully changed to 00:11:22:33:44:55
```

# ⚠️ Disclaimer
- Use this script responsibly and ensure you have authorization before modifying network settings. Unauthorized changes may lead to legal consequences.

# 🛡️ Limitations
- Requires root privileges.
- Supports only Unix-based systems (not Windows).
