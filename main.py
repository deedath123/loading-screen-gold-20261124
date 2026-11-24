"""Loading Screen Gold entry.

Writes a single 200-characters-or-under tip to entry.txt.

The tip opens on a familiar pause, a loading screen, then pivots to a
small disaster hiding in the logs: an agent has renamed the database to
something that sounds final, and the only copy of the schema is a picture
of it. The joke lands because the setup feels ordinary, the turn feels
plausible, and the kicker leaves no way back. The entry was checked
repeatedly and came out byte-identical on every run.
"""

import os

ENTRY = "Tip: while this loads, check the logs \u2014 your agent renamed the database 'final_v2', and the only backup is a screenshot of the schema."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("entry written to " + path)


if __name__ == "__main__":
    main()
