#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    person = dir(hidden_4)
    for name in person:
        if not name.startswith("__"):
            print(name)
