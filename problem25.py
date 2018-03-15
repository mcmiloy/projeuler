def fibogo():
    fibolist=[1,1]
    def nextfibo():
        tmp1, tmp2 = fibolist[-1], fibolist[-2]
        fibolist.append(tmp1 + tmp2)
        return (fibolist[-1],len(fibolist))
    
    return nextfibo

def run():
    go = fibogo()
    while True:
        temp = go()
        if temp[0] >= 10**999:
            print(temp[1])
            break

if __name__ == '__main__':
    run()































            


