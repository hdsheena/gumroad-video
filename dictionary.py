testdictionary = {'Test product 3 - Testfile 3 - M456 - 1.mp4': {'product': 'Test product 3 ', 'price': ' 1', 'name': ' Testfile 3 ', 'videonumber': ' M456 '}, 'Test product 2 - Testfile 2 - M234 - 1.mp4': {'product': 'Test product 2 ', 'price': ' 1', 'name': ' Testfile 2 ', 'videonumber': ' M234 '}}
existingproducts = []
productstoadd = []
for (name,details) in testdictionary.items():
	if details['product'] not in existingproducts:
		productstoadd.append(details['product'])

print productstoadd
print existingproducts
