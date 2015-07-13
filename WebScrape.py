from bs4 import BeautifulSoup
import urllib2
import json

# the function that changes the spaces in the scraped link to '%20' to make for a valid url. 
def fix_url(url):
    url_new = ''
    for i in range(len(url)):
        if url_in[i] != ' ':
            url_new = url_new+ url_in[i] 
        else:
            url_new = url_new + '%20'
    return url_new


# In each of the 10 pages (whose link is url depending on i),  there are 10 companies website (link is url_in scraped from url). in the company website,  scrape the table for the company info and save as the kth entry to the dictionary.  
i=0
k=1  
data = {}
urlB = 'http://52.8.18.83'
while i< 10:   
    i = i+1
    url = urlB + "/companies/?page=%d" %(i)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    table = soup.find("table", { "class" : "table table-hover"})
    for link in table.findAll('a'):
        url_in = urlB+link.get('href') # link to each company website
        url_in = fix_url(url_in)
        page_in = urllib2.urlopen(url_in)
        soup_in = BeautifulSoup(page_in.read())
        table_in = soup_in.find_all('td') # find all relevant data from table 
        id = '%d'%(k) # index the dictionary entry 
        data[id] = {}
        for j in range(len(table_in)):
            if j%2 == 0:
                data[id][table_in[j].get_text()] =  table_in[j+1].get_text() # saves the data in table for each company as one dictionary entry
        k=k+1 


# saving the data in a json file called solution
f = open('solution.json', 'w')
json.dump(data, f)
f.close()




