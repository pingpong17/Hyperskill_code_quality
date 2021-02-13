# Hyperskill_code_quality

Устанавливаются дополнения к flake8:
pip install wemake-python-styleguide
pip install cohesion
pip install radon

flake8 их автоматически подхватывает:
flake8 --version
3.8.4 (cohesion: 1.0.0, flake8-bandit: 2.1.2, flake8-broken-line: 0.3.0,
flake8-bugbear: 20.11.1, flake8-comprehensions: 3.3.1, flake8-darglint: 1.6.0,
flake8-debugger: 4.0.0, flake8-docstrings: 1.5.0, pydocstyle: 5.1.1,
flake8-eradicate: 1.0.0, flake8-string-format: 0.3.0, flake8_commas: 2.0.0,
flake8_isort: 4.0.0, flake8_quotes: 3.2.0, mccabe: 0.6.1, naming: 0.11.1,
pycodestyle: 2.6.0, pyflakes: 2.2.0, radon: 4.3.2, rst-docstrings: 0.0.14,
wemake_python_styleguide: 0.15.1)



В main.py проверяемый код.

cmd:
flake8 main.py > errors.txt 

cmd:
python parse_flake8.py > parsed_errors.txt
> errors.txt

В errors.txt - неструктурированный вывод flake8.
В parsed_errors.txt - ошибки сгруппированы по категориям.
