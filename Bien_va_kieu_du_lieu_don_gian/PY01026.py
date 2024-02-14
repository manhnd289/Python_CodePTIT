if __name__ == "__main__":

    for t in range(int(input())):

        s1, s2 = input(), input()

        if "".join(sorted(s1)) == "".join(sorted(s2)): isValid = True
        else: isValid = False

        print(f"Test {t+1}: " + ("YES" if isValid else "NO"))
