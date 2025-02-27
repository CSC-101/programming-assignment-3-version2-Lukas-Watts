import data
from build_data import get_data
from data import CountyDemographics


#Part 1
def population_total(list_of_county:list[CountyDemographics])->int:
    population_total=0
    for county in list_of_county:
        population_total+=county.population.get("2014 Population")
    return population_total
print(population_total(get_data()))
#Counts 2014 population of all counties in the US. Input is a list containg data for all counties in the US, Output is a integer

#Part 2
def filter_by_state(list_of_countys:list[CountyDemographics], state: str)->list[CountyDemographics]:
    state_county_list=[]
    for county in list_of_countys:
        if county.state==state:
            state_county_list.append(county.county)
    return state_county_list
print(filter_by_state(get_data(),"HI"))
#Filters information about the counties by the state it is in, input is a list containing data for all counties in the US and a string to represent a states abreviation. Output is that filtered list
#Part 3
#Part A
def population_by_education(list_of_county:list[CountyDemographics],education_key:str)->float:
    educated_americans=0
    for county in list_of_county:
        educated_americans+=(county.population.get('2014 Population')*(county.education.get(education_key)/100))
    return educated_americans
print(population_by_education(get_data(),'High School or Higher'))
# Returns the total population of the US that completed what the education key specfies, input is a list containing data for all counties in the US and a education key(str) which represents the education level which was completed,
#Output is a integer value filtered according to the education key
#Part B
def population_by_ethnicity(list_of_county:list[CountyDemographics],ethnicity_key:str)->float:
    total_ethnicity_americans=0
    for county in list_of_county:
        total_ethnicity_americans+=(county.population.get('2014 Population')*(county.ethnicities.get(ethnicity_key)/100))
    return total_ethnicity_americans
print(population_by_ethnicity(get_data(),'Native Hawaiian and Other Pacific Islander Alone'))
#Returns total population of US which belongs to the selected ethnicity group. input is a list containing data for all counties in the US and str to select ethnic group
#Output is a float which represents how many americans belong to the selected ethnic group
#Part C
def population_below_poverty_level(list_of_county:list[CountyDemographics])->float:
    total_americans_under_poverty_level=0
    for county in list_of_county:
        total_americans_under_poverty_level+=(county.population.get('2014 Population')*county.income.get('Persons Below Poverty Level'))/100
    return total_americans_under_poverty_level
print(population_below_poverty_level(get_data()))
#Shows the population of the US which is below the poverty level. input is a list containing data for all counties in the US.
#Output is a value representing how many americans live poverty in the US
#Part 4
#PART A
def percent_by_education(list_of_county:list[CountyDemographics],education_key:str)->float:
    educated_americans=0
    us_population=0
    for county in list_of_county:
        us_population+=county.population.get('2014 Population')
        educated_americans+=(county.population.get('2014 Population')*county.education.get(education_key))/100
    percent_educated_us=(educated_americans/us_population)*100
    return percent_educated_us
print(percent_by_education(get_data(),"Bachelor's Degree or Higher"))
#Shows what perecent of americans have completed the selected educational level. input is a list containing data for all counties in the US and a str to represent completed education lvl
#Output is a float(percentage) which represents how many americans have completed the selected educational level
# Part B
def percent_by_ethnicity(list_of_county:list[CountyDemographics],ethnicity_key:str)->float:
    total_ethnicity_americans=0
    us_population = 0
    for county in list_of_county:
        us_population += county.population.get('2014 Population')
        total_ethnicity_americans+=(county.population.get('2014 Population')*county.ethnicities.get(ethnicity_key))/100
    percent_given_ethnicity=(total_ethnicity_americans/us_population)*100
    return percent_given_ethnicity
print(percent_by_ethnicity(get_data(),'Two or More Races'))
# Returns a percent of how many americans belong to the selected ethnic group. input is a list containing data for all counties in the US and a str to select ethnic group
#Output is a percent representing how many americans belong to that ethnic group
# Part C
def percent_below_poverty_level(list_of_county:list[CountyDemographics])->float:
    total_americans_under_poverty_level=0
    us_population = 0
    for county in list_of_county:
        us_population += county.population.get('2014 Population')
        total_americans_under_poverty_level+=(county.population.get('2014 Population')*county.income.get('Persons Below Poverty Level'))/100
    percent_by_poverty_level=(total_americans_under_poverty_level/us_population)*100
    return percent_by_poverty_level
print(percent_below_poverty_level(get_data()))
#Returns a percent of how many americans live in poverty. input is a list containing data for all counties in the US
#Output is a percent showing how many americans live in poverty
#Part 5
#Part A
def education_greater_than(list_of_county:list[CountyDemographics], education_key:str, education_limit:float) -> list[CountyDemographics]:
    counties_over_education_level=[]
    for county in list_of_county:
        if county.education.get(education_key) > education_limit:
            counties_over_education_level.append(county.county)
    return counties_over_education_level
print(education_greater_than(get_data(),"High School or Higher",98.1))
#Shows counties whose percentage population which completed the selected education lvl is higher than a user selected educational percentage. input is a list containing data for all counties in the US
# and also str to choose education lvl and a float representing the percentage you are comparing to. Output is a list of counties which meet qualifcations
def education_less_than(list_of_county:list[CountyDemographics], education_key:str, education_limit:float) -> list[CountyDemographics]:
    counties_under_education_level=[]
    for county in list_of_county:
        if county.education.get(education_key) < education_limit:
            counties_under_education_level.append(county.county)
    return counties_under_education_level
print(education_less_than(get_data(),"High School or Higher",55.1))
#Shows counties whose percentage population which completed the selected education lvl is lower than a user selected educational percentage. input is a list containing data for all counties in the US
# and also str to choose education lvl and a float representing the percentage you are comparing to. Output is a list of counties which meet qualifcations
#Part B
def ethnicity_greater_than(list_of_county:list[CountyDemographics], ethnicity_key:str, ethnicity_value:float) -> list[CountyDemographics]:
    counties_over_ethnicity_value = []
    for county in list_of_county:
        if county.ethnicities.get(ethnicity_key)>ethnicity_value:
            counties_over_ethnicity_value.append(county.county)
    return counties_over_ethnicity_value
print(ethnicity_greater_than(get_data(),'Native Hawaiian and Other Pacific Islander Alone',20))
#Shows counties whose percentage population is the selected ethnic group is higher than a user selected percentage. input is a list containing data for all counties in the US
# and also str to choose ethnic group and a float representing the percentage you are comparing to. Output is a list of counties which meet qualifcations
def ethnicity_less_than(list_of_county:list[CountyDemographics], ethnicity_key:str, ethnicity_value:float) -> list[CountyDemographics]:
    counties_under_ethnicity_value = []
    for county in list_of_county:
        if county.ethnicities.get(ethnicity_key)<ethnicity_value:
            counties_under_ethnicity_value.append(county.county)
    return counties_under_ethnicity_value
print(ethnicity_less_than(get_data(),'Asian Alone',.01))
#Shows counties whose percentage population is the selected ethnic group is lower than a user selected percentage. input is a list containing data for all counties in the US
# and also str to choose ethnic group and a float representing the percentage you are comparing to. Output is a list of counties which meet qualifcations
#Part C
def below_poverty_level_greater_than(list_of_county:list[CountyDemographics], poverty_level:float) -> list[CountyDemographics]:
    counties_over_poverty_level=[]
    for county in list_of_county:
        if county.income.get('Persons Below Poverty Level')>poverty_level:
            counties_over_poverty_level.append(county.county)
    return counties_over_poverty_level
print(below_poverty_level_greater_than(get_data(),32.139312))
#Shows counties whose percentage population in poverty is higher than a user selected poverty level. Helps Find poor counties. input is a list containing data for all counties in the US
# and a float representing the poverty level you are comparing to. Output is a list of counties which meet qualifcations
def below_poverty_level_less_than(list_of_county:list[CountyDemographics], poverty_level:float) -> list[CountyDemographics]:
    counties_under_poverty_level=[]
    for county in list_of_county:
        if county.income.get('Persons Below Poverty Level')<poverty_level:
            counties_under_poverty_level.append(county.county)
    return counties_under_poverty_level
print(below_poverty_level_less_than(get_data(),6.261))
#Shows counties whose percentage population in poverty is lower than a user selected poverty level.Helps find rich counties!! input is a list containing data for all counties in the US
# and a float representing the poverty level you are comparing to. Output is a list of counties which meet qualifcations


