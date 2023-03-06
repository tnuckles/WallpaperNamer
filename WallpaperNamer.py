#!usr/bin/env python
#Sort Downloaded LvD Files
import os, shutil, random, math
from PyPDF2 import PdfFileReader
from datetime import date

###Variables

folderLocation = os.path.expanduser('~') + '/Desktop/#Wallpaper Renaming'
printFolderLocation = "/Volumes/GoogleDrive/Shared drives/# Production/#LvD Fulfillment"

materialTypes = ('Wv', 'Sm', 'Tr')
fullOrSamp = ('Full', 'Samp')
validHeights = (3,4,5,6,7,8,9,10,11,12)
swears = ('Whoops.', 'Frick.', 'Cottonheaded Ninimuggins.', 'Shoot darn', 'Ah heck.', 'Daggum.', 'Dagnabbit', 'Balderdash.', "This is why we can't have nice things.", 'Srsly?', "That's fun.", 'Oh come on!', "What in the Mary Berry's biscuits!", 'Gee Manetti Christmas!', 'Probably Brenna\'s fault.', 'Someone call Brenna, she can save us.')

today = date.today()

###Functions

def randomSwears():
    print('\n', random.choice(swears))

def checkForFile(fileName, itemName):
    counter = int(itemName.split(')')[0].split('(')[1])
    while os.path.exists(itemName) == True:
        print('File with new name already exists.\n' + itemName)
        itemName = itemName.split('(')[0] + '(' + str(counter + 1) + ')' + itemName.split(')')[1] + '.pdf'
        counter += 1
    else:
        try:
            os.rename(fileName, itemName)
            print("\nOriginal File Name: ", fileName, "\nNew File Name: ", itemName, "\nFile successfully renamed.")
        except OSError:
            print(OSError)
            print('\nError renaming.\nOld File Name: ' + fileName + '\nAttempted New File Name: ' + itemName)

#300001432(1)-Chasin Cheetahs-Sm-Samp-Rp 4-Qty 1-W9-H25.pdf
#1036617_Vintage_Peonies_Wallpaper_33308_bi_v

def confirmName(newName, oldName):
    print('\nOriginal Name: ', oldName, '\nNew Name: ', newName)
    proceed = int(input("\nIs this filename correct? Enter the number for how you'd like to proceed:\n\n1. It's correct\n2. Change Order Number\n3. Change Wallpaper Name\n4. Change Paper Type\n5. Change Full or Sample\n6. Change Repeat \n7. Change Quantity Ordered\n8. Change Height\n\nChoice: "))
    nameValues = [newName.split('(')[0], newName.split('-')[1], newName.split('-')[2], newName.split('-')[3], newName.split('-')[4], newName.split('-')[5], newName.split('-')[6], ((newName.split('-')[7]).split('.pdf')[0])]
    nameStart = newName.split('-')[0] + '-'
    fullWidth =  "-W" + str(int((newName.split('-')[5]).split(' ')[1]) * 24 + 1) 

    if (proceed == 1): #correct
        print('\nNailed it.')
        return newName
    elif proceed == 2: #  Order Number
        randomSwears()
        orderNumber = input("\nWhat is the order number?\nOrder Number: ")
        while len(orderNumber) != 9:
            orderNumber = input ("\nPlease enter a 9 digit order number: ")
        newName = orderNumber + '(' + newName.split('(')[1]
        return confirmName(newName, oldName)
    elif proceed == 3: # Wallpaper Name
        randomSwears()
        templateName = input("\nWhat is the wallpaper template name?\nTemplate Name: ").title()
        nameEnd = '-'.join(nameValues[2::]) + '.pdf'
        newName = nameStart + templateName + '-' + nameEnd
        return confirmName(newName,oldName)
    elif proceed == 4: # Paper Type
        randomSwears()
        paperType = input("\nWhich type of paper is it?\n(wv/sm/tr) ").title()
        nameStart = nameStart + nameValues[1] + '-'
        nameEnd = '-'.join(nameValues[3::]) + '.pdf'
        newName = nameStart + paperType + '-' + nameEnd
        return confirmName(newName,oldName)
    elif proceed == 5: # Full or Sample
        randomSwears()
        orderSize = input("\nIs it a full panel or a sample?\n(f/s) ").lower()
        if orderSize == 's':
            orderSize = 'Samp'
            nameStart = nameStart + '-'.join(nameValues[1:3:]) + '-'
            nameEnd = '-'.join(nameValues[4:6:]) + '-W9-H25.pdf'
            newName = nameStart + orderSize + '-' + nameEnd
            return confirmName(newName,oldName)
        else:
            orderSize = "Full"
            height = input("\nHow tall is the panel? Please enter a height in feet.\n(3,4,5,6,7,8,9,10,11,12) ")
            if height == '12':
                nameStart = nameStart + '-'.join(nameValues[1:3:]) + '-'
                nameEnd = nameEnd = '-'.join(nameValues[4:6:]) + fullWidth + "-H" + str(int(height) * 12 + 2.25) + ".pdf"
                newName = nameStart + orderSize + '-' + nameEnd
                return confirmName(newName,oldName)
            else:
                nameStart = nameStart + '-'.join(nameValues[1:3:]) + '-'
                nameEnd = nameEnd = '-'.join(nameValues[4:6:]) + fullWidth + ("-H") + str(int(height) * 12 + 4.25) + ".pdf"
                newName = nameStart + orderSize + '-' + nameEnd
                return confirmName(newName,oldName)
    elif proceed == 6: # Repeat
        randomSwears()
        repeat = input('\nWhat is the pattern repeat?\nPlease enter a number in feet: ')
        nameStart = nameStart + '-'.join(nameValues[1:4:]) + '-'
        nameEnd = '-'.join(nameValues[5::]) + '.pdf'
        newName = nameStart + 'Rp ' + repeat + '-' + nameEnd
        return confirmName(newName,oldName)
    elif proceed == 7: # Quantity
        randomSwears()
        quantity = input("\nHow many were ordered?\nQuantity: ")
        nameStart = nameStart + '-'.join(nameValues[1:5:]) + '-'
        nameEnd = '-'.join(nameValues[6::]) + '.pdf'
        newName = nameStart + 'Qty ' + quantity + '-' + nameEnd
        return confirmName(newName,oldName)
    elif proceed == 8: # Height
        randomSwears()
        orderSize = input("\nIs it a full panel or a sample?\n(f/s) ").lower()
        if orderSize == 's':
            orderSize = 'Samp'
            nameStart = nameStart + '-'.join(nameValues[1:3:]) + '-'
            nameEnd = '-'.join(nameValues[4:6:]) + '-W9-H25.pdf'
            newName = nameStart + orderSize + '-' + nameEnd
            return confirmName(newName,oldName)
        else:
            orderSize = "Full"
            height = input("\nHow tall is the panel? Please enter a height in feet.\n(3,4,5,6,7,8,9,10,11,12) ")
            if height == '12':
                nameStart = nameStart + '-'.join(nameValues[1:3:]) + '-'
                nameEnd = nameEnd = '-'.join(nameValues[4:6:]) + fullWidth + "-H" + str(int(height) * 12 + 2.25) + ".pdf"
                newName = nameStart + orderSize + '-' + nameEnd
                return confirmName(newName,oldName)
            else:
                nameStart = nameStart + '-'.join(nameValues[1:3:]) + '-'
                nameEnd = nameEnd = '-'.join(nameValues[4:6:]) + fullWidth + ("-H") + str(int(height) * 12 + 4.25) + ".pdf"
                newName = nameStart + orderSize + '-' + nameEnd
                return confirmName(newName,oldName)

def renamePDF(fileName):
    reader = PdfFileReader(folderLocation + '/' + fileName)
    page = reader.getPage(0)
    orderNumber = input("\nWhat is the order number?\nOrder Number: ")
    while len(orderNumber) != 9:
        orderNumber = input ("\nPlease enter a 9 digit order number: ")
    try:
        if fileName.split('_')[3] == 'Wallpaper':
            templateName = input('\nIs the wallpaper template name ' + fileName.split('_')[1] + ' ' + fileName.split('_')[2] + '?\n(y/n) ').lower()
            if templateName == 'y':
                templateName = fileName.split('_')[1] + ' ' + fileName.split('_')[2]
        else:
            templateName = input("\nWhat is the wallpaper template name?\nTemplate Name: ").title()    
    except IndexError:
        templateName = input("\nWhat is the wallpaper template name?\nTemplate Name: ").title()
    paperType = input("\nWhich type of paper is it?\n(wv/sm/tr) ").title()
    quantity = input("\nHow many were ordered?\nQuantity: ")
    height = (page.cropBox.getUpperRight()[1])/72
    if height > 25: #checks for full order
        height = str(int(page.cropBox.getUpperRight()[1])/72)
        repeat = int(page.cropBox.getUpperRight()[0])/72
        width = str(int(quantity) * 24 + 1)
        orderSize = "Full"
        if repeat % 2 == 0:
            repeat = str(int(repeat/12))
        else:
            repeat = str(int((repeat - 1)/12))
        if height == '12':
            itemName = orderNumber + ("(1)-") + templateName + ("-") + paperType + ("-") + orderSize + ("-Rp ") + repeat  + ("-Qty ") + quantity + ("-W") + width + ("-H") + height + ".pdf"
        else:
            itemName = orderNumber + ("(1)-") + templateName + ("-") + paperType + ("-") + orderSize + ("-Rp ") + repeat  + ("-Qty ") + quantity + ("-W") + width + ("-H") + height + ".pdf"
    
    else: #or it's a sample
        height = '25'
        width = '9'
        orderSize = 'Samp'
        repeat = input('\nWhat is the pattern repeat?\nPlease enter a number in feet: ')
        itemName = orderNumber + ("(1)-") + templateName + ("-") + paperType + ("-") + orderSize + ("-Rp ") + repeat  + ("-Qty ") + quantity + ("-W") + width + ("-H") + height + ".pdf"

    itemName = confirmName(itemName, fileName)
    checkForFile(fileName, itemName)    

def fileNameCorrect(fileName):    
    print()
    print(fileName)
    correct = input("Is this filename correct? (y/n)").lower()
    if (correct == 'y'):
        print('Name is correct. Next.')
        return
    elif (correct == 'n'):
        print("Let's fix that.")
        renamePDF(fileName)
    else:
        fileNameCorrect(fileName)

def renameFiles():
    print('\n\nHello ' + os.path.expanduser('~').split('/')[-1] + '!')
    print('\nWorking in: ' + folderLocation + '\n')
    for roots, dirs, files in os.walk(folderLocation):
        for fileName in files:
            if fileName.startswith("."): #skips macOS X Hidden file ".DS_Store"
                continue
            else:
                fileNameCorrect(fileName)

def validationFailed(fileName, reason):
    print("\nValidation failed.")
    print("File: ", fileName)
    print("Reason: ", reason)

def validateFileName(fileName):
    validation = True
    extensionRemoval = fileName.split('.pdf')[0]
    splitCheck = extensionRemoval.split('-')
    orderNumber = splitCheck[0]
    paperType = splitCheck[2]
    orderSize = splitCheck[3]
    repeat = splitCheck[4]
    quantity = splitCheck[5]
    width = splitCheck[6]
    height = splitCheck[7]

    try:
        if len(orderNumber.split('(')[0]) != 9:
            validationFailed(fileName, "Order Number not 9 digits.")
            validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if orderNumber.startswith("3") == False:
            validationFailed(fileName, "Order number does not begin with 3.")
            validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if (int(orderNumber.split('(')[0]) % 1 != 0):
            validationFailed(fileName, "Order number is not a whole number.")
            print(int(orderNumber) % 1) 
            validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if paperType not in materialTypes:
            validationFailed(fileName, 'Paper Type "' + splitCheck[2] + '" is invalid.')
            validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if orderSize not in fullOrSamp:
            validationFailed(fileName, 'Order Size "' + splitCheck[3] + '" is invalid.')
            validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if (int(repeat.split(' ')[1]) % 1 != 0):
            validationFailed(fileName, 'Repeat is not a whole number.')
            validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if (int(quantity.split(' ')[1]) % 1 != 0):
            validationFailed(fileName, 'Quantity is not a whole number.')
            validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if orderSize == "Full":
            pdfWidth = int(width.split('W')[1]) - 1
            pdfQuantity = int(quantity.split(' ')[1])
            if pdfWidth % pdfQuantity != 0:
                validationFailed(fileName, 'Width of ' + width + ' is not valid for a full order.')
                validation = False
            if ((int(float(height.split('H')[1]) - 4.25)) / 12) not in validHeights:
                if ((int(float(height.split('H')[1]) - 2.25)) / 12) not in validHeights:
                    validationFailed(fileName, 'Height of ' + height + ' is not valid for a full order.')
                    validation = False
    except IndexError:
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False
    try:
        if orderSize == "Samp":
            if int(width.split('W')[1]) != 9:
                validationFailed(fileName, 'Width of ' + width + ' is not valid for a sample order.')
                validation = False
            if int(height.split('H')[1]) != 25:
                validationFailed(fileName, 'Height of ' + height + ' is not valid for a sample order.')
                validation = False
    except IndexError: 
        print("Looks like your name might not be formatted right. I can't detect the different sections.")
        validation = False

    return validation

def transferFiles():
    transferQuery = input("\nWould you like to transfer these file(s) for print?\n(y/n) ")
    if (transferQuery == 'y'):
        print("I like to move it move it.\n   -King Julian\n      -Reel 2 Reel")
        for roots, dirs, files in os.walk(folderLocation):
            for file in files:
                if file.startswith("."): #skips macOS X Hidden file ".DS_Store"
                    continue
                elif file.endswith('.pdf') != True:
                    continue
                else:
                    print("\nFirst I gotta validate.")
                    if validateFileName(file) == True:
                        try:
                            file = update_name_to_current_convention(file)
                            shutil.move(file, printFolderLocation)
                            print("File: ", file, "\nPassed Validation! *click* Noice!\nMoved for print.")
                        except OSError as err:
                            print(err)
                    else:
                        continue
    elif (transferQuery == 'n'):
        print("Keep it secret. Keep it safe. - Gandalf")
    else:
        transferFiles()

def main():
    os.chdir(folderLocation)
    if len(os.listdir(folderLocation)) == 0:
        print("What the heck? Your folder is empty. I got no work to do!")
    else:    
        renameFiles()
        transferFiles()
        print('\n\nFinished!\n\n')

def calculate_length(quantity, height):
    quantity = int(quantity.split('Qty ')[1])
    height = float(height.split('H')[1])

    first = math.floor(quantity / 2) #quantity divided by two, rounded down, to get the number of panels we can fit side by side
    second = first + (quantity % 2) #quantity + 1 for any odd-quantitied items
    third = height + .5 # height + .5 because there's a .5" gap between each row
    length = second * third
    return length

def update_name_to_current_convention(print_pdf):
    #300001432(1)-Chasin Cheetahs-Sm-Samp-Rp 4-Qty 1-W9-H25.pdf
    #300023428-2-(2022-05-16)-Stnd-Sm-Samp-Rp 2-Qty 1-Radiant Sunshine-L9.5-W25-H9.pdf

    name_dict = {
        'order_number':print_pdf.split('(')[0],
        'order_item':print_pdf.split('(')[1].split(')')[0],
        'due_date':str(today),
        'ship_via':'Prty',
        'material':print_pdf.split('-')[2],
        'pdf_size':print_pdf.split('-')[3],
        'pdf_repeat':print_pdf.split('-')[4],
        'pdf_quantity':print_pdf.split('-')[5],
        'template_name':print_pdf.split('-')[1],
        'pdf_length':'',
        'pdf_width':print_pdf.split('-')[6],
        'pdf_height':print_pdf.split('-')[7].split('.pdf')[0],
    }

    if name_dict['pdf_width'] == 'W9':
        name_dict['pdf_length'] = 'L9.5'
        name_dict['pdf_width'] = 'W25'
        name_dict['pdf_height'] = 'H9'
    else:
        quantity = name_dict['pdf_quantity']
        height = name_dict['pdf_height']
        name_dict['pdf_length'] = 'L' + str(calculate_length(quantity, height))
        
    new_name = name_dict['order_number'] + '-' + name_dict['order_item'] + '-(' + name_dict['due_date'] + ')-' + name_dict['ship_via'] + '-' + name_dict['material'] + '-' + name_dict['pdf_size'] + '-' + name_dict['pdf_repeat'] + '-' + name_dict['pdf_quantity'] + '-' + name_dict['template_name'] + '-' + name_dict['pdf_length'] + '-' + name_dict['pdf_width'] + '-' + name_dict['pdf_height'] + '.pdf' 
    
    os.rename(print_pdf, new_name)

    return new_name

main()
