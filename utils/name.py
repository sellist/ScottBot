import random

"""
TODO:
Merge check_valid_x and add_x into one function using args passed into function at call
"""


class Names:
    """
    This class pertains to the algorithms and methods related to creating a name from a provided list
    """

    def __init__(self, names_file: str, teams_file: str):
        self.names_file = names_file
        self.teams_file = teams_file

    def check_valid_name(self, string: str, limit=20):
        """
        Takes name string as input, checks if name is valid (below max length, not in names.txt)
        :return: Bool
        """

        with open(self.names_file, 'r') as names:
            namelist = names.read().splitlines()

        if string.title() in namelist or len(string) > limit:
            return False

        return True

    def check_valid_team(self, string: str, limit=20):
        """
        Takes name string as input, checks if name is valid (below max length, not in x.txt)
        :return: Bool
        """

        with open(self.teams_file, 'r') as teams:
            teams_list = teams.read().splitlines()

        if string.title() in teams_list or len(string) > limit:
            return False

        return True

    def add_name(self, string: str):

        """
        Takes string as input, splits it at whitespace, converts to Title, checks if names in list, appends to names.txt
        :return: None
        """
        name = string.split()

        # with open(self.names_file, 'r') as names:
        #   namelist = names.read().splitlines()

        if name[0] == '!addname':  # this shouldn't go here but i'm lazy
            del name[0]

        for x in name:
            if self.check_valid_name(x):
                with open(self.names_file, 'a') as names:
                    names.write('\n' + x.title())

    def add_team(self, string: str):
        """
        Takes string as input, splits it at whitespace, converts to Title, checks if names in list, appends to names.txt
        :return: None
        """
        team = string.split()

        # with open(self.teams_file, 'r') as teams:
        # teamlist = teams.read().splitlines()

        if team[0] == '!addname':  # this shouldn't go here but i'm lazy
            del team[0]

        for x in team:
            if self.check_valid_name(x):
                with open(self.teams_file, 'a') as teams:
                    teams.write('\n' + x.title())

    def create_team(self):
        """
        Generates a random name from names list
        :return: String of team name
        """
        with open(self.names_file, 'r') as names:
            names_list = names.read().splitlines()
            names_count = len(names_list)

        with open(self.teams_file, 'r') as teams:
            teams_list = teams.read().splitlines()
            teams_count = len(teams_list)

        first_name = random.randint(0, names_count - 1)
        team_name = random.randint(0, teams_count - 1)

        return "The " + names_list[first_name] + " " + teams_list[team_name]

    def create_name(self):
        """
        Generates a random name from names list
        returns string of name
        """

        with open(self.names_file, 'r') as names:
            names_list = names.read().splitlines()
            line_count = len(names_list)

        firstname = random.randint(0, line_count - 1)
        lastname = random.randint(0, line_count - 1)

        return names_list[firstname] + " " + names_list[lastname]

    def name_count(self):
        with open(self.names_file, 'r') as names:
            names_list = names.read().splitlines()
            return len(names_list)


if __name__ == '__main__':
    test = Names('../names.txt')
    test.add_name("!addname Aborshy Scott")
    print(test.create_name())
