import unittest
from lib.utility import Utility

class Test_validate_instance_of(unittest.TestCase):
    
    def validate_instance_of_test_single_class(self):
        class A: pass
        class B: pass
        a = A()

        Utility.validate_instance_of(a, A)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(a, B)

    def validate_instance_of_test_tuple_of_classes(self):
        class A: pass
        class B: pass
        class C: pass
        a = A()

        Utility.validate_instance_of(a, (A, B))  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(a, (B, C))

    def validate_instance_of_test_primitive_types(self):
        Utility.validate_instance_of(1, int)  # Should not raise an exception
        Utility.validate_instance_of("hello", str)  # Should not raise an exception
        Utility.validate_instance_of(True, bool)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(1, float)

    def validate_instance_of_test_inheritance(self):
        class A: pass
        class B(A): pass
        b = B()

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(b, A)

    def validate_instance_of_test_multiple_inheritance(self):
        class A: pass
        class B: pass
        class C(A, B): pass
        c = C()

        Utility.validate_instance_of(c, C)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(c, (A, B))

    def validate_instance_of_test_edge_case_empty_tuple(self):
        class A: pass
        a = A()

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(a, ())

    def validate_instance_of_test_edge_case_none_type(self):
        with self.assertRaises(TypeError):
            Utility.validate_instance_of(None, int)
    
    def test_nested_classes(self):
        class A:
            class B: pass
        a = A()
        b = A.B()

        Utility.validate_instance_of(b, A.B)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(b, A)

    def test_class_itself_as_object(self):
        class A: pass
        class B: pass

        Utility.validate_instance_of(A, type)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(A, B)

    def test_callable_objects(self):
        def func(): pass
        class A: pass

        Utility.validate_instance_of(func, type(func))  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_instance_of(func, A)
