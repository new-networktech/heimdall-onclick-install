import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def install_prerequisites():
    """Install required packages like Ansible, Git, Docker, and Python dependencies."""
    print("Updating sources.list to use old-releases if necessary...")
    subprocess.run(["sudo", "sed", "-i", "s|http://archive.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g", "/etc/apt/sources.list"])

    print("Installing system prerequisites...")
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "install", "-y", "ansible", "git", "docker.io", "python3-pip"])
    
    print("Installing Python dependencies...")
    subprocess.run(["pip3", "install", "--upgrade", "pip"])  
    subprocess.run(["pip3", "install", "colorama"]) 

    print("All prerequisites installed successfully.")

def get_user_input():
    """Get user input for configuration."""
    print(Fore.YELLOW + "Please provide the following details for Heimdall setup:")
    telegram_bot_token = input(Fore.YELLOW + "Enter your Telegram bot token: " + Fore.GREEN).strip()
    telegram_chat_id = input(Fore.YELLOW + "Enter your Telegram chat ID: " + Fore.GREEN).strip()

    return {
        "telegram_bot_token": telegram_bot_token,
        "telegram_chat_id": telegram_chat_id,
    }

def create_ansible_files(config):
    """Generate ansible.cfg, inventory.ini, secrets.yml, and playbook."""
    os.makedirs("heimdall", exist_ok=True)
    os.chdir("heimdall")

    # ansible.cfg
    with open("ansible.cfg", "w") as f:
        f.write("""
[defaults]
inventory      = ./inventory.ini
host_key_checking = False
retry_files_enabled = False
        """.strip())
    print("ansible.cfg created.")

    # inventory.ini
    with open("inventory.ini", "w") as f:
        f.write("""
[heimdall]
localhost ansible_connection=local
        """.strip())
    print("inventory.ini created.")

    # secrets.yml
    with open("secrets.yml", "w") as f:
        f.write(f"""
telegram_bot_token: "{config['telegram_bot_token']}"
telegram_chat_id: "{config['telegram_chat_id']}"
        """.strip())
    print("secrets.yml created.")

    # update_heimdall.yml
    with open("update_heimdall.yml", "w") as f:
        f.write(f"""
---
- name: Update Heimdall
  hosts: heimdall
  become: yes

  vars_files:
    - secrets.yml

  tasks:
    - name: Pull the latest Heimdall image
      shell: docker pull lscr.io/linuxserver/heimdall:latest
      become: true

    - name: Stop the existing Heimdall container
      shell: docker stop heimdall || true
      become: true

    - name: Remove the existing Heimdall container
      shell: docker rm heimdall || true
      become: true

    - name: Start the updated Heimdall container
      shell: >
        docker run -d
        --name=heimdall
        -e PUID=1000
        -e PGID=1000
        -e TZ=Europe/Berlin
        -v /path/to/heimdall/config:/config
        -p 8080:80
        --restart unless-stopped
        lscr.io/linuxserver/heimdall:latest
      become: true

    - name: Notify on Telegram about update completion
      local_action:
        module: uri
        url: "https://api.telegram.org/bot{{{{ telegram_bot_token }}}}/sendMessage"
        method: POST
        body_format: json
        body:
          chat_id: "{{{{ telegram_chat_id }}}}"
          text: " 🟢 Heimdall was updated successfully with Ansible."
      delegate_to: localhost
        """.strip())
    print("update_heimdall.yml created.")

def run_ansible_playbook():
    """Run the Ansible playbook."""
    print("Running the Ansible playbook...")
    result = subprocess.run(["ansible-playbook", "-i", "inventory.ini", "update_heimdall.yml"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode != 0:
        print("An error occurred while running the playbook. Please check the output above.")

def main():
    print(Fore.CYAN + "Welcome to the Heimdall Ansible Automation Setup!")
    install_prerequisites()
    config = get_user_input()
    create_ansible_files(config)
    print(Fore.GREEN + "All files created successfully!")
    print(Fore.YELLOW + "You can now run the playbook using: " + Fore.CYAN + "ansible-playbook -i inventory.ini update_heimdall.yml")
    if input(Fore.YELLOW + "Would you like to run the playbook now? (yes/no): " + Fore.GREEN).strip().lower() == "yes":
        run_ansible_playbook()

if __name__ == "__main__":
    main()
