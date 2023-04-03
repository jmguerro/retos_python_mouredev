class Fizzbuzz:

    @staticmethod
    def fizz_values():
        for x in range(0, 101):
            if x % 3 and x % 5:
                print(x.__str__() + " fizzbuzz")
            elif x % 3:
                print(x.__str__() + " buzz")
            else:
                print(x.__str__() + " fizz")

    def fizz_with_param(i):
        if i % 3 and i % 5:
            return "fizzbuzz"
        elif i % 3:
            return "buzz"
        else:
            return "fizz"
