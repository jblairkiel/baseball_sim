import random as rand
class Player():

    def __init__(self, first_name, last_name, position, jersey_number):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        if jersey_number == None:
            self.jersey_number = rand.randrange(0,99)
        else:
            self.jersey_number = jersey_number
        self.stats = {
            'at_bats': 0,
            'hits': 0,
            'home_runs': 0,
            'runs_batted_in': 0,
            'doubles': 0,
            'triples': 0,
            'strikeouts': 0,
            'walks': 0,
            'stolen_bases': 0,
            'caught_stealing': 0,
            'batting_average': 0.0,
            'on_base_percentage': 0.0,
            'slugging_percentage': 0.0,
        }

    def __str__(self):
        return f'{self.first_name} {self.last_name} (#{self.jersey_number})'

    def get_batting_average(self):
        if self.stats['at_bats'] == 0:
            return 0.0
        return self.stats['hits'] / self.stats['at_bats']

    def get_on_base_percentage(self):
        if self.stats['at_bats'] == 0:
            return 0.0
        return (self.stats['hits'] + self.stats['walks']) / self.stats['at_bats']

    def get_slugging_percentage(self):
        if self.stats['at_bats'] == 0:
            return 0.0
        total_bases = self.stats['hits'] + (2 * self.stats['doubles']) + (3 * self.stats['triples']) + (4 * self.stats['home_runs'])
        return total_bases / self.stats['at_bats']

    def update_stats(self, event):
        if event == 'single':
            self.stats['at_bats'] += 1
            self.stats['hits'] += 1
            self.stats['batting_average'] = self.get_batting_average()
        elif event == 'double':
            self.stats['at_bats'] += 1
            self.stats['hits'] += 1
            self.stats['doubles'] += 1
            self.stats['batting_average'] = self.get_batting_average()
            self.stats['slugging_percentage'] = self.get_slugging_percentage()
        elif event == 'triple':
            self.stats['at_bats'] += 1
            self.stats['hits'] += 1
            self.stats['triples'] += 1
            self.stats['batting_average'] = self.get_batting_average()
            self.stats['slugging_percentage'] = self.get_slugging_percentage()
        elif event == 'home_run':
            self.stats['at_bats'] += 1
            self.stats['hits'] += 1
            self.stats['home_runs'] += 1
            self.stats['runs_batted_in'] += 1
            self.stats['batting_average'] = self.get_batting_average()
            self.stats['slugging_percentage'] = self.get_slugging_percentage()
        elif event == 'walk':
            self.stats['at_bats'] += 1
            self.stats['walks'] += 1
            self.stats['on_base_percentage'] = self.get_on_base_percentage()
        elif event == 'strikeout':
            self.stats['at_bats'] += 1
            self.stats['strikeouts'] += 1
        elif event == 'stolen_base':
            self.stats['stolen_bases'] += 1
        elif event == 'caught_stealing':
            self.stats['caught_stealing'] += 1
        else:
            raise ValueError(f'Invalid event: {event}')