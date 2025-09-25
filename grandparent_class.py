class Grandparent:
    def grandparent_info(self):
        print("I am the grandparent")
class Parent(Grandparent):
    def parent_info(self):
        print("I am the parent")
class Child(Parent):
    def child_info(self):
        print("I am the child")
child_obj = Child()
child_obj.grandparent_info()
child_obj.parent_info()
child_obj.child_info()