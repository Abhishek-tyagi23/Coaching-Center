import st_database
import teacher_1
class Course:
    def Courses(self):
        while(True):

            Details='''\n ******** Course Details ********
        Please choice an option :
        1. Web Development Courses : 
            .Instructor: Colt Steele
            .Platform: Udemy
            .Comprehensive course covering HTML, CSS, JavaScript, Node.js, and more

        2. Learn Python :
            .Platform: MIT OpenCourseWare
            .An introduction to Python programming and computer science concepts.

        3. Core Java :
            .oops Concepts
            .App Development in Java

        4. Machine Learning:
            .Instructor: Andrew Ng
            .A foundational course on machine learning.
            
        5. Data Science :
            .Instructor: Jose Portilla
            .Covers data science concepts using the R programming language.

            
        6. Cyber Security Specialization :
            .Institution: New York University (NYU)

        7. Mobile App Development Courses :
            .Covers Android app development using Java and Kotlin.

        8. Database Management System :
            .Sql/PlSQL
            .Orcal
            .Microsoft SQL Server
           
        9. Go To Home :

        10. Exit the Center :

        '''
            
    

            print(Details)
            b=int(input("Enter a Choice :"))
            if b== 1:
                student2.Feeshtml()
            elif b==2:
                student2.Feespy()   
            elif b==3:
                student2.Feesjava() 
            elif b==4:
                student2.Feesml() 
            elif b==5:
                student2.Feesds() 
            elif b==6:
                student2.Feescs() 
            elif b==7:
                student2.Feesmd() 
            elif b==8:
                student2.Feesdbms() 
            elif b==9:
                main2.main1()
                
            elif b==9:
                print("Thanks for choosing Central library! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  


class Fee:
    def Feeshtml2(self):
        
        fee='''\n ******** Web design Course Fees Details ********
        
        * Web design Course fees :      15000
        * With Certificates      :      +2000 
        * With GST               :      +2000
        * Total fees             :      19000
        
        '''

        print(fee)
    
    def Feeshtml(self):
        while(True):

            fee='''\n ******** Web design Course Fees Details ********
        
        * Web design Course fees :      15000
        * With Certificates      :      +2000 
        * With GST               :      +2000
        * Total fees             :      19000
        
        1. Join Us :
        2. About Us :
        3. Go To Home :
        4. Exit :
        '''

            print(fee)
            f=input("Enter a Choice :")
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()
            elif f==3:
                 main2.main1()
                
        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  

    def Feespy2(self):
        
        fee='''\n ******** Python Course Fees Details ********
        
        * Python Course fees     :      8000
        * With Certificates      :      +2000 
        * With GST               :      +2000
        * Total fees             :      12000
        
        '''

        print(fee)

    def Feespy(self):
        while(True):

            fee='''\n ******** Python Course Fees Details ********
        
        * Python Course fees     :      8000
        * With Certificates      :      +2000 
        * With GST               :      +2000
        * Total fees             :      12000
        
        1. Join Us :
        2. About Us :
        3. Go To Home :
        4. Exit :
        '''

            print(fee)
            f=int(input("Enter a Choice :"))
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()
            elif f==3:
                 main2.main1()
                
        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  

                
    def Feesjava2(self):
        
        fee='''\n ******** Java Course Fees Details ********
        
        * Java Course fees       :      5000
        * With Certificates      :     +1000 
        * With GST               :     +1000
        * Total fees             :      7000
        
        '''

        print(fee)

    def Feesjava(self):
        while(True):

            fee='''\n ******** Java Course Fees Details ********
        
        * Java Course fees       :       5000
        * With Certificates      :      +1000 
        * With GST               :      +1000
        * Total fees             :       7000
        
        1. Join Us :
        2. About Us :
        3. Go To Home :
        4. Exit :
        '''

            print(fee)
            f=int(input("Enter a Choice :"))
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()

            elif f==3:
                  main2.main1()
                
        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  


    def Feesml2(self):
        
        fee='''\n ******** Machine Learning Course Fees Details ********
        
        * Machine Learning fees  :      5000
        * With Certificates      :     +1000 
        * With GST               :     +1000
        * Total fees             :      7000
        
        '''

        print(fee)

    def Feesml(self):
        while(True):

            fee='''\n ******** Machine Learning Course Fees Details ********
        
        * Machine Learning fees  :      5000
        * With Certificates      :     +1000 
        * With GST               :     +1000
        * Total fees             :      7000
        
        1. Join Us :
        2. About Us :
        3. Go To Home :
        4. Exit :
        '''

            print(fee)
            f=int(input("Enter a Choice :"))
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()
            elif f==3:
                main2.main1()

        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  


    def Feesds2(self):
        
        fee='''\n ******** Data Science Course Fees Details ********
        
        * Data Science fees      :      10000
        * With Certificates      :      +1500 
        * With GST               :      +1500
        * Total fees             :      13000
        
        '''

        print(fee)

    def Feesds(self):
        while(True):

            fee='''\n ******** Data Science Course Fees Details ********
        
        * Data Science fees      :      10000
        * With Certificates      :      +1500 
        * With GST               :      +1500
        * Total fees             :      13000
        
        1. Join Us :
        2. About Us :
        3. Go To Home :
        4. Exit :
        '''

            print(fee)
            f=int(input("Enter a Choice :"))
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()
            elif f==3:
                main2.main1()

        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  


    def Feescs2(self):
        
        fee='''\n ******** Cyber Security Course Fees Details ********
        
        * Cyber Security fees    :      15000
        * With Certificates      :      +2000 
        * With GST               :      +2000
        * Total fees             :      19000
        
        '''

        print(fee)

    def Feescs(self):
        while(True):

            fee='''\n ******** Cyber Security Course Fees Details ********
        
        * Cyber Security  fees   :      15000
        * With Certificates      :      +2000 
        * With GST               :      +2000
        * Total fees             :      19000
        
        1. Join Us :
        2. About Us :
        3. Go To Homt :
        4. Exit :
        '''

            print(fee)
            f=int(input("Enter a Choice :"))
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()
            elif f==3:
                main2.main1()

        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  


    def Feesmd2(self):
        
        fee='''\n ******** Mobile App Development Course Fees Details ********
        
        * Mobile App Development fees   :      6000
        * With Certificates             :     +1000 
        * With GST                      :     +1000
        * Total fees                    :      8000
        
        '''

        print(fee)

    def Feesmd(self):
        while(True):

            fee='''\n ******** Mobile App Development Course Fees Details ********
        
        * Mobile App Development fees   :      6000
        * With Certificates             :     +1000 
        * With GST                      :     +1000
        * Total fees                    :      8000
        
        1. Join Us :
        2. About Us :
        3. Go To Home :
        4. Exit :
        '''

            print(fee)
            f=int(input("Enter a Choice :"))
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()
            elif f==3:
                main2.main1()

        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  
        
    def Feesdbms2(self):
        
        fee='''\n ******** Database Management System Course Fees Details ********
        
        * Database Management System fees   :      6000
        * With Certificates                 :     +1000 
        * With GST                          :     +1000
        * Total fees                        :      8000
        
        '''

        print(fee)

    def Feesdbms(self):
        while(True):

            fee='''\n ******** Database Management System Course Fees Details ********
        
        * Database Management System fees   :      6000
        * With Certificates                 :     +1000 
        * With GST                          :     +1000
        * Total fees                        :      8000
        
        1. Join Us :
        2. About Us :
        3. Go to Home :
        4. Exit :
        '''

            print(fee)
            f=int(input("Enter a Choice :"))
            if f== 1:
                st_database.create_student_form()
            elif f==2:
                student3.us()
            elif f==3:
                main2.main1()
                
        
            elif f==4:
                print("Thanks for choosing select! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  
        
class about:
    def us(self):
        while(True):

            about='''\n\t******************************* About Us **************************** 
            
            The scope of the center is any research involving the programming of computer systems, including the use 
            of programming languages semantics to reason about ... Missing: details| Show results with:
            

                Computer programming is the process of writing instructions that are to be executed by computers. 
                    These written instructions are often called “code,” as they are written in one of several
                         special programming languages which the computer can understand.



                         Phone Number :- 711235468
                         Phone Number :- 441478953

                         E-mail:-center-pro@gmail.com

                    Contact us:-784562361



                1. Go To Home :
                2. Exit :
            '''

            print(about)
            b=int(input("Enter a Choice :"))
            if b==1:
                main2.main1()
                
            elif b==2:
                print("Thanks for choosing Computer Center ! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  




class teacher: 
  
    def login():  
        users = {'Abhishek': '2138433', 'Vishal': 'vishal', 'admin': 'admin'}  
        username = input("Enter your username: ")  
        password = input("Enter your password: ")  
  
        if username in users and users [username] == password:  
            print("Login successful!")  
            teacher.info() 
        else:  
            print("Invalid username or password. Please try again.")  

   

    def info():
        while(True):

            info='''\n ******** Teacher Details ********
        Please choice an option:

        1.Teacher Details :
        2.Teacher Salary Details :
        3.Go To Home:
        4. Exit :
        '''

       
            print(info)
            c=int(input("Enter a Choice :"))
            if c== 1:
                teacher_1.teach_details()

            elif c==2:
                teacher_1.teach_salary()

            elif c==3:
                
                main2.main1()
                
        
            elif c==4:
                print("Thanks for choosing Central library! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!") 

class main():
    def main1(self):

        while(True):
        
            WelcomeMSG='''\n ******** Welcome to Central Library ********
        Please choice an option:
        1. Courses :
        2. Fee Structure :
        3. About us :
        4. Teacher Section :
        5. Exit :
        '''

            print(WelcomeMSG)
            a=int(input("Enter a Choice :"))
            if a== 1:
                student.Courses()
            elif a==2:
                student2.Feeshtml2()    
                student2.Feespy2()    
                student2.Feesjava2()    
                student2.Feesml2()    
                student2.Feescs2()    
                student2.Feesds2()    
                student2.Feesmd2()    
                student2.Feesdbms2()    
            elif a==3:
                student3.us() 
            elif a==4:
                teacher.login() 
            
            elif a==5:
                print("Thanks for choosing Central library! Have a great day ahead ")  
                exit()
            else :
                print("Invaild Choice!")  
   
        
    

if __name__=="__main__":
    main2=main()
    student=Course()
    student2=Fee()
    student3=about()
    teach=teacher()
    
    main2.main1()
                 
       
           
