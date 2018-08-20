'''collection of custom jinja extensions for spinnaker pipelines'''
from jinja2.ext import Extension
from jinja2 import nodes

#http://jinja.pocoo.org/docs/2.10/extensions/#module-jinja2.ext

class Pipeline(Extension):
    # a set of names that trigger the extension.
    tags = set(['module'])

    def parse(self, parser):
        # the first token is the token that started the tag.  In our case
        # we only listen to ``'cache'`` so this will be a name token with
        # `module` as value.  We get the line number so that we can give
        # that line number to the nodes we create by hand.
        lineno = next(parser.stream).lineno

        args = [parser.parse_expression()]

        nodes.Const(None)
