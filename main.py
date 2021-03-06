from netmiko import Netmiko
import settings


def main():
    connection = Netmiko(settings.host, settings.port, settings.username, settings.password,
                         device_type=settings.device)
    output = connection.send_command("show run")
    print(output)
    connection.disconnect()


if __name__ == '__main__':
    main()
