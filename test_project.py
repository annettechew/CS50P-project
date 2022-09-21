from project import checkword, searchagain, translate

def test_checkword():
    assert checkword("abandoned industrial site") == ["Site that cannot be used for any purpose, being contaminated by pollutants."]
    assert checkword("abandoned vehicle") == ["A vehicle that has been discarded in the environment, urban or otherwise, often found wrecked, destroyed, damaged or with a major component part stolen or missing."]
    assert checkword("exhausted") == ["Who lived a hard experience and is therefore drained of energy or effectiveness, or extremely tired."]


def test_searchagain():
    assert searchagain("yes") == True
    assert searchagain("no") == False

def test_translate():
    assert translate(['Expression of greeting used by two or more people who meet each other.'], "french") == "Expression de salutation utilisée par deux personnes ou plus qui se rencontrent."
    assert translate(['A distinct unit of language (sounds in speech or written letters) with a particular meaning, composed of one or more morphemes, and also of one or more phonemes that determine its sound pattern.'], "spanish") == "Una unidad distinta de lenguaje (sonidos en el habla o letras escritas) con un significado particular, compuesta de uno o más morfemas, y también de uno o más fonemas que determinan su patrón de sonido."
