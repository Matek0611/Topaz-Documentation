import json
from html import escape
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from xml.etree import ElementTree as etree
import topaz_extensions.icons as icons

'''
Format:
{{{compatibility:
{
    "Windows": [
        {"feature": "x", "support": "full", "version": "10", "timeline": [] }
    ],
    "macOS": [...],
    "Linux": [...],...
}
}}}
'''

class CompatibilityBlockProcessor(BlockProcessor):
    def test(self, parent, block):
        return block.startswith('{{{compatibility:')
    
    def generate_legend(self, element: etree.Element):
        container = etree.SubElement(element, 'div', {'class': 'compat-table-legend'})
        items = [
            (icons.ICON_FULL_COMPATIBILITY, 'Full support.'),
            (icons.ICON_PARTIAL_COMPATIBILITY, 'Partial support.'),
            (icons.ICON_NO_COMPATIBILITY, 'No support.'),
            (icons.ICON_DEPRECATED, 'Deprecated. Do not use in new scripts.'),
            (icons.ICON_EXPERIMENTAL, 'Experimental. Expect behavior to change in the future.'),
            (icons.ICON_DOTS, 'See implementation notes.')
        ]

        for item in items:
            citem = etree.SubElement(container, 'div', {'class': 'compat-table-legend-item'})
            etree.SubElement(citem, 'div', {'class': 'compat-table-icon'}).text = item[0]
            etree.SubElement(citem, 'span').text = item[1]

    def run(self, parent, blocks):
        etree.SubElement(parent, 'h2').text = 'Operating system compatibility'

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
            pre = etree.SubElement(parent, 'em')
            pre.text = f'Invalid compatibility JSON: {e}'
            return

        table = etree.SubElement(etree.SubElement(parent, 'div', {'class': 'compat-block'}), 'table', {'class': 'compat-table'})
        thead = etree.SubElement(table, 'thead')
        tbody = etree.SubElement(table, 'tbody')
        trhead = etree.SubElement(thead, 'tr')
        etree.SubElement(trhead, 'th')

        for system in data.keys():
            thsystem = etree.SubElement(trhead, 'th', {'class': 'compat-table-system'})
            etree.SubElement(thsystem, 'span').text = system

        fresult = {
            feature: {
                os_name: {k: v for k, v in f.items() if k != "feature"}
                for os_name, features in data.items()
                for f in features
                if f["feature"] == feature
            }
            for feature in {f["feature"] for features in data.values() for f in features}
        }

        for fname, fvalue in fresult.items():
            trbody = etree.SubElement(tbody, 'tr')
            tdinfo = etree.SubElement(trbody, 'td')
            tdinfo.text = fname

            for system in data.keys():
                tdinfo = etree.SubElement(trbody, 'td')

                if system not in fvalue.keys():
                    tdinfo.text = 'none'
                    continue

                tdinfo.text = 'x'

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
