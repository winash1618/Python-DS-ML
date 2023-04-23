"""
The goals of this exercise is to discover new built-in functions and deepen your class
manipulation and to be aware of possibility to modify instanced objects.
In this exercise you learn how to modify or add attributes to an object.
"""
# in the_bank.py
class Account(object):
    """
    Object to deal with a person's account
    """
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        """
        called automatically when an instance of Account is created
        """
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        """
        For transfering money to your account
        """
        self.value += amount

# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """
        Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if not isinstance(new_account, Account):
            print("Object given is not type Account()")
            return False
        try:
            for account in self.accounts:
                if account.name == new_account.name:
                    print("Account with same name allready exist")
                    return False
            self.accounts.append(new_account)
            return True
        except ValueError as err:
            print(err)
        return False

    def transfer(self, origin, dest, amount=0):
        """"
        Perform the fund transfer
            f@origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        try:
            for account in self.accounts:
                if account.name == origin:
                    attributes = dir(account)
                    if len(attributes) % 2 == 0:
                        raise AttributeError("The attribute count of the object is not even")
                    is_value = 0
                    is_id = 0
                    is_name = 0
                    for attribute in attributes:
                        if attribute[0] == 'b':
                            raise AttributeError("The attribute starting with b")
                        if attribute[0:3] == "zip" or attribute[0:4] == "addr":
                            raise AttributeError("The attribute start with zip or addr")
                        if attribute == "name":
                            is_name = 1
                        if attribute == "id":
                            is_id = 1
                        if attribute == "value":
                            is_value = 1
                    if not is_value or not is_id or not is_name:
                        raise AttributeError("The account object should have name, id, value")
                    if not isinstance(account.name, str):
                        raise TypeError("Account name is not of the type string")
                    if not isinstance(account.id, int):
                        raise TypeError("Account id is not of the type int")
                    if not isinstance(account.value, (int, float)):
                        raise TypeError("Account value is not of the type int or float")
                    if account.value < 0 or amount > account.value:
                        raise ValueError("Not enough balance")
                    origin_account = account
                if account.name == dest:
                    attributes = dir(account)
                    if len(attributes) % 2 == 0:
                        raise AttributeError("The attribute count of the object is not even")
                    for attribute in attributes:
                        if attribute[0] == 'b':
                            raise AttributeError("The attribute starting with b")
                        if attribute[0:3] == "zip" or attribute[0:4] == "addr":
                            raise AttributeError("The attribute start with zip or addr")
                        if attribute == "name":
                            is_name = 1
                        if attribute == "id":
                            is_id = 1
                        if attribute == "value":
                            is_value = 1
                    if not is_value or not is_id or not is_name:
                        raise AttributeError("The account object should have name, id, value")
                    if not isinstance(account.name, str):
                        raise TypeError("Account name is not of the type string")
                    if not isinstance(account.id, int):
                        raise TypeError("Account id is not of the type int")
                    if not isinstance(account.value, (int, float)):
                        raise TypeError("Account value is not of the type int or float")
                    dest_account = account
            origin_account.value -= amount
            dest_account.value += amount
            return True
        except AttributeError as err:
            print(err)
        except TypeError as err:
            print(err)
        return False

    def fix_account(self, name):
        """
        Fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        for account in self.accounts:
            if account.name == name:
                if isinstance(account.name, str):
                    attributes = dir(account)
                    if len(attributes) % 2 == 0:
                        account.extra = "hi"
                    for attribute in attributes:
                        if attribute[0] == 'b':
                            sub_attribute = attribute[1:]  # remove the first character 'b'
                            setattr(account, sub_attribute, getattr(account, attribute))  # create new attribute without 'b' and copy value
                            delattr(account, attribute)
                        if attribute[0:3] == "zip" or attribute[0:4] == "addr":
                            sub_attribute = "new_" + attribute
                            setattr(account, sub_attribute, getattr(account, attribute))  # create new attribute without 'b' and copy value
                            delattr(account, attribute)
                        if attribute == "name":
                            is_name = 1
                        if attribute == "id":
                            is_id = 1
                        if attribute == "value":
                            is_value = 1
                    if not is_value or not is_id or not is_name:
                        setattr(account, 'name', "defalt name")
                    if not isinstance(account.name, str):
                        new_name = "new_" + str(account.name)
                        account.name = new_name
                    if not isinstance(account.id, int):
                        new_id = 0
                        account.id = new_id
                    if not isinstance(account.value, (int, float)):
                        new_value = 0
                        account.value = new_value
                    return True
        return False
