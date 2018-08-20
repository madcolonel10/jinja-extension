'''collection of custom jinja extensions for spinnaker pipelines'''
from jinja2.ext import Extension
from jinja2 import nodes


# http://jinja.pocoo.org/docs/2.10/extensions/#module-jinja2.ext
# for better understanding of jinja extension refer ^^

class ModuleExtension(Extension):
    """Fetch spinnaker pipeline stage module from central template repo
    Usage:
    1. Without passing any variables for wait-stage.module
    {% module 'wait-stage.module' %}
    2. Passing variables for wait-stage.module
    {% module 'wait-stage.module',variables='testVar1=10,testVar2=cool'}
    """
    # a set of names that trigger the extension.
    tags = set(['module'])

    def fetch_module(self, module_name, variables):

        stage_variables = variables.split(",")
        var_to_value = {}
        for v in stage_variables:
            var, var_value = v.split("=")
            var_to_value[var] = var_value
        print "module_name:" + module_name
        print var_to_value
        return "hello"

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        # assume first token is the stage module value
        args = [parser.parse_expression()]
        # check if we have a comma next
        if parser.stream.skip_if('comma'):
            # check if we have variables assignment
            if parser.stream.current.type == 'name':
                # returns the current token only if all goes well
                name = parser.stream.expect('name')
                if name.value == 'variables':
                    if parser.stream.skip_if('assign'):
                        args.append(parser.parse_expression())
                # if the name of variable is not "variables" ignore
                else:
                    if parser.stream.skip_if('assign'):
                        next(parser.stream)
                        args.append(nodes.Const(None))
        # if there is nothing after comma, variables is assigned to None, default variables will be used
        else:
            args.append(nodes.Const(None))

        call_method = self.call_method('fetch_module', args)

        return nodes.Output([call_method], lineno=lineno)
