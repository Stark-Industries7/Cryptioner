class Cryptioner:
    def __init__(self,sttr,enkey):
        self.sttr = sttr
        self.enkey = enkey
    def Encrypt(self):
        return self.enkey.join(self.sttr)
    def Decrypt(self):
        return self.sttr.split(self.enkey)


def main():
    print("------------------------Welcome To Cryptioner------------------------\n")
    mainString = input("enter your string : ")
    print()
    encryptStr = input("enter your encryption key : ")
    print()

    crypt = Cryptioner(mainString,encryptStr)
    enStr = crypt.Encrypt()
    deLst = crypt.Decrypt()
    deStr = "".join(deLst)

    print("The encrypted string is : ", enStr,"\n")
    print("String after decryption is : ", deStr,"\n")
    print("Thank you for using Cryptioner!😉 \n")
    
if __name__ == "__main__":
    main()
