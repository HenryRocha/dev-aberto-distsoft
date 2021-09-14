from setuptools import setup

setup(
    name="dev_aberto_henryfr1",
    description="Disponibiliza um programa executável `hello.py`, que imprime a mensagem \"Hello, World!\" na tela.",
    long_description="Disponibiliza um programa executável `hello.py`, que imprime a mensagem \"Hello, World!\" na tela.",
    author="Henry Rocha, Thomas Queiroz and André Weber",
    author_email="henryrocha@protonmail.com",
    url="https://github.com/HenryRocha/dev-aberto-distsoft",
    license="MIT",
    version="0.2.3",
    packages=["dev_aberto"],
    scripts=["scripts/hello.py"],
    depencies=["requests"],
    python_requires=">=3.6",
    platforms=["Windows", "Linux", "Mac OS-X"],
)
