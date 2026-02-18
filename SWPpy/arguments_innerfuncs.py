'''
Outer Func: create_processor
 - fix arg. base_multiplier (number)
 - *args strings as filter-keywords
 - **kwargs as standard transformation - prefix="LOG: "
 - inner func process_data --> Closure-Concept

Inner Func: process_data
 - *args 
 - 1. only data included in the 'filter-keywords' or numbers - FILTER
 - 2. if number -> multiply with base_multiplier - CALCULATION
 - 3. if string -> transformation from **kwargs - TRANSFORMATION
 - return list

Inner Helper Methode
 - within process_data a method _validate_item
 -> checks if a element should be allowed in the transform process
'''

def create_processor(nr, *filter_keywords: str, **transform):
    if isinstance(nr, (int, float)):
        def process_data(*data):
            transformed_list = []

            def _validate_item(item):
                if isinstance(item, (int, float)): return True
                if isinstance(item, str) and item in filter_keywords: return True
                return False

            for d in data:
                if _validate_item(d):
                    if isinstance(d, (int, float)):
                        transformed_list.append(d*nr)

                    else:
                        if transform is not None:
                            if len(transform.values()) >= 2:
                                vals = list(transform.values())
                                transf_str = f"{vals[0]} {d} {vals[1]}"
                            else:
                                val = list(transform.values())[0]
                                transf_str = f"{val} {d}"
                            transformed_list.append(transf_str)

                        else: transformed_list.append(d)

            return transformed_list
        return process_data
    else:
        raise TypeError(f"first param needs to be a number - no {type(nr).__name__}")

def main():
    # testing
    try:
        processor = create_processor(10, "error", "warning", prefix="[SYSTEM] ", suffix=" !!!")
        data = (5, "error", "info", 12, "warning", "debug")
        result = processor(*data)
        print(f"First test: {result}")
        processor2 = create_processor(0.5, "geometry", "monaco", param1="--> ")
        data2 = (3, "int", "monaco", "latex", 14, 20.5, "geometry")
        res2 = processor2(*data2)
        print(f"Second test: {res2}")
        processor3 = create_processor("top", "geometry", "monaco")
        res3 = processor3(*data2)
        print(f"Third test: {res3}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()