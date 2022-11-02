import pandas as pd
import urllib.request

####http link
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
##download file and save it as csv
urllib.request.urlretrieve(filename,  "addresses.csv")
##save csv file as dataframe
df = pd.read_csv("addresses.csv", header=None)
# add columns
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
# To select the first row
print(df.loc[0])
# To select the 0th,1st and 2nd row of "First Name" column only
print(df.loc[[0,1,2], "First Name" ])

# To select the 0th,1st and 2nd row of "First Name" column only
print(df.iloc[[0,1,2], 0])
