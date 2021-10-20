import sys
import time


# http://ajennings.net/blog/a-million-digits-of-pi-in-9-lines-of-javascript.html
# https://math.tools/numbers/pi/1000000

def digits_of_pi(digits):
    c1 = 1
    c2 = 2
    c4 = 4
    c10 = 10

    i = c1
    x = 3 * c10.__pow__(digits + 20)
    pi = x

    while x > 0:
        x = (x * i) // ((i + c1) * c4)
        pi += (x // (i + c2))
        i += c2

    return f'{pi}'[1:digits + 1]


def format_digits(digits, space_freq, newline_freq):
    result = ''

    for i in range(0, len(digits)):
        result += digits[i]

        ordinal_pos = i + 1

        if ordinal_pos % newline_freq == 0:
            result += '\n'
        elif ordinal_pos % space_freq == 0:
            result += ' '

    return result.strip()


def main():
    if len(sys.argv) == 2:
        digits = int(sys.argv[1])

        print('\nCalculating π to {:,d} digits\n'.format(digits))

        start = time.time()

        result = f'{digits_of_pi(digits)}'
        result = format_digits(result, 10, 100)

        elapsed_time = round(time.time() - start)

        print(f'π = 3.\n{result}')

        print('\nElapsed Time: {:,d} seconds'.format(elapsed_time))
    else:
        print('usage: {digits}')


main()
