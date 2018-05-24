


from taxi import Taxi

def main():


    taxi = Taxi('prius_1', 100 )
    taxi.drive(40)

    print('Expect that Prius 1 has 60 liters of fuel, and fair costs $49.20 - '
          'Got, {self.name}, has {self.fuel} LTRS of fuel'.format(self = taxi), ',Fare Costs ${:.2f}'.format(taxi.get_fare()))


main()