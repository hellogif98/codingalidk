class employee:
    # intiailizing (constructor)
    def _init_(self):
        print("employee created.")

    # deleting (destructor)
    def _del_(self):
        print("destructor called , employee deleted.")

obj = employee()
del obj