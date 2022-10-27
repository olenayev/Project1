from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#store  string in the variable HTML
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, "html.parser")

#display the HTML in the nested structure
#print(soup.prettify())

#title of the page and the name of the top paid player 
tag_object=soup.title
#print("tag object:",tag_object)

#the most paid player:
tag_object=soup.h3
#print(tag_object)

#child of the tag
tag_child =tag_object.b
print(tag_child)

#parent  of the tag
parent_tag=tag_child.parent
print(parent_tag) ##or tag_object

#sibiling
sibling_1=tag_object.next_sibling
print(sibling_1)
sibling_2=sibling_1.next_sibling
print(sibling_2)

#tag’s attributes 
print (tag_child['id']) # or ag_child.attrs or tag_child.get('id')


###############################################

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

#extract all the tags with tr and its children
table_rows=table_bs.find_all('tr')
print(table_rows)

first_row =table_rows[0]
print(first_row)

#obtain the child
print(first_row.td)

#iterate through the list, each element corresponds to a row in the table:
for i,row in enumerate(table_rows):
    print("row",i,"is",row)

#list, each element corresponds to a cell and is a Tag object,
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

#filter against each tag’s id attribute
print(table_bs.find_all(id="flight"))

# find all the elements that have links to the Florida Wikipedia page
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

########### Downloading And Scraping The Contents Of A Web Page

#Download the contents of the web page
url = "http://www.ibm.com"
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


 #The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

# we can see how many tables were found by checking the length of the tables list
len(tables)

#10 most densly populated countries 
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

#creation of dataframe
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

#appending dataframe
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data