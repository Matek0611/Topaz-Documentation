import re

from pygments.lexer import RegexLexer, words, include, bygroups
from pygments.token import Comment, Keyword, Name, Number, String, Operator, Text


KEYWORDS = [
    'BEGIN', 'END', 'DIV', 'MOD', 'TYPE', 'SHL', 'SHR', 'NOT', 'IN', 'IS', 'AS',
    'AND', 'OR', 'OF', 'XOR', 'IF', 'THEN', 'FOR', 'WHILE', 'REPEAT', 'UNTIL',
    'DO', 'BREAK', 'CONTINUE', 'CASE', 'ARRAY', 'MAP',
    'VAR', 'VARARGS', 'CONST', 'FEATURE', 'COMPONENT',
    'SELF', 'VIA', 'RESULT', 'EXIT', 'FUNCTION', 'METHOD', 'OPERATOR',
    'CONSTRUCTOR', 'DESTRUCTOR', 'PROPERTY', 'GET', 'SET', 'PRIVATE', 'PUBLIC', 'USE',
    'PLATFORM', 'UNIMPLEMENTED', 'DEPRECATED', 'EXPERIMENTAL', 'MESSAGE',
    'EXTERNAL', 'RAISE', 'TRY', 'EXCEPT', 'FINALLY', 'STATIC', 'ASYNC',
    'INLINE', 'ABSTRACT', 'ELSE', 'ASM', 'ATTRIBUTE', 'YIELD', 'GENERATOR',
    'RECORD', 'UNION', 'MODULE', 'REF', 'MAPARGS', 'PACKAGE', 'TASK',
    'SYNCHRONIZED' 
]

INBUILT_TYPES = [
    'POINTER', 'TINYINTEGER', 'TINYNATURAL', 'SMALLINTEGER', 'SMALLNATURAL', 'INTEGER', 'NATURAL',
    'LONGINTEGER', 'LONGNATURAL', 'SINGLE', 'DOUBLE', 'CURRENCY', 'BOOLEAN', 'CHAR',
    'WIDECHAR', 'ANSISTRING', 'WIDESTRING', 'RAWBYTESTRING', 'UNICODESTRING',
    'CSTRING', 'CWIDESTRING', 'DELEGATE',
    'STRING', 'IOSTRING', 'UNICODECHAR',
    'OBJECT', 'AUTO', 'EXCEPTION', 'ATTRIBUTE', 
    'SYSTEM'
]

CONSTS = [
    'TRUE', 'FALSE', 'NIL'
]

PREPROCESSOR_KEYWORDS = [
    'IF', 'ELSE', 'END', 
    'DEF', 'DEFINE', 'NDEF', 'UNDEFINE',
    'VAL', 'VALUE',
    'WARN', 'WARNING',
    'FATAL', 'ERROR'
]


class TopazLexer(RegexLexer):
    name = 'Topaz'
    aliases = ['topaz', 'tpz']
    filenames = ['*.tpz', '*.tpk']
    flags = re.IGNORECASE | re.MULTILINE

    tokens = {
        'root': [
            # whitespaces 
            (r'\s+', Text),
            # single-line comments
            (r'//.*$', Comment.Single),
            # multi-line comments
            (r'\{\*\* ', Comment.Doc, 'doccomment'),
            (r'\{', Comment.Multiline, 'comment'),
            # preprocessor
            (r'\|', Comment.Preproc, 'preprocessor'),
            # func args
            (r'\b(function|method|constructor|destructor|operator|generator)\b(\s+)([^\W\d]\w*)(\s*)(\()', bygroups(Keyword.Reserved, Text, Name.Function, Text, Operator), 'func_args'),
            # strings
            (r'"', String, 'double_string'),
            (r"'", String, 'single_string'),
            # escaped keyword
            (r'&[^\W\d]\w*', Name),
            # keywords
            (words(KEYWORDS, suffix=r'\b'), Keyword.Reserved),
            # build-in types
            (words(INBUILT_TYPES, suffix=r'\b'), Keyword.Type),
            # consts
            (words(CONSTS, prefix=r'\b', suffix=r'\b'), Keyword.Constant),
            # attributes
            (r'(@[^\W\d]\w*)(\s*)(\()', bygroups(Name.Decorator, Text, Operator), 'attribute_args'),
            (r'@[^\W\d]\w*', Name.Decorator),
            # numbers
            (r'\$[0-9a-f]+(?:_[0-9a-f]+)*\b', Number.Hex),
            (r'%[01]+(?:_[01]+)*\b', Number.Bin),
            (r'&[0-7]+(?:_[0-7]+)*\b', Number.Oct),
            (r'\b\d+(?:_\d+)*\.\d+(?:_\d+)*(?:[eE][+-]?\d+(?:_\d+)*)?\b', Number.Float),
            (r'\b\d+(?:_\d+)*[eE][+-]?\d+(?:_\d+)*\b', Number.Float),
            (r'\b\d+(?:_\d+)*\b', Number.Integer),
            # operators
            (r'(=>|=|<>|><|:=|\+|-|\*{1,2}|/|<=|>=|<|>)', Operator),
            (r'[().,;:|]', Operator),
            (r'[}{]', Operator),
            # identifiers
            (r'[^\W\d]\w*', Name)
        ],
        'comment': [
            (r'\}', Comment.Multiline, '#pop'),
            (r'\{', Comment.Multiline, '#push'), 
            (r'[^{}]+', Comment.Multiline)
        ],
        'doccomment': [
            (r'\*\}', Comment.Doc, '#pop'),
            (r'[^*]+', Comment.Doc),
            (r'\*', Comment.Doc)
        ],
        'preprocessor': [
            (r'\|', Comment.Preproc, '#pop'),
            (words(PREPROCESSOR_KEYWORDS, prefix=r'\b', suffix=r'\b'), Comment.Preproc),
            (r'[^\W\d]\w*', Name.Constant),
            (r'[()]', Operator),
            (r'\s+', Text)
        ],
        'func_args': [
            (r'\)', Operator, '#pop'),
            (words(('REF', 'CONST'), prefix=r'\b', suffix=r'\b'), Keyword.Modifier),
            (r'\((?=[^)]*?\)\s*:)', Operator, 'param_group'),
            (r'([^\W\d]\w*)(\s*)(:)', bygroups(Name.Variable, Text, Operator)),
            include('root'),
        ],
        'param_group': [
            (r'\)', Operator, '#pop'), 
            (r'[^\W\d]\w*', Name.Variable),
            (r',', Operator),
            (r'\s+', Text),
            include('root'),
        ],
        'double_string': [
            (r'\$\{', String.Interpol, 'interpolation'),
            (r'"', String, '#pop'),
            (r'\\.', String),
            (r'[^"\$\\]+', String),
            (r'\$', String)
        ],
        'single_string': [
            (r"''", String),
            (r"'", String, '#pop'),
            (r"[^']+", String)
        ],
        'interpolation': [
            (r'\}', String.Interpol, '#pop'),
            include('root')
        ],
        'attribute_args': [
            (r'\)', Operator, '#pop'),
            (r'([^\W\d]\w*)(\s*)(:=)', bygroups(Name.Attribute, Text, Operator)),
            include('root')
        ]
    }

