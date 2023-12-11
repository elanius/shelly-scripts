import json
import requests
import argparse


def send_rpc_call(shelly_ip, rpc_payload):
    try:
        response = requests.post(f"http://{shelly_ip}/rpc", json=rpc_payload)
        return response.status_code, response.text
    except requests.RequestException as e:
        return None, str(e)


def process_commands(filename, shelly_ip):
    with open(filename, "r") as file:
        commands = json.load(file)

    for cmd in commands:
        status, message = send_rpc_call(shelly_ip, cmd)
        print(f"Status: {status}, Message: {message}")


def main():
    parser = argparse.ArgumentParser(description="Send RPC commands to Shelly device.")
    parser.add_argument("--ip", help="IP address of the Shelly device", default="192.168.10.201")
    parser.add_argument("--commands", help="File containing list of JSON commands", required=True)

    args = parser.parse_args()

    process_commands(args.commands, args.ip)


if __name__ == "__main__":
    main()
