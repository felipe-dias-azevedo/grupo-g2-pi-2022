from generate_data import gen


def main():
    data = gen(count=100)
    for d in data:
        print(d.__dict__)


if __name__ == "__main__":
    main()
