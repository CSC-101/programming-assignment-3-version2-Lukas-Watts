from unittest import expectedFailure

import Hw3
import data
import build_data
import unittest


# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total_1(self):
        list_of_county=build_data.get_data()
        result=Hw3.population_total(list_of_county)
        expected=318857056
        self.assertEqual(result,expected)

    def test_population_total_2(self):
        list_of_county=build_data.get_data()
        result=Hw3.population_total(list_of_county)
        expected=7000018857056
        self.assertNotEqual(result,expected)

    # Part 2
    # test filter_by_state
    def test_filter_by_state_1(self):
        list_of_county = build_data.get_data()
        state="CA"
        result=Hw3.filter_by_state(list_of_county,state)
        expected=['Alameda County', 'Alpine County', 'Amador County', 'Butte County', 'Calaveras County', 'Colusa County', 'Contra Costa County', 'Del Norte County', 'El Dorado County', 'Fresno County', 'Glenn County', 'Humboldt County', 'Imperial County', 'Inyo County', 'Kern County', 'Kings County', 'Lake County', 'Lassen County', 'Los Angeles County', 'Madera County', 'Marin County', 'Mariposa County', 'Mendocino County', 'Merced County', 'Modoc County', 'Mono County', 'Monterey County', 'Napa County', 'Nevada County', 'Orange County', 'Placer County', 'Plumas County', 'Riverside County', 'Sacramento County', 'San Benito County', 'San Bernardino County', 'San Diego County', 'San Francisco County', 'San Joaquin County', 'San Luis Obispo County', 'San Mateo County', 'Santa Barbara County', 'Santa Clara County', 'Santa Cruz County', 'Shasta County', 'Sierra County', 'Siskiyou County', 'Solano County', 'Sonoma County', 'Stanislaus County', 'Sutter County', 'Tehama County', 'Trinity County', 'Tulare County', 'Tuolumne County', 'Ventura County', 'Yolo County', 'Yuba County']
        self.assertEqual(result,expected)

    def test_filter_by_state_2(self):
        list_of_county = build_data.get_data()
        state = "HI"
        result = Hw3.filter_by_state(list_of_county, state)
        expected=['Hawaii County', 'Honolulu County', 'Kalawao County', 'Kauai County', 'Maui County']
        self.assertEqual(result, expected)

    #Part3
    #test population_by_education
    def test_population_by_education_1(self):
        education_key="Bachelor's Degree or Higher"
        list_of_county=Hw3.get_data()
        result=Hw3.population_by_education(list_of_county,education_key)
        expected=92216021.02199993
        self.assertEqual(result,expected)

    def test_population_by_education_2(self):
        education_key='High School or Higher'
        list_of_county=Hw3.get_data()
        result=Hw3.population_by_education(list_of_county,education_key)
        expected=274026015.6330008
        self.assertEqual(result,expected)
    #test_population_by_ethnicity
    def test_population_by_ethnicity_1(self):
        ethnicity_key='Native Hawaiian and Other Pacific Islander Alone'
        list_of_county=Hw3.get_data()
        result=Hw3.population_by_ethnicity(list_of_county,ethnicity_key)
        expected=738301.5059999998
        self.assertEqual(result,expected)

    def test_population_by_ethnicity_2(self):
        ethnicity_key='Asian Alone'
        list_of_county=Hw3.get_data()
        result=Hw3.population_by_ethnicity(list_of_county,ethnicity_key)
        expected=17346856.558999952
        self.assertEqual(result,expected)
    #test_population_by_poverty
    def test_population_in_poverty_1(self):
        list_of_county=Hw3.get_data()
        result=Hw3.population_below_poverty_level(list_of_county)
        expected=48996488.47399998
        self.assertEqual(expected,result)
    def test_population_in_poverty_2(self):
        list_of_county=Hw3.get_data()
        result=Hw3.population_below_poverty_level(list_of_county)
        expected=21348996488.47399998
        self.assertNotEqual(expected,result)
    # Part 4
    # test percent_by_education
    def test_percent_by_education_1(self):
        list_of_county=Hw3.get_data()
        education_key="Bachelor's Degree or Higher"
        result=Hw3.percent_by_education(list_of_county,education_key)
        expected=28.920803001455276
        self.assertEqual(expected,result)

    def test_percent_by_education_2(self):
        list_of_county=Hw3.get_data()
        education_key='High School or Higher'
        result=Hw3.percent_by_education(list_of_county,education_key)
        expected=85.94008207646526
        self.assertEqual(expected,result)


    # test percent_by_ethnicity
    def test_percent_by_ethnicity_1(self):
        list_of_county=Hw3.get_data()
        ethnicity_key='Asian Alone'
        result=Hw3.percent_by_ethnicity(list_of_county,ethnicity_key)
        expected=5.4403238794878535
        self.assertEqual(expected,result)

    def test_percent_by_ethnicity_2(self):
        list_of_county=Hw3.get_data()
        ethnicity_key='Native Hawaiian and Other Pacific Islander Alone'
        result=Hw3.percent_by_ethnicity(list_of_county,ethnicity_key)
        expected=0.2315462343100853
        self.assertEqual(expected,result)
    # test percent_below_poverty_level
    def test_percent_below_poverty_1(self):
        list_of_county=Hw3.get_data()
        result=Hw3.percent_below_poverty_level(list_of_county)
        expected=15.366286413307403
        self.assertEqual(expected,result)

    def test_percent_below_poverty_2(self):
        list_of_county=Hw3.get_data()
        result=Hw3.percent_below_poverty_level(list_of_county)
        expected=151.366286413307403
        self.assertNotEqual(expected,result)
    # Part 5
    # test education_greater_than
    def test_education_greater_than_1(self):
        list_of_county = Hw3.get_data()
        education_key = "Bachelor's Degree or Higher"
        Value_key = 74.1
        result = Hw3.education_greater_than(list_of_county, education_key, Value_key)
        expected = ['Falls Church city']
        self.assertEqual(result, expected)

    def test_education_greater_than_2(self):
        list_of_county = Hw3.get_data()
        education_key = "High School or Higher"
        Value_key = 98.1
        result = Hw3.education_greater_than(list_of_county, education_key, Value_key)
        expected = ['Ouray County', 'Blaine County']
        self.assertEqual(result, expected)
    # test education_less_than
    def test_education_less_than_1(self):
        list_of_county = Hw3.get_data()
        education_key = "Bachelor's Degree or Higher"
        Value_key = 3.9
        result = Hw3.education_less_than(list_of_county, education_key, Value_key)
        expected = ['Quitman County']

    def test_education_less_than_2(self):
        list_of_county = Hw3.get_data()
        education_key = "High School or Higher"
        Value_key = 55.1
        result = Hw3.education_less_than(list_of_county, education_key, Value_key)
        expected = ['Hudspeth County', 'La Salle County', 'Presidio County', 'Starr County', 'Zapata County']
    # test ethnicity_greater_than
    def test_ethnicity_greater_than_1(self):
        list_of_county=Hw3.get_data()
        ethnicity_key='Hispanic or Latino'
        Value_key=90
        result=Hw3.ethnicity_greater_than(list_of_county,ethnicity_key,Value_key)
        expected=['Hidalgo County', 'Jim Hogg County', 'Maverick County', 'Starr County', 'Webb County', 'Zapata County', 'Zavala County']
        self.assertEqual(result,expected)
    def test_ethnicity_greater_than_2(self):
        list_of_county=Hw3.get_data()
        ethnicity_key='Native Hawaiian and Other Pacific Islander Alone'
        Value_key=20.1
        result=Hw3.ethnicity_greater_than(list_of_county,ethnicity_key,Value_key)
        expected=['Kalawao County']
        self.assertEqual(result,expected)
    # test ethnicity_less_than
    def test_ethnicity_less_than_1(self):
        list_of_county=Hw3.get_data()
        ethnicity_key='Hispanic or Latino'
        Value_key=.5
        result=Hw3.ethnicity_less_than(list_of_county,ethnicity_key,Value_key)
        expected=['Leslie County', 'Blaine County', 'Hancock County', 'Bedford city']
        self.assertEqual(result,expected)
    def test_ethnicity_less_than_2(self):
        list_of_county=Hw3.get_data()
        ethnicity_key='Asian Alone'
        Value_key=.01
        result=Hw3.ethnicity_less_than(list_of_county,ethnicity_key,Value_key)
        expected=['Kiowa County', 'Keweenaw County', 'Jefferson County', 'Petroleum County', 'Banner County', 'Blaine County', 'Garden County', 'Hooker County', 'Loup County', 'McPherson County', 'Slope County', 'Kent County', 'King County', 'Loving County', 'Bedford city']
        self.assertEqual(result,expected)
    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than_1(self):
        list_of_county=Hw3.get_data()
        value_key=50
        result=Hw3.below_poverty_level_greater_than(list_of_county,value_key)
        expected=['Shannon County']
        self.assertEqual(expected,result)

    def test_below_poverty_level_greater_than_2(self):
        list_of_county=Hw3.get_data()
        value_key=32.139312
        result=Hw3.below_poverty_level_greater_than(list_of_county,value_key)
        expected=['Conecuh County', 'Dallas County', 'Greene County', 'Sumter County', 'Wilcox County', 'Apache County', 'Chicot County', 'Phillips County', 'Atkinson County', 'Ben Hill County', 'Burke County', 'Calhoun County', 'Clarke County', 'Clay County', 'Sumter County', 'Madison County', 'Bell County', 'Breathitt County', 'Clay County', 'Jackson County', 'Knox County', 'Lee County', 'Martin County', 'Owsley County', 'Wolfe County', 'East Carroll Parish', 'Madison Parish', 'Tensas Parish', 'Bolivar County', 'Claiborne County', 'Coahoma County', 'Holmes County', 'Humphreys County', 'Issaquena County', 'Jefferson County', 'Kemper County', 'Leflore County', 'Noxubee County', 'Oktibbeha County', 'Quitman County', 'Sunflower County', 'Washington County', 'Yazoo County', 'Glacier County', 'McKinley County', 'Scotland County', 'Benson County', 'Rolette County', 'Sioux County', 'Allendale County', 'Bennett County', 'Buffalo County', 'Corson County', 'Dewey County', 'Mellette County', 'Shannon County', 'Todd County', 'Ziebach County', 'Brooks County', 'Cameron County', 'Hidalgo County', 'Hudspeth County', 'Kenedy County', 'Starr County', 'Willacy County', 'Zapata County', 'Zavala County', 'Harrisonburg city', 'Radford city', 'Whitman County', 'McDowell County']
        self.assertEqual(expected,result)
    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than_1(self):
        list_of_county=Hw3.get_data()
        value_key=1.1
        result=Hw3.below_poverty_level_less_than(list_of_county,value_key)
        expected=['Borden County']
        self.assertEqual(expected,result)

    def test_below_poverty_level_less_than_2(self):
        list_of_county=Hw3.get_data()
        value_key=6.261
        result=Hw3.below_poverty_level_less_than(list_of_county,value_key)
        expected=['Juneau City and Borough', 'Skagway Municipality', 'Yakutat City and Borough', 'Douglas County', 'Hinsdale County', 'Ouray County', 'Kendall County', 'Monroe County', 'Piatt County', 'Hamilton County', 'Hendricks County', 'Greeley County', 'Hodgeman County', 'Stanton County', 'Calvert County', 'Carroll County', 'Frederick County', 'Howard County', 'Livingston County', 'Carver County', 'Scott County', 'Washington County', 'St. Charles County', 'Fallon County', 'Hayes County', 'Kearney County', 'Perkins County', 'Pierce County', 'Rockingham County', 'Burlington County', 'Hunterdon County', 'Morris County', 'Somerset County', 'Sussex County', 'Los Alamos County', 'Nassau County', 'Putnam County', 'Camden County', 'Cavalier County', 'Steele County', 'Delaware County', 'Bucks County', 'Montgomery County', 'Deuel County', 'Lincoln County', 'Sully County', 'Union County', 'Williamson County', 'Borden County', 'Glasscock County', 'King County', 'Roberts County', 'Rockwall County', 'Morgan County', 'Fairfax County', 'Fauquier County', 'Goochland County', 'Hanover County', 'Loudoun County', 'New Kent County', 'Powhatan County', 'Stafford County', 'York County', 'Falls Church city', 'Poquoson city', 'Ozaukee County', 'Waukesha County', 'Sublette County']
        self.assertEqual(expected,result)



if __name__ == '__main__':
    unittest.main()
