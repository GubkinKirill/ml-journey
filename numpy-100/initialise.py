"""Помощники для работы с задачами.

Подключается первой ячейкой ноутбука: %run initialise.py

    question(3)  # условие задачи
    hint(3)      # подсказка
    pick()       # случайная задача
"""

from pathlib import Path

import numpy as np

SOURCE = Path(__file__).parent / 'source' / 'exercises.ktx'


def _load(path, keystarter='<'):
    """Разбор keyed-text файла в словарь {ключ: текст}."""
    data, key = {}, None
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith(keystarter):
            key = line.lstrip(keystarter).strip()
            data[key] = ''
        elif key is not None:
            data[key] = (data[key] + '\n' + line).strip()
    return data


TEXTS = _load(SOURCE)


def question(n):
    """Условие задачи n на английском и русском."""
    head, _, rest = TEXTS[f'q{n}'].partition('\n')
    print(f'{n}. {head}')
    print('   ' + TEXTS[f'r{n}'])
    if rest.strip():
        print(rest.strip())


def hint(n):
    """Подсказка: какие функции стоит посмотреть."""
    print(TEXTS[f'h{n}'])


def pick():
    """Случайная задача."""
    question(np.random.randint(1, 101))
