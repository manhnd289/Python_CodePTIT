if __name__ == "__main__":
    
    with open("CONTACT.in", "r") as file:
        lines = file.readlines()

    lines = [line.strip().lower() for line in lines]
    lines = set(lines)
    print(*sorted(lines), sep = "\n")