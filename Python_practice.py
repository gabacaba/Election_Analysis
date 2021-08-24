print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties or "Arapahoe" in counties:
    print (" is in the list.")
else:
    print (" is not in the list.")

county = 0
for county in counties:
    print (county)
for i in range(len(counties)):
    print(counties[i])
counties_dict={"Arapahoe": 422829, "Denver": 463353, "Jefferson":432438}
for county in counties_dict:
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county,"county has", voters,"registered voters")