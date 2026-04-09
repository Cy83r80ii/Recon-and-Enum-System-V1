def remove_duplicates(items):

    seen = set()
    result = []

    for item in items:

        # case 1: string (URLs)
        if isinstance(item, str):

            if item not in seen:
                seen.add(item)
                result.append(item)

        # case 2: param object
        elif isinstance(item, dict):

            key = f"{item.get('url')}::{item.get('param')}"

            if key not in seen:
                seen.add(key)
                result.append(item)

    return result
