# RAW DATA
platform = ['Shopee','Tokopedia','Lazada','Blibli','Tiktok Shop']
sales = [25000,15000,1500,500,5000]
order = [125,50,15,10,20]
pv = [1100,360,120,160,300]

# FORMULA FOR CONVERSION RATE AND AVG BASKET SIZE
cr_formula = lambda o,p : round(o/p*100,1)
abs_formula = lambda s,o : s//o

cr = [f'{cr_formula(order[x],pv[x])}%' for x in range(len(sales))]
abs = [abs_formula(sales[x],order[x]) for x in range(len(sales))]

# TABEL IN DICTIONARY
tabel_dashboard = {
    'Platform': platform,
    'Sales': sales,
    'Order': order,
    'Product Views': pv,
    'Conversion Rate': cr,
    'Avg Basket Size': abs
    }

# ADDITIONAL RAW DATA 
banyak_platform = len(platform)
banyak_kolom = len(tabel_dashboard.keys())                  
banyak_baris = len((list(tabel_dashboard.values()))[0])     
menu_request = '0'
editable = ['Sales','Order','Product Views']
noneditable = ['Platform','Conversion Rate','Avg Basket Size']



# MENU FUNCTION

def home():
    global menu_request
    print('''
====== Welcome to Seller Dashboard ======

Main Menu
1. Show Platform Performance Report
2. Create New Platform Data
3. Update Existing Platform Data
4. Delete Existing Platform Data
5. Exit Seller Dashboard
''')
    menu_request = input('Please choose menu number [1-5]: ')


# TABLE FUNCTION

def line():
    print('--------------------------------------------------------------------------------------------------------------------')

def header():
    for x in tabel_dashboard:
        print('{:<15}'.format(x),end='    ')

def content(index_list):
    for index in range(banyak_kolom):
        values = list(tabel_dashboard.values())[index][index_list]
        print('{:<15}'.format(values),end='    ')

def platform_performance():
    global tabel_dashboard
    banyak_platform = len(platform)
    print()
    print('ALL PLATFORM PERFORMANCE')
    line()
    header()
    print()
    line()
    for y in range(banyak_platform): 
        content(y)
        print()
    line()
    print()

def single_table(variable):
    line()
    header()
    print()
    line()
    content(variable)
    print()
    line()


# READ FUNCTION

def submenu_menu1():
    print('''
====== Show Platform Performance Report ======

Sub Menu
1. Show All Platform Performance
2. Find Performance by Platform
3. Back to Main Menu
''')

def menu1():
    command = 'start'
    while command == 'start':
        submenu_menu1()
        sub_menu1_request = input('Please choose sub-menu number [1-3]: ')
        if sub_menu1_request == '1':                                
            if len(sales)>0:                                            # DICEK TERLEBIH DAHULU APAKAH DATA ADA ATAU TIDAK
                platform_performance()
            else:
                print('No Platform Performance Report Found.')
        elif sub_menu1_request == '2':
            while command == 'start':
                platform_name = input('Input Platform Name: ')
                platform_name = platform_name.title()                   # MEMBUAT HURUF AWAL YANG DIINPUT MENJADI CAPITAL
                if platform_name in platform:                           # CHECKING APAKAH DATA SUDAH ADA
                    index_platform = platform.index(platform_name)
                    print()
                    print(f'Showing data for: {platform_name}')
                    single_table(index_platform)
                    while command == 'start':
                        ask1 = input('Do you want to search another data? (Y/N): ')
                        ask1 = ask1.title()
                        if ask1 == 'Y':
                            break
                        elif ask1 == 'N':
                            print('Your search is stopped.')
                            command = 'stop'
                            menu1()
                        else:
                            print('ERROR: Wrong Input. Try again.')
                else:
                    print('ERROR: Platform Data Not Found. Please try again.')
                    command = 'stop'
                    menu1()
        elif sub_menu1_request == '3':
            command = 'stop'
        else:
            print()
            print(f'ERROR: MENU NOT FOUND. Try again.')


# CREATE FUNCTION

def submenu_menu2():
    print('''
====== Create New Platform Data ======

Sub Menu
1. Input Platform Details
2. Back to Main Menu
''')

def menu2():
    global platform
    command = 'start'
    while command == 'start':
        submenu_menu2()
        sub_menu2_request = input('Please choose sub-menu number [1-2]: ')
        if sub_menu2_request == '1':
            new_platform = input('Input new platform name: ')
            new_platform = new_platform.title()                     # MEMBUAT HURUF AWAL YANG DIINPUT MENJADI CAPITAL
            if new_platform in platform:                            # CHECKING APAKAH DATA SUDAH ADA ATAU TIDAK
                print('ERROR: Platform already exists. Please only input new platform data.')
            else:
                while command == 'start':
                    new_sales = (input('Input Sales data: '))
                    new_order = (input('Input Order count: '))
                    new_pv = (input('Input Product Views: '))
                    if new_sales.isnumeric() and new_order.isnumeric() and new_pv.isnumeric():     # CHECKING NUMERIC INPUT
                        new_sales = int(new_sales)
                        new_order = int(new_order)
                        new_pv = int(new_pv)  
                        new_cr = f'{cr_formula(new_order,new_pv)}%'                 # MEMANGGIL FUNGSI LAMBDA CR
                        new_abs = abs_formula(new_sales,new_order)                  # MEMANGGIL FUNGSI LAMBDA ABS
                        while command == 'start':
                            save = input('Do you want to save the data? (Y/N): ')
                            save = save.capitalize()
                            if save == 'Y':
                                platform.append(new_platform)
                                sales.append(new_sales)
                                order.append(new_order)
                                pv.append(new_pv)
                                cr.append(new_cr)
                                abs.append(new_abs)
                                print('New data is successfully added to the existing report.')
                                command = 'stop'
                                menu2()
                            elif save == 'N':
                                print('New Platform data creation is cancelled.')
                                command = 'stop'
                                menu2()
                            else:
                                print('ERROR: Wrong Input. Try again.')
                    else:
                        print('Error: Data MUST be NUMBER. Please try again.')
        elif sub_menu2_request == '2':
            command = 'stop'
        else:
            print(f'ERROR: MENU NOT FOUND. Try again.')


# UPDATE FUNCTION

def submenu_menu3():
    print('''
=== Update Existing Platform Data ===

Sub Menu
1. Update Platform Details
2. Back to Main Menu
''')

def menu3():
    global platform
    command = 'start'
    submenu_menu3()
    sub_menu3_request = input('Please choose sub-menu number [1-2]: ')
    if sub_menu3_request == '1':
        edit_platform = input('Input Platform name to be changed: ')
        edit_platform = edit_platform.title()
        while command == 'start':
            if edit_platform in platform:                                       # CHECKING DATA SUDAH ADA ATAU TIDAK
                index_edit = platform.index(edit_platform)
                print(f'Existing Data for: {edit_platform}')
                single_table(index_edit)
                while command == 'start':
                    cont = input('Do you want to update this data? (Y/N):')
                    cont = cont.capitalize()
                    if cont == 'Y':
                        while command == 'start':
                            column_update = input('Input column/parameter to be changed: ')
                            column_update = column_update.title()
                            if column_update in editable:
                                while command == 'start':
                                    new_data = input('Input new data to replace: ')
                                    if new_data.isnumeric():
                                        while command == 'start':
                                            confirm = input('Do you want to save the data? (Y/N): ')
                                            confirm = confirm.capitalize()
                                            if confirm == 'Y': 
                                                new_data = int(new_data)
                                                tabel_dashboard[column_update][index_edit] = new_data
                                                new_sales = sales[index_edit]
                                                new_order = order[index_edit]
                                                new_pv = pv[index_edit]
                                                update_cr = f'{cr_formula(new_order,new_pv)}%'
                                                update_abs = abs_formula(new_sales,new_order)
                                                tabel_dashboard['Conversion Rate'][index_edit] = update_cr
                                                tabel_dashboard['Avg Basket Size'][index_edit] = update_abs
                                                print(f'Data {column_update} for {edit_platform} is updated.')
                                                command = 'stop'
                                                menu3()
                                            elif confirm == 'N':
                                                print('Data update is cancelled.')
                                                command = 'stop'
                                                menu3()
                                            else:
                                                print('ERROR: Wrong Input. Try Again.')
                                    else:
                                        print('ERROR: Data MUST be NUMBER. Please try again.')
                            elif column_update in noneditable:
                                print('ERROR: You can not change data in this list. Please try again.')
                                command = 'stop'
                            else:
                                print('ERROR: Column/parameter NOT FOUND. Try Again.')
                    elif cont == 'N':
                        print('Data update is cancelled.')
                        command = 'stop'
                        menu3()
                    else:
                        print('ERROR: Wrong Input. Try Again.')
            else:
                print('ERROR: Platform NOT FOUND. Try Again.')
                command = 'stop'
                menu3()
    elif sub_menu3_request == '2':
        command = 'stop'
    else:
        print(f'ERROR: MENU NOT FOUND. Try again.')


# DELETE FUNCTION 

def submenu_menu4():
    print('''
=== Delete Existing Platform Data ===

Sub Menu
1. Delete Platform Details
2. Back to Main Menu
''')

def menu4():
    global platform
    command = 'start'
    while command == 'start':
        submenu_menu4()
        sub_menu4_request = input('Please choose sub-menu number [1-2]: ')
        if sub_menu4_request == '1':
            if len(sales)>0:                                                # CHECKING APAKAH ADA DATA ATAU TIDAK 
                platform_performance()
                while command == 'start':
                    delete_req = input('Please input Platform Name to be deleted: ')
                    delete_req = delete_req.title()
                    if delete_req in platform:
                        index_delete = platform.index(delete_req)
                        single_table(index_delete)
                        while command == 'start':
                            confirm = input('Are you sure you want to delete this data? (Y/N): ')
                            confirm = confirm.capitalize()
                            if confirm == 'Y':
                                platform.pop(index_delete)
                                sales.pop(index_delete)
                                order.pop(index_delete)
                                pv.pop(index_delete)
                                cr.pop(index_delete)
                                abs.pop(index_delete)
                                print('Data has been deleted successfully.')
                                command = 'stop'
                                menu4()
                            elif confirm == 'N':
                                print('Data deletion is cancelled.')
                                command = 'stop'
                                menu4()
                            else:
                                print('ERROR: Wrong Input. Try again.')
                    else:
                        print('ERROR: Platform NOT FOUND. Try Again.')
                        command = 'stop'
                        menu4()
            else:
                print('No Platform Performance Report Found.')
        elif sub_menu4_request == '2':
            command = 'stop'
        else:
            print(f'ERROR: MENU NOT FOUND. Try again.')


# MAIN APPLICATION

home()

loop = 'begin'

while loop == 'begin':
    if menu_request == '1':
        menu1()
        home()
    elif menu_request == '2':
        menu2()
        home()
    elif menu_request == '3':
        menu3()
        home()
    elif menu_request == '4':
        menu4()
        home()
    elif menu_request == '5':
        print('Thank You & Good Bye!')
        loop = 'end'
    else:
        print('Menu NOT FOUND. Please try again.')
        home()
