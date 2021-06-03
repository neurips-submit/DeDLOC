import codecs
import glob
import hashlib
import os
import re
import shlex
import subprocess
import tarfile
import tempfile
import urllib.request

from packaging import version
from pkg_resources import parse_requirements
from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install


P2PD_VERSION = 'v0.3.1'
P2PD_CHECKSUM = '8810097959db720208cdc9f2945804a4'
LIBP2P_TAR_URL = 'https://github.com/libp2p/go-libp2p-daemon/archive/2a7b233.tar.gz'


here = os.path.abspath(os.path.dirname(__file__))


def proto_compile(output_path):
    import grpc_tools.protoc

    cli_args = ['grpc_tools.protoc',
                '--proto_path=src/proto', f'--python_out={output_path}',
                f'--grpc_python_out={output_path}'] + glob.glob('src/proto/*.proto')

    code = grpc_tools.protoc.main(cli_args)
    if code:  # hint: if you get this error in jupyter, run in console for richer error message
        raise ValueError(f"{' '.join(cli_args)} finished with exit code {code}")
    # Make pb2 imports in generated scripts relative
    for script in glob.iglob(f'{output_path}/*.py'):
        with open(script, 'r+') as file:
            code = file.read()
            file.seek(0)
            file.write(re.sub(r'\n(import .+_pb2.*)', 'from . \\1', code))
            file.truncate()


def libp2p_build_install():
    try:
        result = subprocess.run("go version", capture_output=True, shell=True).stdout.decode('ascii', 'replace')
        m = re.search(r'^go version go([\d.]+)', result)
        v = m.group(1)

        if version.parse(v) < version.parse("1.13"):
            raise EnvironmentError(f'Newer version of go required: must be >= 1.13, found {version}')

    except FileNotFoundError:
        raise FileNotFoundError('Could not find golang installation')

    with tempfile.TemporaryDirectory() as tempdir:
        dest = os.path.join(tempdir, 'libp2p-daemon.tar.gz')
        urllib.request.urlretrieve(LIBP2P_TAR_URL, dest)

        with tarfile.open(dest, 'r:gz') as tar:
            dirname = os.path.join(tempdir, tar.getmembers()[0].name)
            tar.extractall(tempdir)
            os.rename(dirname, os.path.join(tempdir, f'go-libp2p-daemon-{P2PD_VERSION[1:]}'))

        result = subprocess.run(f'go build -o {shlex.quote(os.path.join(here, "src", "src_cli", "p2pd"))}',
                                cwd=os.path.join(tempdir, f'go-libp2p-daemon-{P2PD_VERSION[1:]}', 'p2pd'), shell=True)

        if result.returncode:
            raise RuntimeError('Failed to build or install libp2p-daemon:'
                               f' exited with status code: {result.returncode}')


class Install(install):
    def run(self):
        libp2p_build_install()
        proto_compile(os.path.join(self.build_lib, 'src', 'proto'))
        super().run()


class Develop(develop):
    def run(self):
        libp2p_build_install()
        proto_compile(os.path.join('src', 'proto'))
        super().run()


with open('requirements.txt') as requirements_file:
    install_requires = list(map(str, parse_requirements(requirements_file)))

# loading version from setup.py
with codecs.open(os.path.join(here, 'src/__init__.py'), encoding='utf-8') as init_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", init_file.read(), re.M)
    version_string = version_match.group(1)

setup(
    name='src',
    version=version_string,
    cmdclass={'install': Install, 'develop': Develop},
    packages=find_packages(),
    package_data={'src': ['proto/*']},
    include_package_data=True,
    license='MIT',
    setup_requires=['grpcio-tools'],
    install_requires=install_requires,
)
