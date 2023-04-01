import unittest
from lib.utility import Utility

class Test_validate_nullable_instance_of(unittest.TestCase):
    
    def test_single_class(self):
        class A: pass
        class B: pass
        a = A()

        Utility.validate_nullable_instance_of(a, A)  # Should not raise an exception
        Utility.validate_nullable_instance_of(None, A)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(a, B)

    def test_tuple_of_classes(self):
        class A: pass
        class B: pass
        class C: pass
        a = A()

        Utility.validate_nullable_instance_of(a, (A, B))  # Should not raise an exception
        Utility.validate_nullable_instance_of(None, (A, B))  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(a, (B, C))

    def test_primitive_types(self):
        Utility.validate_nullable_instance_of(1, int)  # Should not raise an exception
        Utility.validate_nullable_instance_of("hello", str)  # Should not raise an exception
        Utility.validate_nullable_instance_of(True, bool)  # Should not raise an exception
        Utility.validate_nullable_instance_of(None, int)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(1, float)

    def test_inheritance(self):
        class A: pass
        class B(A): pass
        b = B()

        Utility.validate_nullable_instance_of(None, A)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(b, A)

    def test_multiple_inheritance(self):
        class A: pass
        class B: pass
        class C(A, B): pass
        c = C()

        Utility.validate_nullable_instance_of(c, C)  # Should not raise an exception
        Utility.validate_nullable_instance_of(None, C)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(c, (A, B))

    def test_edge_case_empty_tuple(self):
        class A: pass
        a = A()

        Utility.validate_nullable_instance_of(None, ())  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(a, ())
    
    def test_nested_classes(self):
        class A:
            class B: pass
        a = A()
        b = A.B()

        Utility.validate_nullable_instance_of(b, A.B)  # Should not raise an exception
        Utility.validate_nullable_instance_of(None, A.B)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(b, A)

    def test_class_itself_as_object(self):
        class A: pass
        class B: pass

        Utility.validate_nullable_instance_of(A, type)  # Should not raise an exception
        Utility.validate_nullable_instance_of(None, type)  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(A, B)

    def test_callable_objects(self):
        def func(): pass
        class A: pass

        Utility.validate_nullable_instance_of(func, type(func))  # Should not raise an exception
        Utility.validate_nullable_instance_of(None, type(func))  # Should not raise an exception

        with self.assertRaises(TypeError):
            Utility.validate_nullable_instance_of(func, A)
