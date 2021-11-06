# -*- coding: utf-8 -*-
from typing import List, Tuple
from laonlp.corpus import get_path_corpus
from pythainlp.tag import PerceptronTagger

_FILENAME = "ptagger_kashgari_corpus.json"
_PATH = get_path_corpus(_FILENAME)
_TAGGER = PerceptronTagger(path=_PATH)


def pos_tag(
    words: List[str],
    engine: str = "perceptron",
    corpus: str = "kashgari"
) -> List[Tuple[str, str]]:
    """
    Lao Part-of-speech

    We use lao corpus from https://github.com/FoVNull/SeqLabeling

    :param List[str] words:  a list of tokenized lao words
    :param str engine: engine of pos_tag (perceptron engine)
    :param str corpus: kashgari (corpus from https://github.com/FoVNull/SeqLabeling)

    :return: a list of tuples (word, POS tag)
    :rtype: list[tuple[str, str]]
    """
    return _TAGGER.tag(words)