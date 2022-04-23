from generate_data import gen


def main():
    data = gen(count=1)
    for d in data:
        print(d)


if __name__ == "__main__":
    main()
