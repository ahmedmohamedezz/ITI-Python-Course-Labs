import time


def main() -> None:
    lst = list(range(0, 10_000_000 + 5))
    st = set(lst)

    # linear search O(n)
    start = time.time()
    print(1_000_000 in lst)
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

    # search using hash value O(1)
    start = time.time()
    print(1_000_000 in st)
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")


if __name__ == "__main__":
    main()
