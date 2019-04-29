from expects import *

list1 = [1, 2, 3, 4, 5]
list3 = [3, 2, 1]

def get_product(input_list):
    product = 1
    plist = []
    for num in input_list:
        product = product * num
    for i in range(len(input_list)):
        plist.append(product)
    for i in range(len(plist)):
        plist[i] = plist[i]/input_list[i]
    return plist

def get_product_no_division(input_list):
    plist = []
    for i in range(len(input_list)):
        product = 1
        for j in range(len(input_list)):
            if (j != i):
                product = product * input_list[j]
        plist.append(product)
    return plist

expect(get_product(list1)).to(equal([120, 60, 40, 30, 24]))
expect(get_product(list3)).to(equal([2, 3, 6]))
expect(get_product_no_division(list1)).to(equal([120, 60, 40, 30, 24]))
expect(get_product_no_division(list3)).to(equal([2, 3, 6]))
