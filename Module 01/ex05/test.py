from the_bank import Account, Bank

if __name__ == "__main__":
	bank = Bank()
	newacc = Account('Charlie McG', info= 'bitebite')
	bank.add(newacc)
	bank.fix_account('Charlie McG')
	if bank.transfer('Charlie McG', 'Charlie McG') is False:
		print("failed")
	else:
		print("success")