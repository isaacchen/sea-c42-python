#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, content='', name='html', indent_level=0):
        self.content = content
        self.name = name
        self.indent_level = indent_level
        # you can define attribute without reference in__init__
        self.children = [content] if content else []

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, outfile, content=''):
        tag_indent = '    ' * self.indent_level
        txt_indent = '    ' * (self.indent_level + 1)

        if (self.name == 'html'):
            outfile.write('<%s>\n' % self.name)
        else:
            outfile.write(('%s<%s>\n') % (tag_indent, self.name))

        for child in self.children:
            if (type(child) == str):
                # print content string
                outfile.write(txt_indent + child + '\n')
            else:
                # recursively render new child node
                child.render(outfile, txt_indent)

        if (self.name == 'html'):
            outfile.write('</%s>' % self.name)
        else:
            outfile.write(('%s</%s>\n') % (tag_indent, self.name))

    def OneLineTag(self, outfile, content, name='', indent_level=0):
        tag_indent = '    ' * indent_level
        oneline = '%s<%s>%s</%s>\n' % (tag_indent, name, self.content, name)
        outfile.write(oneline)


class Html(Element):
    def __init__(self, content='', name='', indent_level=0):
        Element.__init__(self, content='', name='html', indent_level=0)

    def render(self, outfile, content=''):
        outfile.write('<!DOCTYPE html>\n')
        Element.render(self, outfile, '')


class Body(Element):
    def __init__(self, content='', name='', indent_level=0):
        Element.__init__(self, content='', name='body', indent_level=1)


class P(Element):
    def __init__(self, content, name='', indent_level=0):
        Element.__init__(self, content, name='p', indent_level=2)


class Head(Element):
    def __init__(self, content='', name='', indent_level=0):
        Element.__init__(self, content='', name='head', indent_level=1)


class Title(Element):
    def __init__(self, content, name='', indent_level=0):
        Element.__init__(self, content, name='title', indent_level=2)

    def render(self, outfile, content, name='', indent_level=0):
        Element.OneLineTag(self, outfile, self.content, name='title',
                           indent_level=self.indent_level)
