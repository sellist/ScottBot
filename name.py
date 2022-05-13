import random


class Names:
    """
    This class pertains to the algorithms and methods related to creating a name from a provided list
    """

    def __init__(self, file: str):
        self.file_name = file

    def check_if_valid(self, string: str, limit=20):
        """
        Takes name string as input, checks if name is valid (below max length, not in names.txt)
        returns boolean if valid or not
        """

        with open(self.file_name, 'r') as names:
            namelist = names.read().splitlines()

        if string.title() in namelist or len(string) > limit:
            return False

        return True

    def add_name(self, string: str):

        """
        Takes string as input, splits it at whitespace, converts to Title, checks if names in list, appends to names.txt
        returns None
        """
        limit = 20  # allowed max length of a name added
        name = string.split()

        with open(self.file_name, 'r') as names:
            namelist = names.read().splitlines()

        if name[0] == '!addname':  # this shouldn't go here but i'm lazy
            del name[0]

        for x in name:
            if self.check_if_valid(x):
                with open(self.file_name, 'a') as names:
                    names.write('\n' + x.title())

    def create_name(self):
        """
        Generates a random name from names list
        returns string of name
        """

        with open(self.file_name, 'r') as names:
            names_list = names.read().splitlines()
            line_count = len(names_list)

        firstname = random.randint(0, line_count - 1)
        lastname = random.randint(0, line_count - 1)

        return names_list[firstname] + " " + names_list[lastname]

    def name_count(self):
        with open(self.file_name, 'r') as names:
            names_list = names.read().splitlines()
            return len(names_list)


if __name__ == '__main__':
    test = Names('names.txt')
    test.add_name("!addname Aborshy Scott")
    print(test.create_name())
