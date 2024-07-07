class City:
    def __init__(self, name, population):
        self.name = name
        self.population = int(population)

    def print_details(self):
        print(f"City: {self.name}, Population: {self.population}")


class District(City):
    def __init__(self, name, population, num_cities):
        super().__init__(name, population)
        self.num_cities = int(num_cities)

    def print_details(self):
        print(f"District: {self.name}, Population: {self.population}, Number of Cities: {self.num_cities}")


class TamilNadu(District):
    def __init__(self, name, population, num_districts):
        super().__init__(name, population, num_districts)
        self.num_districts = int(num_districts)

    def print_details(self):
        print(f"State: {self.name}, Population: {self.population}, Number of Districts: {self.num_districts}")


def clean_input(value):
    return str(value.strip())


def main():
    city_name, city_population = map(clean_input, input().strip().split(","))
    city = City(city_name, int(city_population))

    district_name, district_population, num_cities = map(clean_input, input().strip().split(","))
    district = District(district_name, int(district_population), int(num_cities))

    state_name, state_population, num_districts = map(clean_input, input().strip().split(","))
    state = TamilNadu(state_name, int(state_population), int(num_districts))

    city.print_details()
    district.print_details()
    state.print_details()


if __name__ == "__main__":
    main()
