import customer as cus


print(globals)
def workMode():
    task=int(input("\n 1. add customer \n 2. print all customer"))
    match task:
        case 1:
            num= int(input("\n how many customer you want to add ?").strip())
            for i in range(num):
                cus.add_customer()
            workMode()
        case 2:
            cus.print_allCustomer()
            workMode()

if __name__=="__main__":
    print("Hey, admin what you want to do today!")
    workMode()
