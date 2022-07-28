def insert_data(provider, data):
    result = provider.create()
    for x in data:
        result = provider.insert_value(result, x)
    return result
