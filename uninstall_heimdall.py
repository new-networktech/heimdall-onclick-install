import os
import subprocess

def remove_heimdall_container():
    """Stop and remove the Heimdall Docker container."""
    print("Stopping and removing Heimdall container...")
    subprocess.run(["docker", "stop", "heimdall"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["docker", "rm", "heimdall"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Heimdall container removed.")

def remove_ansible_files():
    """Remove Heimdall-related Ansible files and configurations."""
    print("Removing Heimdall-related Ansible files...")
    if os.path.exists("heimdall"):
        subprocess.run(["rm", "-rf", "heimdall"])
        print("Ansible files removed.")
    else:
        print("No Ansible files found to remove.")

def remove_docker_image():
    """Remove the Heimdall Docker image."""
    print("Removing Heimdall Docker image...")
    subprocess.run(["docker", "rmi", "-f", "lscr.io/linuxserver/heimdall:latest"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Heimdall Docker image removed.")

def uninstall_prerequisites():
    """Optionally uninstall the prerequisites."""
    print("Do you want to uninstall prerequisites like Docker, Ansible, and Git? (yes/no)")
    if input().strip().lower() == "yes":
        print("Uninstalling prerequisites...")
        subprocess.run(["sudo", "apt", "remove", "--purge", "-y", "ansible", "git", "docker.io", "python3-pip"])
        subprocess.run(["sudo", "apt", "autoremove", "-y"])
        print("Prerequisites uninstalled.")
    else:
        print("Skipping prerequisite uninstallation.")

def main():
    print("Starting Heimdall uninstallation process...")
    remove_heimdall_container()
    remove_docker_image()
    remove_ansible_files()
    uninstall_prerequisites()
    print("Uninstallation complete.")

if __name__ == "__main__":
    main()
