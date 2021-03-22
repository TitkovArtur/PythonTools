# @Author: Artur Titvkov <Artur>
# @Date:   2021-01-27T16:14:53+01:00
# @Last modified by:   Artur
# @Last modified time: 2021-03-22T11:24:57+01:00



import redis
from datetime import datetime
import hashlib
"""
################################################################################
#################################### TASK 1 ####################################
################################################################################
"""
def insertEntries():
	keys = ["Redis", "Riak", "DynamoDB"]
	schema = ["Developer", "Open", "Rank", "Download"]
	rows = [["Salvatore Sanfilippo",	"false",	9,	"https://redis.io/download"],
		   ["Basho Technologies",		"true",		22,	"http://docs.basho.com"],
		   ["Amazon",					"false",	42,	"None"]]
	i = 0
	for k in keys:
		r.rpush("databases", k)
		j = 0
		for col in schema:
			key = "databases:" + k + ":" + col
			if rows[i][j] == "None":
				j = j + 1
				continue
			r.set(key, rows[i][j])
			j = j + 1
		i = i + 1


def getEntry(name, attribute):
	key = "databases:" + name + ":" + attribute
	print(r.get(key))

def hasEntry(name, attribute):
	key = "databases:" + name + ":" + attribute
	b = "true" if (r.get(key) is not None) else "false";
	print(b)


def rankUp(name):
	key = "databases:" + name + ":Rank"
	r.incr(key)







"""
################################################################################
#################################### TASK 2 ####################################
################################################################################
"""
def insertNewUser(name, age):
	id = r.incr("UserCounter", 1)
	dic = {
		"Name" : name,
		"Age"  : age
	}
	key = "Users:" + str(id)
	print(key)
	r.hset( key,  mapping=dic )


def updateLogin(id):
	user = "Users:" + str(id)
	time = str(datetime.now())
	r.hset(user, key = "Time", value=time)

def checkLastLogin(id):
	print(r.hget("Users:" + str(id), "Time"))










"""
################################################################################
#################################### TASK 3 ####################################
################################################################################
"""

def inserDestricts():
	dic ={
	'Altstadt': 18267,
	'Neustadt': 28149,
	'Oberstadt': 21955,
	'Hartenb./Muenchf': 17879,
	'Mombach': 13986,
	'Gonsenheim': 2539,
	'Finthen': 14667,
	'Bretzenheim': 20077,
	'Marienborn': 4488,
	'Lerchenberg': 6355,
	'Drais': 3124,
	'Hechtsheim': 15402,
	'Ebersheim': 5803,
	'Weisenau': 12959,
	'Laubenheim': 93372}

	r.zadd("Mainz", dic)

def getDistrictRank(district):
	print(r.zrank("Mainz", district))

def getInRange(lower, upper):
	print(r.zrangebyscore("Mainz", 100, 10000, withscores=True))






"""
################################################################################
#################################### TASK 4 ####################################
################################################################################
"""

def setPassword(user, pwd):
	pwd_hash =  hashlib.sha256(pwd)
	pwd_hex  = pwd_hash.hexdigest()
	r.set("pwd//" + user, pwd_hex)

def login(user, pwd):
	pwd_hash = hashlib.sha256(pwd)
	pwd_hex  = pwd_hash.hexdigest()

	pwd2 = r.get("pwd//" + user);

	if pwd_hex == pwd2:
		r.set("loggedin//" + user, 1)
		r.expire("loggedin//" + user, 10)
	else:
		print("NO")


def logout(user):
	r.delete("loggedin//" + user)









"""
################################################################################
##################################### MAIN #####################################
################################################################################
"""

host = "3.122.231.43"
groupNumber = 12 #add your group number
password = "wt2021"
r = redis.Redis(host=host, port=6379, db=groupNumber, password=password)





"""
	TASK 1
"""
#getEntry("DynamoDB", "Download")
#hasEntry("DynamoDB", "Download")
#rankUp("Redis")
#getEntry("Redis", "Rank")


"""
	TASK 2
"""
#r.set("UserCounter", 0)
#insertNewUser("Lisa", 24)
#insertNewUser("Elli", 26)
#updateLogin(1)
#checkLastLogin(1)


"""
	TASK 3
"""
#inserDestricts()
#getDistrictRank("Drais")
#getDistrictRank("Neustadt")
#getInRange(10,10);



"""
	TASK 4
"""

#setPassword("Lisa", "1234")
login("Lisa", "1234")
#logout("Lisa")


















































#
