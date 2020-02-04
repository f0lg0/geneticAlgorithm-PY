def displayBanner():
    banner = open('./banner/banner.txt', 'r', encoding='utf8')
    print(banner.read())

def choice():
    while True:
        choice = int(input(">"))
        if choice == 0:
            break
        elif choice == 1:
            exit()
        else:
            print("Retry")
