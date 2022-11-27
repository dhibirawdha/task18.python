from netmiko import ConnectHandler
import yaml


def send_config_commands(device, config_commands, log=True):
    if log:
        print(f"Connecting to {device['host']}...")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_config_commands(dev, commands))