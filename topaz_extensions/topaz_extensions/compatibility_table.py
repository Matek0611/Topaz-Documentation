import json
from html import escape
import uuid
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor
from xml.etree import ElementTree as etree
import topaz_extensions.icons as icons

'''
Format:
{{{compatibility:
{
    "Windows": [
        {"feature": "x", "support": "full", "version": "10", "timeline": [[true, "x", "2025"]] }
    ],
    "macOS": [...],
    "Linux": [...],...
}
}}}
'''

class CompatibilityBlockProcessor(BlockProcessor):
    def test(self, parent, block):
        return block.startswith('{{{compatibility:')
    
    def get_raw_json(self, blocks):
        block = blocks.pop(0)

        lines = block.splitlines()
        json_lines = []

        for line in lines[1:]:
            if line.strip() == '}}}':
                break
            json_lines.append(line)

        return '\n'.join(json_lines)
    
    def generate_compat_item(self, global_parent, parent, feature, system, icon, title, add_more, color_class):
        parent.set('class', color_class)
        compat_item = etree.SubElement(parent, 'div', {'class': 'compat-table-item'})
        
        etree.SubElement(compat_item, 'span').text = icon

        if title:
            etree.SubElement(compat_item, 'span').text = title
        if add_more:
            id = f'dg{uuid.uuid1().hex}'
            dialog = etree.SubElement(global_parent, 'dialog', {'id': id, 'class': 'compat-dialog'})
            top_bar = etree.SubElement(dialog, 'div', {'class': 'compat-dialog-topbar'})

            if feature and system:
                etree.SubElement(top_bar, 'h1', {'title': f'{feature} ({system})'}).text = f'{feature} (<em>{system}</em>)'

            etree.SubElement(top_bar, 'form', {'method': 'dialog'}).text = '<button class="dialog-close">&times;</button>'

            timeline_dl = etree.SubElement(etree.SubElement(dialog, 'div'), 'dl')
            for part in add_more:
                tdt = etree.SubElement(timeline_dl, 'dt', {'class': 'compat-table-dt'})
                etree.SubElement(tdt, 'div').text = icons.ICON_DISC if part[0] else icons.ICON_SEMI_DISC
                etree.SubElement(tdt, 'span').text = (f'<strong>{part[2]}</strong><br>' if part[2] else '') + part[1]

            morebtn = etree.SubElement(compat_item, 'span', {'style': 'color: #555; cursor: pointer;', 'onclick': f'document.getElementById("{id}").showModal()'})
            morebtn.text = icons.ICON_DOTS
    
    def generate_table(self, parent, data):
        global_parent = etree.SubElement(parent, 'div')
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
                    self.generate_compat_item(global_parent, tdinfo, fname, system, icons.ICON_NO_COMPATIBILITY, 'No', False, 'compat-no-support')
                    continue

                fivalue = fvalue[system]

                match fivalue.get('support', ''):
                    case 'full': 
                        self.generate_compat_item(global_parent, tdinfo, fname, system, icons.ICON_FULL_COMPATIBILITY, fivalue.get('version', 'Yes'), fivalue.get('timeline', ''), 'compat-supported')
                    case 'partial':
                        self.generate_compat_item(global_parent, tdinfo, fname, system, icons.ICON_PARTIAL_COMPATIBILITY, fivalue.get('version', 'Partial'), fivalue.get('timeline', ''), 'compat-partial-support')
                    case 'deprecated':
                        self.generate_compat_item(global_parent, tdinfo, fname, system, icons.ICON_DEPRECATED, fivalue.get('version', 'Obsolete'), fivalue.get('timeline', ''), 'compat-deprecated')
                    case 'experimental':
                        self.generate_compat_item(global_parent, tdinfo, fname, system, icons.ICON_EXPERIMENTAL, fivalue.get('version', 'New'), fivalue.get('timeline', ''), 'compat-experimental')
                    case _:
                        self.generate_compat_item(global_parent, tdinfo, fname, system, icons.ICON_NO_COMPATIBILITY, fivalue.get('version', 'No'), fivalue.get('timeline', ''), 'compat-no-support')
    
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

        try:
            data = json.loads(self.get_raw_json(blocks))
        except json.JSONDecodeError as e:
            info = etree.SubElement(parent, 'em')
            info.text = f'Invalid compatibility JSON data ({e}).'
            return

        self.generate_table(parent, data)
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
