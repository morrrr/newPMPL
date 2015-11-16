from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_lists_items(self):
        self.fail('write me!')
