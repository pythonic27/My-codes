primero = 0
segundo = 1

print(0)
print(1)
for i in range(0,20):
    actual = primero + segundo
    primero = segundo
    segundo = actual
    print(actual)