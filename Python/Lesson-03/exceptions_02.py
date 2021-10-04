from exceptions import divid_two

try:
    divid_two(10,'0')
except TypeError:
    print('Type error')
except ZeroDivisionError:
    print('ZeroDivisionError')
except BaseException:
    print(e)
finally:
    print('On finally')

