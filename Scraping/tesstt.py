from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

#setting up webdriver
Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://portal.iitb.ac.in/asc/Courses")
all_details = []
some_details = []



#selecting the department
for i in range(30,34):
    if i-4<10: 
        k = ("0"+str(i-4))
    else :
        k = str(i-4)    
    i = str(i)
    a1 = "/html/body/table[2]/tbody/tr["
    a2 = "]"
    a =a1+i+a2
    ClickObj=driver.find_element_by_xpath(a)
    branch = str(ClickObj.text)
    
    clic = driver.find_element_by_link_text(branch)
    clic.click()
    
    #entered the course list page
    
    driver.implicitly_wait(2)
    driver.switch_to.frame("sidepanel")
   
    branch_shortcut = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]")
    
    txt = branch_shortcut.text
    
    b_short = txt.split(" ")
    
    courses = driver.find_elements_by_partial_link_text(b_short[0])
    number_of_courses =len(courses)
    
    for subj in range(number_of_courses):

        if subj+1<10: 
            l = ("00"+str(subj+1))
        elif subj+1>=10 and subj+1<100 :
            l = str("0"+str(subj+1))  
        else:
            l = str(subj)
        
        if subj < 1:
            driver.switch_to.default_content()
            driver.switch_to.frame("sidepanel")

        
        
        courses = driver.find_elements_by_partial_link_text(b_short[0])
        
        courses[subj].click()
        
        Course_Name =driver.find_element_by_xpath("/html/body/table[1]/tbody/tr/td/font/h3/b/font").text
        text = Course_Name.split(" - ")
        CourseCode = text[0]
        CourseTitle = text[1]
        
        
        Total_Credits =driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td[2]").text
        Type =driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]").text
        Lecture = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[4]/td[2]").text
	    
        Tutorial =driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[5]/td[2]").text
        Practical =driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[6]/td[2]").text
	    
        Selfstudy =driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[7]/td[2]").text
        Half_Semester=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[8]/td[2]").text
        Prerequisite=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[9]/td[2]").text
        Text_Reference=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[10]/td[2]").text
	    
        Description = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[11]/td[2]").text
        Last_Update=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[12]/td[2]").text
        tx = Last_Update.split(" ")
        Last_Update = tx[0]
        Type = Type or None
        Lecture = Lecture or None
        Tutorial = Tutorial or None
        Practical = Practical or None
        Selfstudy = Selfstudy or None
        Half_Semester = Half_Semester or None
        Description = Description or None
        Text_Reference = Text_Reference or None
        Last_Update = Last_Update or None
        Prerequisite = Prerequisite or None
        Department = branch
        

        Structure ={
            "Type":Type,
	        "Lecture":Lecture,
            "Tutorial":Tutorial,
	        "Practical":Practical,
            "Selfstudy":Selfstudy,
            "HalfSemester":Half_Semester,

        }
       
       
        some_info = {
            "id": int(k+l),
        "Department":branch,
        "Code":CourseCode,
        "Title":CourseTitle,
        "TotalCredits":Total_Credits,
        
        "Prerequisite":Prerequisite,
	    "TextReference":Text_Reference,
        "LastUpdate":Last_Update,
        }
        
        course_info = {
        "id": int(k+l),
        "Department":branch,
        "Code":CourseCode,
        "Title":CourseTitle,
        "TotalCredits":Total_Credits,
        "Description":Description,	
        "Prerequisite":Prerequisite,
	    "TextReference":Text_Reference,
        "LastUpdate":Last_Update,
        }
        course_info['Structure']= Structure
        some_info['Structure']= Structure
        all_details.append(course_info)
        some_details.append(some_info)
        
        driver.back()
        
        driver.switch_to.default_content()
        driver.switch_to.frame("sidepanel")
        
    driver.back()

        
       
        
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

path = './'
fileName = 'all_details'


data = all_details


writeToJSONFile('./',fileName,data)


    
    

# /html/body/table[2]/tbody/tr[5]
# /html/body/table[2]/tbody/tr[8]
# /html/body/table[2]/tbody/tr[27]
#/html/body/table[2]/tbody/tr[18]/td/a /html/body/table[2]/tbody/tr[142]
#body > table.fancyTable > tbody > tr:nth-child(17)
# try:
#     main = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.XPATH,"/html/body/table[2]/tbody/tr[10]"))
#     )
#     print(main.text)
# except:
#     driver.quit() 