import os
import requests	
def GetFiles(input=None):
    """
    This function will run inside the folder determined by where I run 
    gumroadupload.py  It will come up with a list of files for the GetDetails 
    function to use.
    """
    # default: get files from current working directory
    if input is None:
        input = "testfolder"
        
    #make ls of files
  
    # python has a way of returning a list of filenames
    ListOfFiles = os.listdir(input) # get filenames from dir "."
    print "This is the list of files that are being recognized by the program:" + str(ListOfFiles)
    return ListOfFiles




def GetDetails():
    """
    This function will take a bunch of files, and get the Product attribute for
    CreateProduct, as well as name and price info from the file names. It will 
    associate the Product attribute with the file somehow so that UploadFileToProduct
    knows which ones go where
    """
    files = GetFiles()
    details = dict()
    #Separate filenames by character '-'
    #Put each of those separate entities into a part of the dictionary
    for filename in files:
        price = GetPriceFromFilename(filename)
        videoname = GetVideoNameFromFilename(filename)
        productname = GetProductNameFromFilename(filename)
        videonumber = GetVideoNumberFromFilename(filename)
        
        # do something with the file
        something = {
                "price": price,
                "name": videoname,
                "product": productname,
                "videonumber": videonumber,
            }
        details[filename] = something
    
    print """This is a dictionary full of associated information for each file. 
    There should be one dictionary entry for each file: """ + str(len(details)) +    "\n" + "This is the dictionary itself: "
    print details
    return details # print must go before return because python will return

#the next four functions are all for making the GetDetails function work with easier debugging for Bryan

def GetPriceFromFilename(filename):
    withsuffix =  filename.split("-")[3]
    return withsuffix.split(".")[0]
    
def GetVideoNameFromFilename(filename):
    return filename.split("-")[1]

def GetProductNameFromFilename(filename):
    return filename.split("-")[0]

def GetVideoNumberFromFilename(filename):
    return filename.split("-")[2]


def GetExistingProducts():
	"""
	This function will get the list of current products on Gumroad and put them in a list for the program so
	no duplicate products are created
	"""
	existingproducts = ['existing']
	#some API stuff goes here to ask Gumroad for the list of existing products, and make it in a list format nicely
	return existingproducts

def CreateProductList():
	"""
	This function will create a product in Gumroad for each unique Product found
	by GetDetails, so UploadFileToProduct can put the files there
	"""
	ProductToCreate = GetDetails()
    #take only the products that are unique from the dictionary and ask Gumroad
    #to create them

	existingproducts = GetExistingProducts()

	productstoadd = []

	for (name,details) in ProductToCreate.items():
		if details['product'] not in existingproducts:
			productstoadd.append(details['product'])

	print "This product has been created on GumRoad: " + str(productstoadd)
	print "This is the current list of products on GumRoad:" + str(existingproducts)
	return productstoadd

def AddProducts():
	"""
	This function will add the products that CreateProductList found to the
	Gumroad site via their API
	"""
	Adding = CreateProductList()
	#Turn Adding into the format that the API needs to create products
	#Send them to Gumroad for creation
	#check that this has worked? If error, then what?
	

def UploadFileToProduct():
    """
    This function will take the file and upload it to the Gumroad product that 
    matches it's file details from GetDetails
    """
    FilesToUpload = GetDetails()
    #get the file's product info from the dictionary and upload that file to
    #the product that matches the dict entry
    for file in FilesToUpload:
        productname = FilesToUpload[file]['product']
        #gumroad opens productname
        #upload file to productname
        print "the file : " + str(file) + " has been uploaded to " + str(productname)



def main():
    """
    Upload to Gumroad.
    """
    UploadFileToProduct()

# This goes at the bottom of the file. It tells python to do these specific
# commands when running the file.
if __name__ == "__main__":
    main()

