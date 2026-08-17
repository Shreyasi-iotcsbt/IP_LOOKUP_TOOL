import requests
import os

while True:
    os.system('cls')
    print("IP Lookup Tool")
    x = input("Option (1 = lookup, 2 = quit): ")

    if x == "1":
        os.system('cls')
        print("Welcome to the IP lookup")
        enter_ip = input("Enter target IP: ")

        try:
            r = requests.get(f"http://ip-api.com/json/{enter_ip}")
            data = r.json()
            print("\nResults:")
            print(f"Country: {data['country']}")
            print(f"City: {data['city']}")
            print(f"Region: {data['region']}")
            print(f"Timezone: {data['timezone']}")
        except Exception as e:
            print(f"Error: {e}")

        input("\nPress enter to return...")

    elif x == "2":
        break

    else:
        input("Invalid option. Press enter to try again...")