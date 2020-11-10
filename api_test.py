import requests
from unit_test import myunitest

#Check response of get_url
r = requests.get(myunitest.get_url)
print("*****TEST FOR GET METHOD*****")
print(r.headers)
 
#upd_url
r1 = requests.get(myunitest.upd_url)
print("*****TEST FOR UPDATE METHOD*****")
print(r1.headers)

#pos_url
r2 = requests.get(myunitest.pos_url)
print("*****TEST FOR POST METHOD*****")
print(r2.headers)

#del_url
r3 = requests.get(myunitest.del_url)
print("*****TEST FOR DELETE METHOD*****")
print(r3.headers)
