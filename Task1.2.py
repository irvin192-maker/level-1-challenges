def compare(a, b):
    if a == 3 or b == 3:
        while True:
            sig = a + b
            s = str(sig)
            if str(3) in s:
                return True
            else:
                return False
