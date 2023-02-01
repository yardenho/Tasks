def priceCheck(products, productPrices, productSold, soldPrice):
    error = 0
    for index, prod in enumerate(productSold):
        if productPrices[products.index(prod)] != soldPrice[index]:
            error += 1
    return error


def priceCheckTest():

    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese']
    soldPrice = [18.99, 400.89]
    print(priceCheck(products, productPrices, productSold, soldPrice))

    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    print(priceCheck(products, productPrices, productSold, soldPrice))