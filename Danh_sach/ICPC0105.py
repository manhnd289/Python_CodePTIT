import re 

if __name__ == "__main__":

    for _ in range(int(input())):

        num_lst = [int(i) for i in re.findall(r"\d+", input())]
        if len(num_lst) > 0:
            print(max(num_lst))