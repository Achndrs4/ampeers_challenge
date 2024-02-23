def transform_dictionary(input_dictionary: dict) -> None:
    # in-place transformation of dictionary so we don't have to copy the dict
    for key, value in input_dictionary.items():
        if isinstance(value, int):
            input_dictionary[key] = value + 1
        elif isinstance(value, float):
            input_dictionary[key] = round(value + 1, 8)
        elif isinstance(value, str):
            input_dictionary[key] = value + ' AE'
            