import requests

def fetch_amount_for_denom(address):
    url = f"https://celatone-api-prod.alleslabs.dev/v1/initia/initiation-1/accounts/{address}/balances"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for item in data:
                if item['denom'] == "move/944f8dd8dc49f96c25fea9849f16436dcfa6d564eec802f3ef7f8b3ea85368ff":
                    # breakpoint()
                    amount = int(item['amount']) / 1000000  # Поділити на 100000
                    amount = round(amount, 2)  # Обрізати до 2 значень після коми
                    return amount

            # Якщо немає відповідного denom, повертаємо None або позначку, яку ви вважаєте за кращу
            return None
        else:
            print(f"Помилка запиту для адреси {address}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту для адреси {address}: {e}")
        return None

def main():
    addresses_file = "addresses.txt"
    with open(addresses_file, 'r') as file:
        addresses = file.read().splitlines()

    for address in addresses:
        amount = fetch_amount_for_denom(address)
        if amount is not None:
            print(f"{amount}")
            # print(f"{address}: {amount}")
        else:
            print(f"0")
            # print(f"Дані для адреси {address} не знайдено")

if __name__ == "__main__":
    main()
