import os

def UploadFileToProduct(input):
    """
    This function will take the file and upload it to the Gumroad product that 
    matches it's file details from GetDetails
    """
    FilesToUpload = GetDetails(input)
    #get the file's product info from the dictionary and upload that file to
    #the product that matches the dict entry
    print "This file has been uploaded to GumRoad:" + str(input)
    
def CreateProduct(input):
    """
    This function will create a product in Gumroad for each unique Product found
    by GetDetails, so UploadFileToProduct can put the files there
    """
    ProductToCreate = GetDetails(input)
    #take only the products that are unique from the dictionary and ask Gumroad
    #to create them
    print "This product has been created on GumRoad:" + str(products)
    return products

def GetDetails(input):
    """
    This function will take a bunch of files, and get the Product attribute for
    CreateProduct, as well as name and price info from the file names. It will 
    associate the Product attribute with the file somehow so that UploadFileToProduct
    knows which ones go where
    """
    files = GetFiles(input)
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
    There should be one dictionary entry for each file""" + len(something) 
    return details # print must go before return because python will return

def GetPriceFromFilename(filename):
    print 
    return filename.split("-")[3]
    
def GetVideoNameFromFilename(filename):
    return filename.split("-")[1]
def GetProductNumberFromFilename(filename):
    return filename.split("-")[0]
def GetVideoNumberFromFilename(filename):
    return filename.split("-")[2]
    
def GetFiles(input=None):
    """
    This function will run inside the folder determined by where I run 
    gumroadupload.py  It will come up with a list of files for the GetDetails 
    function to use.
    """
    # default: get files from current working directory
    if input is None:
        input = "."
        
    #make ls of files
  
    # python has a way of returning a list of filenames
    ListOfFiles = os.listdir(input) # get filenames from dir "."
    print "This is the list of files that are being recognized by the program:" + str(ListOfFiles)
    return ListOfFiles


def main():
    """
    Upload to Gumroad.
    """
    files = GetFiles()
    #details = GetDetails(files)
   # for product in details:
   #     UploadFileToGumroad(product)

#This is my debugging section where I can run stuff to play with it, without running
#it inside the other functions
filename = "Test product - Testfile - M123.mp4"
print GetVideoNumberFromFilename(filename)
# This goes at the bottom of the file. It tells python to do these specific
# commands when running the file.
if __name__ == "__main__":
    main()