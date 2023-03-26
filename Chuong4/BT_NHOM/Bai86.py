from Bai85 import sodoi

def display_verse(ngay):
    print(f"On the {sodoi(ngay)} day of Christmas")
    print("my true love sent to me:")
    if ngay >= 12:
        print("Twelve drummers drumming,")
    if ngay >= 11:
        print("Eleven pipers piping,")
    if ngay >= 10:
        print("Ten lords a-leaping,")
    if ngay >= 9:
        print("Nine ladies dancing,")
    if ngay >= 8:
        print("Eight maids a-milking,")
    if ngay >= 7:
        print("Seven swans a-swimming,")
    if ngay >= 6:
        print("Six geese a-laying,")
    if ngay >= 5:
        print("Five golden rings,")
    if ngay >= 4:
        print("Four calling birds,")
    if ngay >= 3:
        print("Three French hens,")
    if ngay >= 2:
        print("Two turtle doves,")
    if ngay == 1:
        print("A partridge in a pear tree.")
    else:
        print("And a partridge in a pear tree.")

if __name__ == '__main__':
    for i in range(1, 13):
        display_verse(i)
        print()