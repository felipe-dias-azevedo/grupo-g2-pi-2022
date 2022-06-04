def getlist() -> tuple:
    with open("tweets/profanity_ptbr.txt") as f:
        return tuple(map(lambda x: x.lower().replace('\n', ''), f.readlines()))


if __name__ == "__main__":
    words = getlist()
    print(words[:10])
