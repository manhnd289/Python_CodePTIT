class Contact:

    def __init__(self, name, phone_num, time) -> None:
        self.name = name
        self.phone_num = phone_num
        self.time = time

    def __str__(self) -> str:
        return f"{self.name}: {self.phone_num} {self.time}"

if __name__ == "__main__":

    with open("SOTAY.txt", "r") as file:
        lines = file.readlines()
    arr = []

    i = 0
    while i < len(lines):
        if lines[i][:4] == "Ngay": 
            time = lines[i][5:len(lines[i])-1]
            i+=1
        arr.append(Contact(lines[i][:len(lines[i])-1], lines[i+1][:len(lines[i+1])-1], time))
        i += 2

    with open("DIENTHOAI.txt", "w") as file:
        for item in arr:
            item = str(item)
            file.write(item)
            file.write("\n")

