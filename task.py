#Task 1: fetch name
#Task 2: fetch names whose department is IT
#Task 3: fetch names and age when department is ECE
#Task 4: top performer of every branch
#Task 5: avg performance for every Branch
#Task 6: low performer of every branch
#Task 7: count of Job Selection
#Task 8: Highest/average/lowest of each department
#Task 9: category-wise data on the basis of department find count/sum of annual package/average
#Task 10: on the basis of performance implement annual package for 
# (i) above 5-15 Lakh
# (ii) above 3 and below 5-10 Lakh
# (iii) below 3-5 Lakh
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name' : ['Aarushi','AARAV KARN','AARYAN NITIN ZADE','ADITYA SARIN','AFIF KHAN','AISHWARYA PARASHAR','AJAY KUMAR GIRI','AKRITI SINGH','AKSHAT GARG','ANIKET SANGAL','ANISH KUMAR',
            'ANJALI VERMA','ANSH SRIVASTAVA','ANSHUL ASWAL','BASANT MALIK','BHARAT KUMAR','DARSH JAISWAL' ,'DEVANSH SHUKLA','DIKSHA JHA','DIVYANSH TRIPATHI','DROMIL','EKLAVYA GUPTA'
            ,'GAURAV SINGH','HRITTIK RAUSHAN','KANISHQ ATTREYA','LAVANYA SRIVASTAVA','MUKESH GUPTA','NIDHI VERMA','NITISH KUMAR YADAV','PAKHI DUBEY','PAVITRA VERMA'
            ,'POORVI PRADHAN','PRATIK ABHISHEK','PRIYANSHU SHARMA','RAJ SINGH','RIDDHI BOSE,SWYAM', 'YASHI GUPTA'],
    'age' : [18,19,19,18,19,19,20,18,19,19,18,19,19,20,
             19,19,20,18,19,19,18,19,19,20,18,19,19,18,19,
             19,20,18,19,19,18,19,19],
    'performance' : ['HIGH','LOW','MEDIUM','HIGH','HIGH','MEDIUM','LOW',
                     'HIGH','LOW','MEDIUM','HIGH','HIGH','MEDIUM','LOW',
                     'HIGH','LOW','MEDIUM','HIGH','HIGH','MEDIUM','LOW',
                     'HIGH','LOW','MEDIUM','HIGH','HIGH','MEDIUM','LOW',
                     'HIGH','LOW','MEDIUM','HIGH','HIGH','HIGH','MEDIUM',
                     'LOW','HIGH'],
    'department' :  ['ECE','ME','IT','CSE','ECE','ME','IT','CSE',
                      'ECE','ME','IT','CSE','ECE','ME','IT','CSE',
                      'ECE','ME','IT','CSE','ECE','ME','IT','CSE',
                      'ECE','ME','IT','CSE','ECE','ME','IT','CSE',
                      'ECE','ME','IT','CSE','ECE'],
    'job_selection' : ['Selected','Not-Selected','Selected','Selected','Selected','Not-Selected','Selected','Selected',
                       'Selected','Not-Selected','Selected','Selected','Selected','Not-Selected','Selected','Selected',
                       'Selected','Not-Selected','Selected','Selected','Selected','Not-Selected','Selected','Selected',
                       'Selected','Not-Selected','Selected','Selected','Selected','Not-Selected','Selected','Selected',
                       'Selected','Not-Selected','Selected','Selected','Selected',],
    'skills' : ['Embedded','AutoCAD','C++','Java','IoT','Embedded','Thermodynamics','C++','Python','VLSI',
                'Embedded','Thermodynamics','C++','Python','IoT','VLSI','AutoCAD','C++','Java','IoT',
                'Iot','AutoCAD','Python','Java','IoT','Embedded','Thermodynamics','C++','Python','VLSI',
                'Iot','Thermodynamics','Python','Java','VLSI','Embedded','AutoCAD'],
    'annual_package' : ['1200000','1000000','200000','400000','1700000','1500000','1200000','1000000',
                        '1200000','1000000','200000','400000','1700000','1500000','1200000','1000000',
                        '1200000','1000000','200000','400000','1700000','1500000','1200000','1000000',
                        '1200000','1000000','200000','400000','1700000','1500000','1200000','1000000',
                        '1200000','1000000','200000','400000','1700000']
})

print("\n" + "="*10 + ' Task 1: Fetch Name ' + "="*10 + "\n")
names = df['name'].tolist()
print('\n',names)

print("\n" + "="*10 + ' Task 2: Fetch names whose department is IT ' + "="*10 + "\n")
it_names = df[df['department'] == 'IT']['name'].tolist()
print('\n',it_names)

print("\n" + "="*10 + ' Task 3: Fetch names and age when department is ECE ' + "="*10 + "\n")
ece_students = df[df['department'] == 'ECE'][['name', 'age']]
print('\n',ece_students)

print("\n" + "="*10 + ' Task 4: Top performer of every branch ' + "="*10 + "\n")
top_performers = df[df['performance'] == 'HIGH'][['department', 'name']]
print('\n',top_performers)

print("\n" + "="*10 + ' Task 5: Avg performance for every Branch ' + "="*10 + "\n")
performance = df.groupby(['department', 'performance']).size().unstack(fill_value=0)
print('\n',performance)

print("\n" + "="*10 + ' Task 6: Low performer of every branch ' + "="*10 + "\n")
low_performers = df[df['performance'] == 'LOW'][['department', 'name']]
print('\n',low_performers)

print("\n" + "="*10 + ' Task 7: Count of Job Selection ' + "="*10 + "\n")
job_count = df['job_selection'].value_counts()
print('\n',job_count)

print("\n" + "="*10 + ' Task 8: Highest/average/lowest of each department ' + "="*10 + "\n")
df['annual_package'] = df['annual_package'].astype(int)
pkg_stats = df.groupby('department')['annual_package'].agg(['max', 'mean', 'min']).round(2)
print('\n',pkg_stats)

print("\n" + "="*10 + ' Task 9: Category-wise data on the basis of department find count/sum of annual package/average ' + "="*10 + "\n")
dept_summary = df.groupby('department')['annual_package'].agg(
    Count='count',
    Sum='sum',
    Average='mean'
).round(2)
print(dept_summary)
print('\n',dept_summary)

print("\n" + "="*10 + ' Task 10 ' + "="*10 + "\n")
def categorize_package(performance):
    if performance == 'HIGH':
        return 'Above 5-15 Lakh'
    elif performance == 'MEDIUM':
        return 'Above 3 and below 5-10 Lakh'
    elif performance == 'LOW':
        return 'Below 3-5 Lakh'
    else:
        return 'Unknown'

df['annual_performance'] = df['performance'].apply(categorize_package)
print('\n',df[['name', 'performance', 'annual_performance']].to_string())

plt.figure(figsize=(9,5))
plt.bar(df['annual_package'],df['department'],color=['red','blue','orange'])
plt.title('Pkg Status vs Department')
plt.xlabel('Pkg Status')
plt.ylabel('Department')
plt.show()