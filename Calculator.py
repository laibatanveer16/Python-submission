import fileforcalculator

def main():

        while (True):
            fileforcalculator.choices()
            choice = input('\nEnter Your Choice(1-4): ')

            if choice == '1':
                print(fileforcalculator.add())

            elif choice == '2':
                print(fileforcalculator.subtract())

            elif choice == '3':
                print(fileforcalculator.multiply())

            elif choice == '4':
                print(fileforcalculator.divide())


#TO ASK FOR PERFORMING ANOTHER OPERATION

            next_calculation = input("\n Do You Want To Perform Another calculation? (yes/no): ")
            if next_calculation == "no":
                break


            else:
                print("Alright")

main()


