def field(data, *args):
    for item in data:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {key: item.get(key) for key in args if item.get(key) is not None}
            if result:
                yield result

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))

if __name__ == '__main__':
    main()
