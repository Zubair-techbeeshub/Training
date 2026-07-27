import requests
URL = "https://jsonplaceholder.typicode.com/users"
def get_all_users():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        users = response.json()
        return users
    except requests.exceptions.RequestException as e:
        print(f"Error while calling API: {e}")
        return None

def display_users(users):
    for user in users:
        print(f"Name    : {user['name']}")
        print(f"Email   : {user['email']}")
        print(f"City    : {user['address']['city']}")
        print(f"Company : {user['company']['name']}")
        print("-" * 40)
def main():
    users = get_all_users()
    if users:
        display_users(users)
    else:
        print("No users to display.")


if __name__ == "__main__":
    main()
