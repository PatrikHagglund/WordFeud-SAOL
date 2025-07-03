import subprocess

EXPECTED_HASHES = {
    "saol_wordlist.txt": "d179d76cb04baafcd5741767c027b36b8230a839",
    "saol2018clean.csv": "1ff05dc06860ac85fde80dc938979556de90366e",
    "WordFeud_ordlista.txt": "362f6e71ba0491dba348523c654763271630b434",
}

def git_hash_of_file(path: str) -> str:
    """Returnera git-objektets SHA-1-hash för en fil."""
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()

def test_expected_hashes() -> None:
    """Kontrollera att filer inte förändrats sedan de checkades in."""
    for fil, expected in EXPECTED_HASHES.items():
        actual = git_hash_of_file(fil)
        assert actual == expected, f"Hashvärdet för {fil} stämmer inte"