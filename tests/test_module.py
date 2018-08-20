import unittest
import jinja2_module

from jinja2 import Environment


class ModuleExtensionTestCase(unittest.TestCase):

    def test_module_with_variables(self):
        env = Environment(extensions=['jinja2_module.ModuleExtension'])
        template = env.from_string('''
        No Fault in my stars
        {% module "wait-stage.module", variables='testVar1=10,testVar2=cool' %}
        ''')

        print template.render()

    def test_only_module(self):
        env = Environment(extensions=['jinja2_module.ModuleExtension'])
        template = env.from_string('''
                No Fault in my stars
                {% module "wait-stage.module" %}
                ''')

