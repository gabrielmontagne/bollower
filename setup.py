from setuptools import setup

setup(
    name='bollower',
    author='Gabriel Montagné Láscaris-Comneno',
    author_email='gabriel@tibas.london',
    license='MIT',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'bollower = bollower.__main__:main'
        ]
    }
)
