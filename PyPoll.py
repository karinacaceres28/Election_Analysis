from optparse import Values


print("Hello World")

#creating a list of counties (if statement)
counties = ["Arapahoe" , "Denver", "Jefferson"]
if counties[1] == "Denver":
        print(counties[1])
#output is DENVER

#single (if-else)
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")  
#output is "EL Paso is not in the list of counties" b/c else/false

#membership and logical operators practice using AND and IN
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
#output "Arapahoe or El Paso is not in the list of countries" b/c else/false

#membership and loginal operators practice using IS IN and OR
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
#output "Arapahoe or El Paso is in the list of counties" because if/true

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
#output "Only Arapahoe is in the list of counties" b/c if/true

#practicing iterate thru list and tuples ((3.2.10))
for county in counties:
    print(county)
#it loops thru all the ((3)) counties
#output will first be "Arapahoe", b/c its the first, 2nd is "Denver", b/c its 2nd, 3rd is "Jefferson", b/c 3rd.


#practicing iterate thru a dictionary ((3.2.10))
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#to get the keys of a dictionary
for county in counties_dict:
    print(county)
#same output as before, where Arapahoe is first, etc

#we can also use key() to iterate over a dictionary to keys
for county in counties_dict.keys():
    print(county)
#same output as before, where Araphoe 1st, etc

#we can get values of keys from the two examples listed below
#1
for voters in counties_dict.values():
    print(voters)

#2
for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

#ask about skill drill found on 3.2.10
for county, voters in counties_dict.items():
    print(county, str("county has "), voters, str("registered voters"))

#the use of f-string: is used to help condence our code. ((3.2.11))
#the code below is what the OG code is
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#the one below is an f-string eg ((3.2.11))
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#practicing multi f-sting ((3.2.11))
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#SKILL DRILL ((3.2.11))
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

