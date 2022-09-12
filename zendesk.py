import json
import sys


class ZendeskSearch:
    def __init__(self):
        ''' The init method to initialize the welcome messages'''
        self.welcome_message = "Welcome to Zendesk Search"
        self.quit_message = (
            'Type "quit" to exist at any time, Press "Enter" to continue'
        )
        print(self.welcome_message, "\n", self.quit_message)

    def _check_quit(self, user_inp):
        ''' The check quit method to exist upon user input'''

        if user_inp == "quit":
            sys.exit(0)

    def _input_validate(self, value, lower_bound, upper_bound, prompt=None):
        ''' This method validates the user input across the program '''

        try:
            value = int(value)
            assert lower_bound <= value <= upper_bound
            return value
        except ValueError:
            print('Invalid Choice, Please input an Integer value only!')
            # self._search_options() if prompt == "search_opt" else self._search_zendesk()
        except AssertionError:
            print(
                f"Invalid Choice, Please make sure the Integer value is between the range "
                f"{lower_bound} - {upper_bound}\n")
            # self._search_options() if prompt == "search_opt" else self._search_zendesk()

    def _search_options(self):
        ''' The search option method to either search or view available fields '''

        print("\n\tSelect Search Options:")
        print("\t* Press 1 to search Zendesk")
        print("\t* Press 2 to view a list of searchable fields")
        user_input = input()
        self._check_quit(user_input)
        return self._input_validate(user_input, 1, 2, "search_opt")

    def _search_prompt(self):
        ''' The generic search prompt method to be used '''

        print("\t* Select 1) User or 2) Tickets or 3) Organizations")
        search_opt = self._input_validate(input(), 1, 3, "search_zen")
        search_mapper = {1: "users", 2: "tickets", 3: "organizations"}
        file_name = search_mapper[search_opt] + ".json"
        with open(file_name, "r") as fileObj:
            data = json.load(fileObj, parse_int=str)
        return data, file_name, search_mapper, search_opt

    def _searchable_keys(self):
        ''' The method returns the maximum available keys from the json file '''

        data, _, _, _ = self._search_prompt()
        total_keys = set().union(*(d.keys() for d in data))
        print(total_keys)

    def _search_zendesk(self):
        ''' The method search for the data in the json file '''

        data, file_name, search_mapper, search_opt = self._search_prompt()
        try:
            result = []
            search_term = input("Enter search term: ").strip()
            search_val = input("Enter search value: ").strip()
            if "quit" in {search_term, search_val}:
                self._check_quit("quit")
            # print([elem for elem in data if search_term in elem if elem[search_term] == search_val]) # one-liner
            print(
                f"Searching {search_mapper[search_opt]} for {search_term} with a value of {search_val}"
            )
            for elem in data:
                if search_term in elem:
                    if elem[search_term] == search_val:
                        result.append(elem)
            # print(result) if result else print(f'No results found') # one-liner
            # print(("%s \t %s" % (x, y)) for dct in result for x, y in dct.items()) # one-liner with spacing
            if not result:
                print("No results found")
            for dct in result:
                for x, y in dct.items():
                    print("{:30s} {}".format(x, y))
        except ValueError:
            print("Invalid Choice, Please input an Integer value only!")


if __name__ == "__main__":
    zs = ZendeskSearch()
    user_input = zs._search_options()
    if user_input == 1:
        zs._search_zendesk()
    else:
        zs._searchable_keys()
