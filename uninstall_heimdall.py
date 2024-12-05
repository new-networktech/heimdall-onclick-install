Here's the updated **README** with uninstallation instructions added:

---

# **Heimdall One-Click Installer**
This project provides an easy, automated way to set up and update Heimdall on your server using a Python script. It also sends a notification to your Telegram chat when the installation or update completes.

---

## **Features**
- Automatically installs Heimdall with all dependencies.
- Uses Ansible and Docker to ensure a reliable setup.
- Sends a Telegram notification upon successful installation or update.
- Provides an uninstallation option to remove Heimdall and related configurations.

---

## **Prerequisites**
1. A fresh Ubuntu 22 server.
2. Basic familiarity with using the command line (no technical expertise required).
3. A Telegram bot token and your Telegram chat ID.

---

## **How to Use**

### **1. Run the Installation Command**
Copy and paste the following command into your terminal to install the necessary tools, download the project, and prepare your server:
```bash
sudo apt update -y && sudo apt install -y git python3 python3-pip && pip3 install colorama && git clone https://github.com/new-networktech/heimdall-onclick-install.git && cd heimdall-onclick-install
```

This command will:
- Update your server's package list.
- Install essential tools (`git`, `python3`, `python3-pip`).
- Install the `colorama` library for Python.
- Clone the repository and navigate to the project directory.

---

### **2. Run the Script**
Run the installer script using Python:
```bash
python3 setup_heimdall.py
```

---

### **3. Follow the Prompts**
The script will ask for two pieces of information:
1. **Telegram Bot Token**: 
   - Create a bot using [BotFather](https://t.me/botfather) on Telegram.
   - Copy the token provided by BotFather.
2. **Telegram Chat ID**:
   - Send a message to your bot and visit:
     ```
     https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
     ```
   - Look for `"chat":{"id":<YOUR_CHAT_ID>}` in the response.

Enter these details when prompted.

---

## **What the Script Does**
1. Installs all required software (`git`, `ansible`, `docker.io`, and more).
2. Installs the Python library `colorama` for colored output (if not already installed).
3. Creates configuration files and an Ansible playbook.
4. Deploys Heimdall using Docker.
5. Sends a Telegram notification to confirm success.

---

## **Access Heimdall**
Once the setup completes, open your browser and go to:
```
http://<your-server-ip>:8080
```

Replace `<your-server-ip>` with your server’s actual IP address.

---

## **Uninstallation**
To completely remove Heimdall and all related configurations, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd heimdall-onclick-install
   ```

2. Run the uninstallation script:
   ```bash
   python3 uninstall_heimdall.py
   ```

The script will:
- Stop and remove the Heimdall Docker container.
- Delete Heimdall-related Ansible files and configurations.
- Remove the Heimdall Docker image.
- Optionally uninstall prerequisites like Docker, Ansible, and Git.

---

## **Troubleshooting**
If you encounter issues:
- Make sure you have entered the correct Telegram bot token and chat ID.
- Ensure you are running the script on Ubuntu 22 or a compatible version.
- Re-run the script if necessary:
  ```bash
  python3 setup_heimdall.py
  ```

---

## **Contributing**
If you have suggestions or improvements, feel free to fork this repository and submit a pull request. Non-technical feedback is also welcome!

---

## **License**
This project is licensed under the MIT License.

---

## **Support**
For additional help, please contact:
- **Email**: [support@new-networktech.com](mailto:support@new-networktech.com)
- **Telegram**: [Support Group](https://t.me/new_networktech_support)

---

## **Example Screenshot**

Below is an example of how the script will look when running:

```plaintext
Welcome to the Heimdall Ansible Automation Setup!
Installing prerequisites...
Prerequisites installed successfully.
Please provide the following details for Heimdall setup:
Enter your Telegram bot token: ***************
Enter your Telegram chat ID: ********
All files created successfully!
You can now run the playbook using: ansible-playbook -i inventory.ini update_heimdall.yml
```

---

This updated README ensures that users are well-informed about both the installation and uninstallation processes. Let me know if you'd like any further refinements! 😊