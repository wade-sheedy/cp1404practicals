""" Do From Scratch Exercise"""

from Prac_07.Guitars import Guitar


def main():
    """
    Tests the functionality of the guitar class
    """
    gibson = Guitar()
    gibson.add_name('Gibson L-5 CES')
    gibson.add_year(1922)
    another = Guitar()
    another.add_name('Another Guitar')
    another.add_year(2012)
    test_subjects = [gibson, another]
    expected_result = [95, 5]
    expected_result_2 = [True, False]
    for i in range(len(test_subjects)):
        age_result = test_subjects[i].get_age()
        print('{self.name}'.format(self=test_subjects[i]), ' get_age() - Expected {}. Got {}'
              .format(expected_result[i], age_result))
    print()
    for n in range(len(test_subjects)):
        vintage_result = test_subjects[n].is_vintage(test_subjects[n].get_age())
        print('{self.name}'.format(self=test_subjects[n]), ' is_vintage() - Expected {}. Got {}'
              .format(expected_result_2[n], vintage_result))


main()