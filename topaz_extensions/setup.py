from setuptools import setup, find_packages

setup(
    name = 'topaz',
    packages = find_packages(),
    entry_points = {
        'pygments.lexers': [
            'topaz = topaz_extensions.topaz_lexer:TopazLexer',
            'tpz = topaz_extensions.topaz_lexer:TopazLexer'
        ]
    }
)