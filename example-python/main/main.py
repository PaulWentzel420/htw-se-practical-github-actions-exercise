from town import Town

def main():
    t = Town("Dresden", 556780)
    print(t.toString())
    t.residents = -1
    print(t.toString())
    #t.name = ""
    #print(t.toString())
    #123420

if __name__ == "__main__":
    main()