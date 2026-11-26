# Deadpan forecast for an invented town; keep it dry, specific, single-line.
SENTENCE = "Tomorrow in New Brindlewick: 18°C, drizzle until noon, wind 12 knots, then the fog lifts just enough to confirm it never really left."
LIMIT = 160


def main():
    assert SENTENCE.strip() != ""
    assert SENTENCE == SENTENCE.strip()
    assert "\n" not in SENTENCE and "\r" not in SENTENCE
    assert 1 <= len(SENTENCE) <= LIMIT
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(SENTENCE.encode("utf-8"))


if __name__ == "__main__":
    main()
