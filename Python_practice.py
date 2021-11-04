counties = ["Arapahoe", "Denver", "Jefferson"]

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for county in range(len(voting_data)):
    print(voting_data[county])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

