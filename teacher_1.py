
from tabulate import tabulate

def teach_details():
    mydata = [
            ["1","Anuradha Mam ","Web Design","7894561234", "Haryana"], 
            ["2","Jasmeen Mam ","Cyber Security","7894561234", "Punjab"], 
            ["3","Bhavna Mam ","Java","7894561234", "Haryana"], 
            ["4","Minni Mam ","Cyber Security ","7894561234", "Punjab"], 
            ["5","Dolly Mam ","App Development,Database","7894561234", "Haryana"], 
            ["6","Kiranpal Sir ","Python, Data Science","7894561234", "Punjab"], 
        
]
 

    head = ["Teacher_Id", "Name","Subject","Phone Number","State"]
    print(tabulate(mydata, headers=head, tablefmt="grid"))


def teach_salary():
    mydata = [
            ["1","Anuradha Mam ","30000"], 
            ["2","Jasmeen Mam ","25000 ",], 
            ["3","Bhavna Mam ","30000"], 
            ["4","Minni Mam ","26000"], 
            ["5","Dolly Mam ","26000"], 
            ["6","Kiranpal Sir ","85000"], 
        
]
 

    head = ["Teacher_Id", "Name","Salary"]
    print(tabulate(mydata, headers=head, tablefmt="grid"))
 



if __name__ == "__main__":
    teach_details()