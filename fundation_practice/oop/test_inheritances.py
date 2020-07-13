class A(object):
    m = 3
    def run(self):
        print("A run..")
    pass


class B(A):
    # m = 1
    def run(self):
        print("B run..")


b = B()
# b.m = 2

# def run():
#     print("outside func run...")
#
# b.run = run

# b.run()

print(b.m)