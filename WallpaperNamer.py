#!usr/bin/env python
#Sort Downloaded LvD Files
import os, shutil, random, math
from PyPDF2 import PdfFileReader
from datetime import date
from glob import glob

### Variables
today = date.today()

renaming_folder_path = os.path.expanduser('~') + '/Desktop/#Wallpaper Renaming'
print_folder_location = '/Volumes/GoogleDrive/Shared drives/# Production/#LvD Fulfillment'

order_item_dict = {}

### Functions

def rename_pdf(pdf):
    #300023428-2-(2022-05-16)-Stnd-Sm-Samp-Rp 2-Qty 1-Radiant Sunshine-L9.5-W25-H9.pdf
    name_dict = {
        'order_number':'',
        'order_item':'',
        'due_date':str(today),
        'ship_via':'Prty',
        'material':'',
        'pdf_size':'',
        'pdf_repeat':'',
        'pdf_quantity':'',
        'template_name':'',
        'pdf_length':'',
        'pdf_width':'',
        'pdf_height':'',
        }

    pdf_name = pdf.split('/')[-1]
    file_path = pdf.split(pdf_name)[0]

    name_dict['order_number'] = get_order_number()
    name_dict['template_name'] = get_template_name(pdf_name)
    name_dict['material'] = get_material()
    name_dict['pdf_quantity'] = get_quantity()
    name_dict['pdf_height'], name_dict['pdf_width'], name_dict['pdf_repeat'], name_dict['pdf_size'] = get_dimensions(pdf, name_dict['pdf_quantity'])
    name_dict['pdf_length'] = get_length(name_dict['pdf_size'],name_dict['pdf_quantity'],name_dict['pdf_height'])
    name_dict['order_item'] = get_order_item(name_dict['order_number'])

    name_dict = confirm_name(name_dict, pdf, pdf_name)

    new_name = format_new_name(name_dict)
    return pdf, file_path + new_name

def format_new_name(name_dict):
    nd = name_dict
    #300023428-2-(2022-05-16)-Stnd-Sm-Samp-Rp 2-Qty 1-Radiant Sunshine-L9.5-W25-H9.pdf
    first_part = nd['order_number'] + '-' + nd['order_item'] + '-(' + nd['due_date'] + ')-' + nd['ship_via'] + '-'
    second_part = nd['material'] + '-' + nd['pdf_size'] + '-' + nd['pdf_repeat'] + '-' + nd['pdf_quantity'] + '-'
    third_part = nd['template_name'] + '-' + nd['pdf_length'] + '-' + nd['pdf_width'] + '-' + nd['pdf_height'] + '.pdf'
    return first_part + second_part + third_part

def confirm_name(name_dict, pdf, pdf_name):
    menu_options = (
        (1, 'All are correct.'),
        (2, 'Order Number: ' + name_dict['order_number']),
        (3, 'Material: ' + name_dict['material']),
        (4, 'Template Name: ' + name_dict['template_name']),
        (5, 'Quantity: ' + name_dict['pdf_quantity']),
    )

    valid_options = populateValidOptions(menu_options)
    print('Please confirm the following renaming elements.\nEnter a number to edit that element')
    print_menu_options(menu_options)
    command = (get_input(valid_options)-1)
    if command == 0:
        return name_dict
    else:
        return update_element(name_dict, command, pdf, pdf_name)

def update_element(name_dict, command, pdf, pdf_name):
    if command == 1:
        name_dict['order_number'] = get_order_number()
    elif command == 2:
        name_dict['material'] = get_material()
    elif command == 3:
        name_dict['template_name'] = get_template_name(pdf_name)
    elif command == 4:
        name_dict['pdf_quantity'] = get_quantity()
        name_dict['pdf_height'], name_dict['pdf_width'], name_dict['pdf_repeat'], name_dict['pdf_size'] = get_dimensions(pdf, name_dict['pdf_quantity'])
    
    return confirm_name(name_dict, pdf, pdf_name)

def get_input(valid_options_list):
    command = input('\n| Command > ')
    try:
        command = int(command)
    except ValueError:
        print('\n| Please enter a valid number')
        return get_input(valid_options_list)
    while command not in valid_options_list:
        print('\n| Not a valid choice.')
        return get_input(valid_options_list)
    return command

def print_menu_options(list_of_menu_options): #takes a list of menu items and prints them out neatly. See below for format.
    # (1, Smooth)
    # (int for valid option, displayed menu option)
    # Will display like: (1) Smooth
    for option in list_of_menu_options:
        print('|  (' + str(option[0]) + ')', option[1],)

def populateValidOptions(menuOptions): # Gathers valid options from menus (like batchDetailsMenu) and ensures they are valid
    validOptions = []
    for option in menuOptions:
        validOptions.append(option[0])
    return validOptions

def get_order_item(order_number):
    existing_count = len(glob(renaming_folder_path + '/*312345678*.pdf'))
    if order_number in order_item_dict:
        order_item_dict[order_number] += 1
        count_to_return = order_item_dict[order_number]
    else:
        order_item_dict[order_number] = existing_count + 1
        count_to_return = order_item_dict[order_number]
    return str(count_to_return)

def get_length(size, quantity, height):
    if size == 'Samp':
        return 'L9.5'
    else:
        quantity = int(quantity.split('Qty ')[1])
        height = float(height.split('H')[1])

        first = math.floor(quantity / 2) #quantity divided by two, rounded down, to get the number of panels we can fit side by side
        second = first + (quantity % 2) #quantity + 1 for any odd-quantitied items
        third = height + .5 # height + .5 because there's a .5" gap between each row
        length = second * third
        return 'L' + str(length)

def get_dimensions(pdf, quantity):
    reader = PdfFileReader(pdf)
    page = reader.getPage(0)
    height = (page.cropBox.getUpperRight()[1])/72
    quantity = quantity.split(' ')[-1]
    if str(height) == '9.0':
        height = 'H9'
        width = 'W25'
        repeat = 'Rp 2'
        size = 'Samp'
        return str(height), width, repeat, size
    else:
        height = 'H' + str(height)
        width = 'W' + str(int(quantity) * 24 + 1)
        repeat = int(page.cropBox.getUpperRight()[0])/72
        if repeat % 2 == 0:
            repeat = 'Rp ' + str(int(repeat/12))
        else:
            repeat = 'Rp ' + str(int((repeat - 1)/12))
        size = 'Full'
        return str(height), width, repeat, size

def get_quantity():
    quantity = input("\nHow many were ordered?\nQuantity: ")
    try:
        quantity = int(quantity)
        return 'Qty ' + str(quantity)
    except:
        print(str(quantity) + ' is not a valid quantity. Please enter a whole number.')
        return get_quantity

def get_order_number():
    orderNumber = input("\nWhat is the order number?\nOrder Number: ")
    while orderNumber[0] != '3':
        orderNumber = input ("\nThe order number should begin with 3: ")
    while len(orderNumber) != 9:
        orderNumber = input ("\nPlease enter a 9 digit order number: ")
    return orderNumber

def get_template_name(pdf_name):
    if '_Wallpaper' in pdf_name:
        name_guess = pdf_name.split(pdf_name.split('_')[0] + '_')[1].split('_Wallpaper')[0].replace('_',' ')
        template_response = input('\nIs the wallpaper template name ' + name_guess + '?\n(y/n) ').lower()
        if template_response == 'y':
            return name_guess
        else:
            template_name = input("\nWhat is the wallpaper template name?\nTemplate Name: ").title()
            return template_name

def get_material():
    material_list = ('Wv', 'Sm', 'Tr')
    material = input("\nWhich type of paper is it?\n(wv/sm/tr) ").title()
    while material not in material_list:
        material = input("\nPlease enter a correct material.\n(wv/sm/tr) ").title()
    return material

def get_new_names(pdf_list):
    list_to_rename = []
    for pdf in pdf_list:
        print('\n\nPDF:', pdf.split('/')[-1])
        correct_name = input('Is this name correct? (y/n): ').lower()
        if correct_name == 'y':
            continue 
        old_name, new_name = rename_pdf(pdf)
        list_to_rename.append([old_name, new_name])
    
    for print_pdf in list_to_rename:
        print(print_pdf[0].split('/')[-1], ' -> ' + print_pdf[1].split('/')[-1])
        os.rename(print_pdf[0], print_pdf[1])

def get_pdf_list(folder_path):
    return glob(folder_path)

def transfer_files():
    list_to_move = get_pdf_list(renaming_folder_path + '/*.pdf')
    if len(list_to_move) > 0:
        transferQuery = input("\nWould you like to transfer these file(s) for print?\n(y/n) ")
        if (transferQuery == 'y'):
            print("I like to move it move it.\n   -King Julian\n      -Reel 2 Reel")
            for print_pdf in list_to_move:
                try:
                    shutil.move(print_pdf, print_folder_location)
                    print('Moved', print_pdf.split('/')[-1])
                except OSError as err:
                    print(err)
        elif (transferQuery == 'n'):
            print("Keep it secret. Keep it safe. - Gandalf")

def main():
    pdf_list = get_pdf_list(renaming_folder_path + '/*.pdf')
    if len(pdf_list) == 0:
        return
    else:
        get_new_names(pdf_list)
        transfer_files()
        return

main()