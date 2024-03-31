import csv

#Credits to 1. https://www.youtube.com/watch?v=iKzTUTdXb98 and 
#2. Stackoverflow ideas to solve the problem was gotten from 
        


# A function to display search items if searched with Subject
def showSubj(subb):   
    with open("subj_classmarks1.csv","r") as file:
            reader=csv.reader(file)
            for each in reader:
                each=[string.strip() for string in each] #removing whitespace if it exists before and after each records in the CSV file
                sub=each[0].upper()
                clmk1 = (each[1].upper()).split(',')
                if sub == subb:
                    with open("location_classmarks.csv","r") as file:
                        reader=csv.reader(file)
                        loc = []
                        for each in reader:
                            each=[string.strip() for string in each]
                            location=each[0].upper()
                            clmk = (each[1].upper()).split(',')
                            for x in clmk1:
                                if x in clmk:
                                    if location not in loc:
                                        loc.append(location)
                                        m_loc = ", ".join(loc)
                                        m_clmk1 = ", ".join(clmk1)
                        print("Subject: %s \nClassmarks: %s \nLocation: %s" %(subb, m_clmk1, m_loc))
                            
                            
                            

# A function to display search items if searched with Classmark                            
def showClmk(clm):
    with open("location_classmarks.csv","r") as file:
        reader = csv.reader(file)
        for each in reader:
            each=[string.strip() for string in each] #removing whitespace if it exist before and after each records in the CSV file
            lkt = each[0].upper()
            clmak1 = (each[1].upper()).split(',')
            if clm in clmak1:
                with open("subj_classmarks1.csv","r") as file:
                    reader = csv.reader(file)
                    check = []
                    for each in reader:
                        each=[string.strip() for string in each]
                        sub=each[0].upper()
                        clmak = (each[1].upper()).split(',')
                        for x in clmak1:
                            if x in clmak:
                                if sub not in check:
                                    check.append(sub)
                                    m_check = ", ".join(check)
                    print("Subject: %s \nClassmarks: %s \nLocation: %s" %(m_check, clm, lkt))   
                            
                            
# A function to display search items if searched with Location                            
def showLkt(lkt):         # This prompts user to enter Location.
    with open("location_classmarks.csv","r") as file:       # This reads in the csv file containing locations and classmarks.
        reader=csv.reader(file)
        for each in reader:
            each=[string.strip() for string in each]        #removing whitespace if it exist before and after each records in the CSV file
            lkt1=each[0].upper()
            clmk1=(each[1].upper()).split(',')
            if lkt1==lkt:
                with open("subj_classmarks1.csv","r") as file:  # This reads in csv file containing subjects and classmarks.
                    reader=csv.reader(file)
                    raw = []
                    point = []
                    for each in reader:
                        each=[string.strip() for string in each]
                        sub=each[0].upper()
                        clmk=(each[1].upper()).split(',')
                        for x in clmk:
                            if x in clmk1:
                                if sub not in raw:
                                    raw.append(sub)          # appends subject to an empty list to hold subjects with the same classmark.  
                                    if clmk1 not in point:
                                        mark = ", ".join(clmk1)
                                        point.append(mark)      # appends classmark to an empty list to hold multiple classmarks that has one subject.
                                        m_raw = ", ".join(raw)
                                        m_point = ", ".join(point) 
                    print("Subject: %s \nClassmarks: %s \nLocation: %s" %(m_raw, m_point, lkt))                     
