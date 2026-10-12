import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_command(command)
    except NetmikoAuthenticationException as error:
        print(f"[AUTH ERROR] {device['host']}: {error}")
    except NetmikoTimeoutException as error:
        print(f"[TIMEOUT / UNREACHABLE] {device['host']}: {error}")


def send_config_commands(device, config_commands, log=True):
    if log:
        print(f"Connecting to {device['host']}...")
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_config_set(config_commands)
    except NetmikoAuthenticationException as error:
        print(f"[AUTH ERROR] {device['host']}: {error}")
    except NetmikoTimeoutException as error:
        print(f"[TIMEOUT / UNREACHABLE] {device['host']}: {error}")


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    command = "show ip interface brief"
    for dev in devices:
        print(send_show_command(dev, command))


    commands = [
        "interface loopback 99",
        "description Netmiko test",
        "ip address 99.99.99.99 255.255.255.255",
    ]
    for dev in devices:
        print(send_config_commands(dev, commands))
        print(send_config_commands(dev, commands, log=False))
