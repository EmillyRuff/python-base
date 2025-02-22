#!usr/bin/env python3

import sys
import os

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)


try:
    names = open("names.txt").readlines()

except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry

except ZeroDivisionError:
    print("[Error] You cant divide by zero!!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn't have banana")
    sys.exit(1)

else:
    print("Sucesso!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
