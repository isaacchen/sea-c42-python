#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, content='', name='html', indent_level=0, **kwargs):
        self.content = content
        self.name = name
        self.indent_level = indent_level
        self.attributes = kwargs
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
            if (len(self.attributes) != 0):
                for k, v in self.attributes.items():
                    outfile.write('%s<%s %s="%s">\n' %
                                  (tag_indent, self.name, k, v))
            else:
                outfile.write('%s<%s>\n' % (tag_indent, self.name))

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


class Html(Element):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, '', 'html', 0, **kwargs)

    def render(self, outfile, content=''):
        outfile.write('<!DOCTYPE html>\n')
        Element.render(self, outfile, '')


class Body(Element):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, '', 'body', 1, **kwargs)


class P(Element):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, content, 'p', 2, **kwargs)


class Head(Element):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, '', 'head', 1, **kwargs)


class OneLineTag(Element):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, content, name, 0, **kwargs)

    def render(self, outfile, content, name='', indent_level=0):
        tag_indent = '    ' * self.indent_level
        oneline = '%s<%s>%s</%s>\n' % (tag_indent, self.name,
                                       self.content, self.name)
        outfile.write(oneline)


class Title(OneLineTag):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, content, 'title', 2, **kwargs)


class SelfClosingTag(Element):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, '', name, 0, **kwargs)

    def render(self, outfile, name='', indent_level=0):
        tag_indent = '    ' * self.indent_level
        tagline = '%s<%s />\n' % (tag_indent, self.name)
        outfile.write(tagline)


class Hr(SelfClosingTag):
    def __init__(self, content='', name='', indent_level=0, **kwargs):
        Element.__init__(self, '', 'hr', 2, **kwargs)
