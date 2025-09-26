# 4) Product Data Transformer (lambda, map, filter, zip)
#    - Ask user for a list of product names (comma-separated).
#    - Ask user for a list of product prices (comma-separated).
#    - Process them by:
#         - Pairing product with price.
#         - Filtering out items where price <= 0.
#         - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
#    - Save the final result as JSON into "products.json".
#    - Print a preview of the first 5 results.
import json
from decorators import read_comma_separated_nums, read_comma_separated_strings


def run_product_data_transformer() -> None:
    print("---- Product Data Transformer Task(4) ----")
    print(
        "Note: if the length of names list and prices list are the same. the shorter will be considered"
    )

    names = read_comma_separated_strings()
    prices = read_comma_separated_nums()

    # pair product with price.
    products = list(zip(names, prices))

    # filter items where price <= 0
    filteredProducts = list(filter(lambda product: product[1] > 0, products))

    # convert each to dict
    # {"product": name, "price": price, "discounted": price * 0.9}
    products = [
        {"product": pr[0], "price": pr[1], "discounted": round(pr[1] * 0.9, 3)}
        for pr in filteredProducts
    ]

    # save in json
    with open("products.json", "w") as f:
        json.dump(products, f, indent=4)

    # note that with block doesn't have a scope, inner variables are accessed outside
    with open("products.json", "r") as f:
        data = json.load(f)

    # preview
    print("First 5 results (from file): ")
    for i, product in enumerate(data):
        if i >= 5:
            break

        print(product)


def main() -> None:
    run_product_data_transformer()


if __name__ == "__main__":
    main()
