# Name: Babitha Kasa
# College Stationery Shop
read_input = open('input1.txt','r')
# read_input = open('input2.txt','r')
# read_input = open('input3.txt','r')
# read_input = open('input4.txt','r')

lines = read_input.readlines()

sub_total = 0

tshirt_sub_total = 0
jacket_sub_total = 0
cap_sub_total = 0
notebook_sub_total = 0
pens_sub_total = 0
markers_sub_total = 0

tshirt_discount = 0
jacket_discount = 0
cap_discount = 0
notebook_discount = 0
pens_discount = 0
markers_discount = 0


def ADD_ITEM(item_name, item_quantity):
    
    if item_name == "TSHIRT":
        tshirt_quantity = 0
        tshirt_quantity = int(tshirt_quantity) + int(item_quantity)
        if tshirt_quantity < 3:
            global tshirt_sub_total
            global tshirt_discount
            tshirt_sub_total = int(tshirt_sub_total) + (int(tshirt_quantity) * 1000)
            tshirt_discount = int(tshirt_discount) + ((int(tshirt_quantity) * 1000) - (100 * int(tshirt_quantity)))
            print("ITEM ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED")

    elif item_name == "JACKET":
        jacket_quantity = 0
        jacket_quantity = int(jacket_quantity) + int(item_quantity)
        if jacket_quantity < 3:
            global jacket_sub_total
            global jacket_discount
            jacket_sub_total = int(jacket_sub_total) + (int(jacket_quantity) * 2000)
            jacket_discount = int(jacket_discount) + ((int(jacket_quantity) * 2000) - (100 * int(jacket_quantity)))
            print("ITEM ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED")
    
    elif item_name == "CAP":
        cap_quantity = 0
        cap_quantity = int(cap_quantity) + int(item_quantity)
        if cap_quantity < 3:
            global cap_sub_total
            global cap_discount
            cap_sub_total = int(cap_sub_total) + (int(cap_quantity) * 500)
            cap_discount = int(cap_discount) + ((int(cap_quantity) * 500) - (100 * int(cap_quantity)))
            print("ITEM ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED")

    elif item_name == "NOTEBOOK":
        notebook_quantity = 0
        notebook_quantity = int(notebook_quantity) + int(item_quantity)
        if notebook_quantity < 4:
            global notebook_sub_total
            global notebook_discount
            notebook_sub_total = int(notebook_sub_total) + (int(notebook_quantity) * 200)
            notebook_discount = int(notebook_discount) + ((int(notebook_quantity) * 200) - (40 * int(notebook_quantity)))
            print("ITEM ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED")
    
    elif item_name == "PENS":
        pens_quantity = 0
        pens_quantity = int(pens_quantity) + int(item_quantity)
        if pens_quantity < 4:
            global pens_sub_total
            global pens_discount
            pens_sub_total = int(pens_sub_total) + (int(pens_quantity) * 300)
            pens_discount = int(pens_discount) + ((int(pens_quantity) * 300) - (30 * int(pens_quantity)))
            print("ITEM ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED")

    elif item_name == "MARKERS":
        markers_quantity = 0
        markers_quantity = int(markers_quantity) + int(item_quantity)
        if markers_quantity < 4:
            global markers_sub_total
            global markers_discount
            markers_sub_total = int(markers_sub_total) + (int(markers_quantity) * 500)
            markers_discount = int(markers_discount) + ((int(markers_quantity) * 500) - (25 * int(markers_quantity)))
            print("ITEM ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED")

def PRINT_BILL():
    global sub_total
    global tshirt_sub_total
    global jacket_sub_total
    global cap_sub_total
    global notebook_sub_total
    global pens_sub_total
    global markers_sub_total
    global tshirt_discount
    global jacket_discount
    global cap_discount
    global notebook_discount
    global pens_discount
    global markers_discount
    
    sub_total = int(tshirt_sub_total) + int(jacket_sub_total) + int(cap_sub_total) + int(notebook_sub_total) + int(pens_sub_total) + int(markers_sub_total)

    if sub_total > 999:

        if sub_total > 2999:
            sub_discount = int(tshirt_discount) + int(jacket_discount) + int(cap_discount) + int(notebook_discount) + int(pens_discount) + int(markers_discount)
            total_discount = int(sub_total) - int(sub_discount)
            print("TOTAL_DISCOUNT %.2f" % total_discount)
            total = int(sub_total) - int(total_discount)
            additional_discount = int(total) - (int(total) * 0.05)
            grand_total = int(additional_discount) + (int(total) * 0.1)
            print("TOTAL_AMOUNT_TO_PAY %.2f" % grand_total)

        else:
            sub_discount = int(tshirt_discount) + int(jacket_discount) + int(cap_discount) + int(notebook_discount) + int(pens_discount) + int(markers_discount)
            total_discount = int(sub_total) - int(sub_discount)
            print("TOTAL_DISCOUNT %.2f" % total_discount)
            total = int(sub_total) - int(total_discount)
            grand_total = int(total) + (int(total) * 0.1)
            print("TOTAL_AMOUNT_TO_PAY %.2f" % grand_total)

    else:
        print("TOTAL_DISCOUNT 0.00")
        total = int(sub_total)
        print("TOTAL_AMOUNT_TO_PAY %.2f" % total)

for line in lines:
    all_lines = line.split(" ",2)
    if all_lines[0] == "ADD_ITEM":
        ADD_ITEM(all_lines[1],all_lines[2])
    elif all_lines[0] == "PRINT_BILL":
        PRINT_BILL()