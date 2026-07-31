"""main"""
def main():
    """mama"""
    text_a = input().lower()
    for x in "aeiou":
        count = text_a.count(x)
        if count > 0:
            print(f'{x} : {count}')
main()
