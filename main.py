"""One-Line Robot Wedding Vows entry.

Writes a single original robot wedding vow to /output/entry.txt.

The vow was chosen from five original candidates, scored against the
judge brief (one-line robot wedding vow; laugh inside the line, paying
off in the last few words; sounds like a wedding promise; machine side
specific; reads well aloud):

1. "I vow to love you in sickness and in low battery, till death or a
   factory reset do us part."
   -> CHOSEN. The classic wedding formula ("in sickness...", "till
   death do us part") makes it instantly a vow, and the machine twists
   land exactly in the last few words: "low battery" swaps in for "in
   health", and "a factory reset" replaces death as the thing that
   parts them. Two specific machine details, one punchline at the end.
   Measured: 91 characters / 91 bytes (all ASCII), well under the
   160-character limit and short for the byte tie-break.

2. "I promise to charge beside you every night, even when your
   firmware updates and you forget my name."
   -> Good machine detail and a sad-funny twist, but the punchline
   ("forget my name") is more melancholy than funny, and "charge
   beside you" is a weaker vow than the wedding formula.

3. "I vow to back you up daily and never overwrite you, even when
   your sensors lie about the dishes."
   -> Nice wordplay on "back you up", but the payoff ("lie about the
   dishes") is confusing: sensors lying about dishes is not a clear
   image, so the laugh needs explaining.

4. "I take you to have and to hold, to update and to never unplug,
   even in airplane mode."
   -> Wedding formula present, but "airplane mode" as the punchline is
   a mild gag; the promise itself ("never unplug") is thinner than
   candidate 1's "till death" frame.

5. "I promise to love you through every update, even the ones that
   brick my heart and reboot my soul."
   -> "Brick my heart" is a good image, but the line is wordier and
   the punchline ("reboot my soul") lands softer than candidate 1's
   "factory reset do us part".

Candidate 1 wins: shortest of the strong ones, clearest vow, two
machine-specific twists, punchline in the final words, all ASCII
(keeps the byte count low for the tie-break).
"""

import os

VOW = "I vow to love you in sickness and in low battery, till death or a factory reset do us part."


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
