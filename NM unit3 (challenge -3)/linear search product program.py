def linear_search_product(product_list, target_product):
    indices = []

    
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)

    return indices


products = ["python", "java", "python", "c++", "linux", "python"]
target = "python"
result = linear_search_product(products, target)
if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")
