from model import category, expense

class app:
    catlist = []
    explist = []
    def startapp(self):
        while True:
            choice = self.printoptions()
            if choice == 1:
                self.addcategory()
            elif choice == 2:
                self.categorylisting()
            elif choice == 3:
                self.addexpense()
            elif choice == 4:
                self.reportCatWise()
            elif choice == 8:
                break

    def printoptions(self):
        print("1. Add Category")
        print("2. Category Listing")
        print("3. Expense Entry")
        print("4. Report: CatWise")
        print("5. Report: Month")
        print("6. Report: MonthRange")
        print("7. Report: Amount")
        print("8. Exit")
        ch = int(input("Enter your choice: "))
        return ch

    def addcategory(self):
        id = int(input("Enter Category ID: "))
        nm = input("Enter Category Name: ")

        c = category()
        c.setcatId(id)
        c.setcatName(nm)

        app.catlist.append(c)
        print("Category Added!")

    def categorylisting(self):
        print("======Available Categories======")
        for i in app.catlist:
            print(i.getcatid(), i.getcatname())

    def addexpense(self):
        #amount, remark, date, cid
        self.categorylisting()
        catid = int(input("Select Category: "))

        amount = float(input("Enter Amount: "))
        remark = input("Enter Remark: ")
        date = input("Enter Date (dd/mm/yyyy): ")

        e = expense()
        e.setAmount(amount)
        e.setRemark(remark)
        e.setDate(date)
        e.setcategoryId(catid)

        app.explist.append(e)
        print("Expenses Added!")

    def reportCatWise(self):
        self.categoryListing()
        cid = int(input("Select Category: "))

        for e in app.explist:
            if e.getcategoryid() == cid:
                print(e.getAmount(), e.getRemark(),e.getDate())
        


app().startapp()
