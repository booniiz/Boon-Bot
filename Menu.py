import URLGen
import refresher


class Menu(object):
    def __init__(self):
        self.choice = 0  # GLOBAL CHOICE VARIABLE

    def description(self):
        url = ""

        while self.choice < 1 or self.choice > 3:
            print("BOON BOT")
            print("--------")
            print("1.Buying Bot")
            print("2.URL Generator")
            print("3.Support & Information")
            self.choice = input('\nPlease enter the number(1-3): ')
            # ERR-INPUT-CHECKING-------------------------------------------------
            if len(self.choice) == 0 or len(self.choice) > 1:
                self.choice = 0
                print("ERR:INVALID CHOICE\n\nPlease choose one of the following")
            elif 47 < ord(self.choice) < 58:
                self.choice = int(self.choice)
            else:
                self.choice = 0
                print("ERR:INVALID CHOICE\n\nPlease choose one of the following")
            # ERR-INPUT-CHECKING-------------------------------------------------
            # BUYING-MENU-------------------------------------------------------------
            if self.choice == 1: # BUYING
                print("\nBUYING BOT")
                print("----------")
                url = input("Please enter the URL:")
                refresher.buyBot(url)
                # print("If the item cannot yet be bought, then you can set up the refresh rate")
                # choice = input("Do you want to enter the refresh rate?(y/n)")
                # if choice == "y":
                #     waitAmount = input("Enter the refresh rate: ")
                #     check = refresher.buyBot(url, waitAmount)
                # elif choice == "n":
                #     check = refresher.buyBot(url, 0)
                # else:
                #     self.choice = 0
                #     print("ERR:INVALID CHOICE")
            # BUYING-MENU-------------------------------------------------------------
            # URL-MENU-START----------------------------------------------------------
            elif self.choice == 2: # URL GENERATOR
                webChoice = 0
                while webChoice < 1 or webChoice > 3:
                    print("\nURL GENERATOR")
                    print("-------------")
                    print("1.Adidas")
                    # print("2.Nike")
                    print("2.Request other websites")
                    print("3.Return to the previous page")
                    webChoice = input('\nPlease enter the number(1-4): ')
                    # ERR-INPUT-CHECKING-------------------------------------------------
                    if len(webChoice) == 0 or len(webChoice) > 1:
                        webChoice = 0
                        print("ERR:INVALID CHOICE\n\nPlease choose one of the following")
                    elif 47 < ord(webChoice) < 58:
                        webChoice = int(webChoice)
                    else:
                        webChoice = 0
                        print("ERR:INVALID CHOICE\n\nPlease choose one of the following")
                    # ERR-INPUT-CHECKING-------------------------------------------------
                    if webChoice == 1:
                        Model = input('Model #: ')
                        Size = float(input('Size(For women size please enter one size lower): '))
                        gen = URLGen.Generator()
                        url = gen.AdidasURL(Model, Size)
                        print("\nYOUR ADIDAS URL:")
                        print(url)
                        input("\n\nPress Enter to return...")
                        self.choice = 0
                        print("\nRETURNING\n")
                    # elif webChoice == 2:
                    #     print("\nYOUR NIKE URL:")
                    #     print(url)
                    #     input("\n\nPress Enter to return...")
                    #     self.choice = 0
                    #     print("\nRETURNING\n")
                    elif webChoice == 2:
                        print("Please contact email for more support on specific site(s)"
                              "\nSupport Email: booniiz80@gmail.com")
                        input("\n\nPress Enter to return...")
                        self.choice = 0
                        print("\nRETURNING\n")
                    elif webChoice == 3:
                        self.choice = 0
                        print("\nRETURNING\n")
                    else:
                        print("ERR:INVALID CHOICE\n\nPlease choose one of the following")
            # URL-MENU-END------------------------------------------------------------
            elif self.choice == 3:  # INFORMATION
                print("Creator: Boon Chantachaimongkon")
                print("Support Email: booniiz80@gmail.com")
                input("\n\nPress Enter to return...")
                self.choice = 0
                print("\nRETURNING\n")
            else: # ERR: INVALID INPUT
                print("ERR:INVALID CHOICE\nPlease choose one of the following option")
