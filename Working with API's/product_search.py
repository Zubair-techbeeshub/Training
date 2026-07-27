import requests
BASE_URL = "https://fakestoreapi.com/products"
def get_product(product_id: int):
    try:
        response = requests.get(f"{BASE_URL}/{product_id}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def display_product(product):
    print("\nProduct Details")
    print("-" * 40)
    print(f"ID       : {product['id']}")
    print(f"Title    : {product['title']}")
    print(f"Price    : ${product['price']}")
    print(f"Category : {product['category']}")
    print(f"Rating   : {product['rating']['rate']}")
    print(f"Reviews  : {product['rating']['count']}")
    print("-" * 40)

def main():
    product_id = input("Enter Product ID (1-20): ")
    if not product_id.isdigit():
        print("Please enter a valid number.")
        return
    product = get_product(int(product_id))
    if product:
        display_product(product)
    else:
        print("Product not found.")

if __name__ == "__main__":
    main()
