def triangle(rows):
    if rows <= 1:
        return rows
    return rows + triangle(rows - 1)

print(triangle(2)==3)
print(triangle(3)==6)
print(triangle(5)==15)
