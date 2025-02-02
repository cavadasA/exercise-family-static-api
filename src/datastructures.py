
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "first_name": "John Jackson",
                "id": 1,
                "age": "33",
                "lucky_numbers": [7, 13, 22]
            },
            {
                "first_name": "Jane Jackson",
                "id": 2,
                "age": "35",
                "lucky_numbers": [10, 14, 3]
            },
            {
                "first_name": "Jimmy Jackson",
                "id": 3,
                "age": "5",
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" in member:
            self._members.append(member)
        else:
            id = self._generateId()
            member["id"] = str(id)
            self._members.append(member)
        return

    def delete_member(self, id):
        newList = []
        for member in self._members:
            if (member["id"] != str(id)):
                newList.append(member)
        if (newList == self._members):
            return False
        else:
            self._members = newList
            return True

    def get_member(self, id):
        for member in self._members:
            if (member["id"] == str(id)):
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
