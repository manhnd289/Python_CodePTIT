if __name__ == "__main__":
    inp = input()
    print("NO" if inp[0] != "6" or inp.count("888") or inp.count("6") + inp.count("8") != len(inp) else "YES")