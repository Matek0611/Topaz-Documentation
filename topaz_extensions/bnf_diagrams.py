import re
import html
import io
import uuid
import railroad
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

try:
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import HtmlFormatter

    def highlight_ebnf_code(code_text: str) -> str:
        try:
            lexer = get_lexer_by_name("ebnf")
        except Exception:
            try:
                lexer = get_lexer_by_name("bnf")
            except Exception:
                lexer = None
        if lexer:
            return highlight(code_text, lexer, HtmlFormatter(nowrap=True))
        return html.escape(code_text)
except Exception:
    def highlight_ebnf_code(code_text: str) -> str:
        return html.escape(code_text)


TOKEN_SPEC = [
    ('COMMENT',     r'\(\*.*?\*\)'),
    ('STRING',      r'"[^"]*"|\'[^\']*\''),
    ('ASSIGN',      r'::=|:=|=|:'),
    ('SEMI',        r';'),
    ('BAR',         r'\||/'),
    ('LPAREN',      r'\('),
    ('RPAREN',      r'\)'),
    ('LBRACK',      r'\['),
    ('RBRACK',      r'\]'),
    ('LBRACE',      r'\{'),
    ('RBRACE',      r'\}'),
    ('OP_OPT',      r'\?'),
    ('OP_ZERO',     r'\*'),
    ('OP_ONE',      r'\+'),
    ('IDENT',       r'<[a-zA-Z0-9_\-\s]+>|[a-zA-Z_][a-zA-Z0-9_\-]*'),
    ('WS',          r'\s+'),
    ('MISC',        r'.'),
]

TOKEN_REGEX = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC), re.DOTALL)

railroad.ARCRADIUS = 4
railroad.VS = 12
railroad.HS = 10

ICON_SCHEMA = '<svg class="bnf-icon" viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M22 11V3h-7v3H9V3H2v8h7V8h2v10h4v3h7v-8h-7v3h-2V8h2v3h7zM7 9H4V5h3v4zm10-4h3v4h-3V5zm3 14h-3v-4h3v4z"/></svg>'
ICON_CODE = '<svg class="bnf-icon" viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>'


def make_optional(item):
    opt = railroad.Optional(item)
    orig_format = opt.format

    def custom_format(*args, **kwargs):
        res = orig_format(*args, **kwargs)
        g = railroad.DiagramItem('g', attrs={'class': 'optional-branch'})
        g.children.append(res)
        return g

    opt.format = custom_format
    return opt


def inject_arrows_to_svg(svg_code: str) -> str:
    path_matches = list(re.finditer(r'<path\s+[^>]*d="([^"]+)"', svg_code))
    arrow_paths = []

    for pm in path_matches:
        if 'bnf-arrow' in pm.group(0):
            continue

        d_str = pm.group(1)
        commands = re.findall(r'([a-zA-Z])\s*([^a-zA-Z]*)', d_str)
        curr_x, curr_y = 0.0, 0.0

        for cmd, args in commands:
            nums = [float(n) for n in re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', args)]

            if cmd == 'M' and len(nums) >= 2:
                curr_x, curr_y = nums[0], nums[1]
            elif cmd == 'm' and len(nums) >= 2:
                curr_x += nums[0]
                curr_y += nums[1]
            elif cmd == 'h' and len(nums) >= 1:
                for dx in nums:
                    if abs(dx) >= 8:
                        mx = round(curr_x + dx / 2.0, 2)
                        my = round(curr_y, 2)
                        # dx > 0: ścieżka w prawo (->), dx < 0: ścieżka powrotna w pętli w lewo (<-)
                        if dx > 0:
                            arrow_paths.append(
                                f'<path class="bnf-arrow-head" d="M {mx-4.5} {my-3.5} L {mx+4.5} {my} L {mx-4.5} {my+3.5} z" />'
                            )
                        else:
                            arrow_paths.append(
                                f'<path class="bnf-arrow-head" d="M {mx+4.5} {my-3.5} L {mx-4.5} {my} L {mx+4.5} {my+3.5} z" />'
                            )
                    curr_x += dx
            elif cmd == 'H' and len(nums) >= 1:
                for tx in nums:
                    dx = tx - curr_x
                    if abs(dx) >= 8:
                        mx = round(curr_x + dx / 2.0, 2)
                        my = round(curr_y, 2)
                        if dx > 0:
                            arrow_paths.append(
                                f'<path class="bnf-arrow-head" d="M {mx-4.5} {my-3.5} L {mx+4.5} {my} L {mx-4.5} {my+3.5} z" />'
                            )
                        else:
                            arrow_paths.append(
                                f'<path class="bnf-arrow-head" d="M {mx+4.5} {my-3.5} L {mx-4.5} {my} L {mx+4.5} {my+3.5} z" />'
                            )
                    curr_x = tx
            elif cmd == 'v' and len(nums) >= 1:
                for dy in nums:
                    curr_y += dy
            elif cmd == 'V' and len(nums) >= 1:
                for ty in nums:
                    curr_y = ty
            elif cmd == 'l' and len(nums) >= 2:
                for i in range(0, len(nums) - 1, 2):
                    curr_x += nums[i]
                    curr_y += nums[i + 1]
            elif cmd == 'L' and len(nums) >= 2:
                for i in range(0, len(nums) - 1, 2):
                    curr_x = nums[i]
                    curr_y = nums[i + 1]
            elif cmd == 'a':
                for i in range(0, len(nums) - 6, 7):
                    curr_x += nums[i + 5]
                    curr_y += nums[i + 6]
            elif cmd == 'A':
                for i in range(0, len(nums) - 6, 7):
                    curr_x = nums[i + 5]
                    curr_y = nums[i + 6]

    if arrow_paths and '</svg>' in svg_code:
        arrows_group = f'<g class="bnf-arrows">{"".join(arrow_paths)}</g></svg>'
        svg_code = svg_code.replace('</svg>', arrows_group, 1)

    return svg_code


def tokenize_ebnf(text):
    tokens = []
    for match in TOKEN_REGEX.finditer(text):
        kind = match.lastgroup
        val = match.group()
        if kind in ('WS', 'COMMENT', 'MISC'):
            continue
        tokens.append((kind, val))
    return tokens


class EbnfParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def get(self):
        tok = self.peek()
        if tok[0] is not None:
            self.pos += 1
        return tok

    def match(self, kind):
        if self.peek()[0] == kind:
            return self.get()
        return None

    def is_start_of_rule(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'IDENT':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'ASSIGN':
                return True
        return False

    def parse_rules(self):
        rules = []
        while self.peek()[0] is not None:
            rule = self.parse_rule()
            if rule:
                rules.append(rule)
            else:
                raise ValueError("Error parsing EBNF rule.")
        return rules

    def parse_rule(self):
        if self.peek()[0] != 'IDENT':
            return None

        start_pos = self.pos
        lhs_val = self.get()[1].strip('<>').strip()

        if not self.match('ASSIGN'):
            return None

        rhs_expr = self.parse_expression()
        self.match('SEMI')

        raw_tokens = [t[1] for t in self.tokens[start_pos:self.pos]]
        raw_code = " ".join(raw_tokens)

        return (lhs_val, rhs_expr, raw_code)

    def parse_expression(self):
        terms = [self.parse_term()]
        while self.match('BAR'):
            terms.append(self.parse_term())

        if len(terms) == 1:
            return terms[0]
        return railroad.Choice(0, *terms)

    def parse_term(self):
        factors = []
        while True:
            if self.is_start_of_rule():
                break
            kind = self.peek()[0]
            if kind in ('STRING', 'IDENT', 'LPAREN', 'LBRACK', 'LBRACE'):
                factors.append(self.parse_factor())
            else:
                break

        if not factors:
            return railroad.Terminal('')
        if len(factors) == 1:
            return factors[0]
        return railroad.Sequence(*factors)

    def parse_factor(self):
        primary = self.parse_primary()

        if self.match('OP_OPT'):
            return make_optional(primary)
        elif self.match('OP_ZERO'):
            return railroad.ZeroOrMore(primary)
        elif self.match('OP_ONE'):
            return railroad.OneOrMore(primary)

        return primary

    def parse_primary(self):
        kind, val = self.peek()

        if kind == 'STRING':
            self.get()
            return railroad.Terminal(val[1:-1])

        elif kind == 'IDENT':
            self.get()
            return railroad.NonTerminal(val.strip('<>').strip())

        elif kind == 'LPAREN':
            self.get()
            expr = self.parse_expression()
            self.match('RPAREN')
            return expr

        elif kind == 'LBRACK':
            self.get()
            expr = self.parse_expression()
            self.match('RBRACK')
            return make_optional(expr)

        elif kind == 'LBRACE':
            self.get()
            expr = self.parse_expression()
            self.match('RBRACE')
            return railroad.ZeroOrMore(expr)

        return railroad.Terminal(val or '')


def convert_bnf_to_svg(ebnf_code: str) -> str:
    tokens = tokenize_ebnf(ebnf_code)
    parser = EbnfParser(tokens)
    rules = parser.parse_rules()

    if not rules:
        raise ValueError("No valid EBNF rules found.")

    output_html = []
    for lhs_name, diagram_element, raw_code in rules:
        rule_id = uuid.uuid4().hex[:8]
        diagram = railroad.Diagram(diagram_element)
        svg_buffer = io.StringIO()
        diagram.writeSvg(svg_buffer.write)
        svg_code = svg_buffer.getvalue()

        svg_code = inject_arrows_to_svg(svg_code)
        highlighted_code = highlight_ebnf_code(raw_code)

        output_html.append(f'''
<div class="bnf-rule-card">
  <input type="radio" id="schema-{rule_id}" name="toggle-{rule_id}" class="bnf-radio-schema" checked>
  <input type="radio" id="code-{rule_id}" name="toggle-{rule_id}" class="bnf-radio-code">
  
  <div class="bnf-rule-header">
    <span class="bnf-title">{html.escape(lhs_name)}</span>
    <div class="bnf-switch-labels">
      <label for="schema-{rule_id}" class="bnf-label-schema" title="Schema">{ICON_SCHEMA}</label>
      <label for="code-{rule_id}" class="bnf-label-code" title="EBNF">{ICON_CODE}</label>
    </div>
  </div>

  <div class="bnf-body bnf-body-schema">
    {svg_code}
  </div>
  <div class="bnf-body bnf-body-code">
    <pre class="highlight"><code class="language-ebnf">{highlighted_code}</code></pre>
  </div>
</div>
''')

    return "".join(output_html)


class BnfRailroadPreprocessor(Preprocessor):
    RE_BNF = re.compile(r'```(?:bnf|ebnf|railroad)[ \t]*\r?\n(.*?)\r?\n[ \t]*```', re.DOTALL)

    def run(self, lines):
        text = "\n".join(lines)

        def replace_match(match):
            code = match.group(1)
            try:
                svg_html = convert_bnf_to_svg(code)
                return f"\n\n{svg_html}\n\n"
            except Exception:
                return match.group(0)

        new_text = self.RE_BNF.sub(replace_match, text)
        return new_text.split("\n")


class BnfRailroadExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(BnfRailroadPreprocessor(md), 'bnf_diagrams_pre', 105)


def makeExtension(**kwargs):
    return BnfRailroadExtension(**kwargs)