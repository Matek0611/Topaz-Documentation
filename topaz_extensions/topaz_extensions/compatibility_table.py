import json
from html import escape
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from xml.etree import ElementTree as etree

'''
Format:
{{{compatibility:

}}}
'''

class CompatibilityBlockProcessor(BlockProcessor):
    def test(self, parent, block):
        return block.startswith('{{{compatibility:')
    
    def generate_legend(self, element: etree.Element):
        container = etree.SubElement(element, 'div', {'class': 'compat-table-legend'})
        items = [
            ('check-circle', 'Full support.'),
            ('skip', 'Partial support.'),
            ('x-circle', 'No support.'),
            ('no-entry', 'Deprecated. Do not use in new scripts.'),
            ('issue-opened', 'Experimental. Expect behavior to change in the future.'),
            ('kebab-horizontal', 'See implementation notes.')
        ]

        for item in items:
            citem = etree.SubElement(container, 'div', {'class': 'compat-table-legend-item'})
            etree.SubElement(citem, 'img', {'src': 'assets/images/octicons/' + item[0] + '-16.svg', 'class': 'compat-table-icon'})
            etree.SubElement(citem, 'span').text = item[1]

    def run(self, parent, blocks):
        block = blocks.pop(0)

        lines = block.splitlines()
        json_lines = []

        for line in lines[1:]:
            if line.strip() == '}}}':
                break
            json_lines.append(line)

        raw_json = '\n'.join(json_lines)

        try:
            data = json.loads(raw_json)
        except json.JSONDecodeError as e:
            pre = etree.SubElement(parent, 'pre')
            pre.text = f'Invalid compatibility JSON: {e}'
            return

        table = etree.SubElement(parent, 'table')
        table.set('class', 'compat-table')

        thead = etree.SubElement(table, 'thead')
        tr = etree.SubElement(thead, 'tr')

        etree.SubElement(tr, 'th').text = 'Browser'
        etree.SubElement(tr, 'th').text = 'Support'

        tbody = etree.SubElement(table, 'tbody')

        for browser, info in data.items():
            tr = etree.SubElement(tbody, 'tr')

            etree.SubElement(tr, 'th').text = browser.capitalize()

            support = info.get('version_added', '—')

            td = etree.SubElement(tr, 'td')
            if support is False:
                td.text = '❌'
            elif support is True:
                td.text = '✔️'
            else:
                td.text = escape(str(support))

        self.generate_legend(parent)


class ZensicalCompatibilityTableExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(
            CompatibilityBlockProcessor(md.parser),
            'compatibility_table',
            priority=175
        )


def makeExtension(**kwargs):
    return ZensicalCompatibilityTableExtension(**kwargs)
