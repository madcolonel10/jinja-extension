'''collection of custom jinja extensions for spinnaker pipelines'''
from jinja2.ext import Extension


class Pipeline(Extension):
    tags = set(['module'])

    def parse(self, parser):
        pass
