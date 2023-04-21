def rle_encode(data):
    data = iter(data)
    try: 
        last_datum = next(data)
        counter = 1
        for datum in data:
            if last_datum == datum:
                counter += 1
            else:
                yield (last_datum, counter)
                last_datum = datum
                counter = 1
        yield (last_datum, counter)
    except StopIteration:
        pass
    
    
def rle_decode(data):
    for datum, count in data:
        for _ in range(count):
            yield datum
