import queue

if __name__ == "__main__":

    for _ in range(int(input())):

        n = int(input())
        q = queue.Queue()
        res = []

        q.put("1"); q.put("2")

        cnt = 0
        while cnt < n:

            tmp = q.get()
            if tmp.count("2") > len(tmp)//2:
                cnt += 1
                res.append(int(tmp))

            q.put(tmp + "0")
            q.put(tmp + "1")
            q.put(tmp + "2")

        print(*res)
        
       
        