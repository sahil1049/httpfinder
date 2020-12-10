
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

#list containing domains
file1 = open('read.txt', 'r') 

Lines = file1.readlines()

for i in Lines:


 
 req = Request("https://"+i)
 print("Status of "+i)
 try:
    response = urlopen(req)
 except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
 except URLError as e:
    file2=open('write.txt','a')
    print('We failed to reach a server.')
    file2.write("http://"+i)  
    file2.close()
    print('Reason: ', e.reason)
    
 else:
    
    print ('Website is working fine')
file1.close()
