from setuptools import setup

tool_map = {
    'fpdb': 'git+https://github.com/ra101/fpdb.git',
}

setup(
    name='ratools',
    license='MIT',
    dependency_links = list(tool_map.values()),
    install_requires = [
        f'{tool} @ {url}' for tool, url in tool_map.items()
    ],
)

