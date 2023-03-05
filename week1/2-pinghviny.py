pinghvin = \
    "   _~_    \n" + \
    "  (o o)   \n" + \
    " /  V  \  \n" + \
    "/(  _  )\ \n" + \
    "  ^^ ^^   \n"

lines = pinghvin.splitlines(keepends=False)
n = int(input())
for line in lines:
    print(line * n)
