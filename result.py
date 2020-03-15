class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll
        
    def DE(self):
        self.sub1_theo=int(input("DE Theory marks   :"))
        self.sub1_prac=int(input("DE parctical marks:"))
        self.sub1total=self.sub1_theo+self.sub1_prac
        print("DE TOTAL:",self.sub1total,"\n")

    def IP(self):
        self.sub2_theo=int(input("IP Theory marks   :"))
        self.sub2_prac=int(input("IP parctical marks:"))
        self.sub2total=self.sub2_theo+self.sub2_prac
        print("IP TOTAL:",self.sub2total,"\n")

    def WP(self):
        self.sub3_theo=int(input("WP Theory marks   :"))
        self.sub3_prac=int(input("WP parctical marks:"))
        self.sub3total=self.sub3_theo+self.sub3_prac
        print("WP TOTAL:",self.sub3total,"\n")
   
    def final_result(self):
        self.result1=self.sub1total+self.sub2total+self.sub3total
        self.per=(100*self.result1)/375
        print("TOTAL MARKS :",self.result1)
        print("PERCENTAGE  :",self.per,"%")
        if self.per>=85:
            print("GRADE A+")
        elif self.per>=35:
            print("GRADE B")
        else:
            print('GRADE F "FAILED" ')

    def display(self):
        print("===============MARKSHEET===============")
        print("Name        :",self.name)
        print("Roll number :",self.roll)
name = input("Please Enter Your Name :")
roll = int(input("Enter Your Roll number :"))
C1=student(name,roll)
C1.DE()
C1.IP()
C1.WP()
C1.display()
C1.final_result()


