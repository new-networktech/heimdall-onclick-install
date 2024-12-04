# Heimdall One-Click Installer

This project provides an easy, automated way to set up and update Heimdall on your server using a Python script. It also sends a notification to your Telegram chat when the installation or update completes.

## Features

- Automatically installs Heimdall with all dependencies.
- Uses Ansible and Docker to ensure a reliable setup.
- Sends a Telegram notification upon successful installation or update.

## Prerequisites

- A fresh Ubuntu 22 server.
- Basic familiarity with using the command line (no technical expertise required).
- A Telegram bot token and your Telegram chat ID.

## How to Use

### 1. Run the Installation Command

Copy and paste the following command into your terminal to install the necessary tools, download the project, and prepare your server:

```bash
sudo apt update -y && sudo apt install -y git python3 python3-pip && pip3 install colorama && git clone https://github.com/new-networktech/heimdall-onclick-install.git && cd heimdall-onclick-install
```

This command will:

- Update your server's package list.
- Install essential tools (git, python3, python3-pip).
- Install the colorama library for Python.
- Clone the repository and navigate to the project directory.

### 2. Run the Script

Run the installer script using Python:

```bash
python3 setup_heimdall.py
```

### 3. Follow the Prompts

The script will ask for two pieces of information:

- **Telegram Bot Token:**
    - Create a bot using BotFather on Telegram.
    - Copy the token provided by BotFather.
- **Telegram Chat ID:**
    - Send a message to your bot and visit:
        ```bash
        https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
        ```
    - Look for `"chat":{"id":<YOUR_CHAT_ID>}` in the response.
    - Enter these details when prompted.

## What the Script Does

- Installs all required software (git, ansible, docker.io, and more).
- Installs the Python library colorama for colored output (if not already installed).
- Creates configuration files and an Ansible playbook.
- Deploys Heimdall using Docker.
- Sends a Telegram notification to confirm success.

## Access Heimdall

Once the setup completes, open your browser and go to:

```arduino
http://<your-server-ip>:8080
```

Replace `<your-server-ip>` with your server’s actual IP address.

## Troubleshooting

If you encounter issues:

- Make sure you have entered the correct Telegram bot token and chat ID.
- Ensure you are running the script on Ubuntu 22 or a compatible version.
- Re-run the script if necessary:

    ```bash
    python3 setup_heimdall.py
    ```

## Contributing

If you have suggestions or improvements, feel free to fork this repository and submit a pull request. Non-technical feedback is also welcome!

## License

This project is licensed under the MIT License.

## Support

For additional help, please contact:

- **Email:** support@new-networktech.com
- **Telegram:** Support Group

## Example Screenshot

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