## Pipeline: Queue → Infographic → Delivery

The full growth hacking content pipeline:

### 1. Research → QC → Queue
- Daily research scan by Pulse into `~/.hermes/growth-hacking/research/YYYY-MM-DD.md`
- Arc QC pass: named source, specific metric, reproducible, not AI slop
- Approved items go to `~/.hermes/growth-hacking/queue/queue.md` with `#READY` tag

### 2. Infographic Generation
- One HTML file per item: `~/.hermes/growth-hacking/output/gh-infographic-<slug>-YYYY-MM-DD.html`
- Use this template's glassmorphism style (see style reference)
- Export to PNG: `python3 ~/.hermes/skills/aiz-infographic/scripts/export.py --png --selector ".canvas" <file.html>`

### 3. Post Text
- Short post text for X/LinkedIn: 2-3 sentences, lead with the hook stat
- Saved to `~/.hermes/growth-hacking/posts/<slug>-social-posts.md`

### 4. Sequential Discord Delivery
For batch delivery (one by one to a Discord channel):

1. Create `~/.hermes/growth-hacking/delivery-queue.json`:
```json
{
  "current_index": 0,
  "items": [
    {
      "number": 1,
      "title": "Item Title",
      "png": "/absolute/path/to/file.png",
      "post": "Post text here."
    }
  ]
}
```

2. **Correct script path:** `~/growth-hacking/scripts/deliver-next.py` (NOT `~/scripts/gh-deliver-next.py` — that path is stale and will cause an immediate SCRIPT-NOT-FOUND error).

    Script contract:
    - Reads queue JSON, outputs next item's image path + post text
    - Increments `current_index` after each run
    - Outputs `DONE: All N infographics delivered` (N is dynamic from `len(items)`) when queue exhausted

    **Hardcoded-count pitfall:** If the script contains a hardcoded completion line like `"All 11 infographics delivered"` or `"of 11"`, it will either lie to the user or stop prematurely when the queue grows. Always patch before queue changes:
    ```python
    # Bad — stale after queue exceeds write-time count
    print(f"**Growth Hack #{item['number']} of 11**")
    print("DONE: All 11 infographics have been delivered.")
    # Good — dynamic, stays correct regardless of queue size
    print(f"**Growth Hack #{item['number']} of {len(items)}**")
    print(f"DONE: All {len(items)} infographics delivered.")
    ```

3. Cron job: `schedule: 0,30 * * * *` (every 30 min), `repeat: 999` or omit repeat entirely for evergreen
    - `deliver: discord:<channel_id>`
    - Prompt tells agent to run `bash ~/.hermes/growth-hacking/scripts/deliver-next.py` and relay stdout (MEDIA: lines become Discord attachments automatically)

    **CRITICAL — cron repeat count:**
    - `repeat: N` where N = queue size → cron silently stops after N runs. Delivery is dead. Queue grows → cron still dead.
    - `repeat: 999` or `repeat: omitted` → cron fires on schedule forever until manually removed. Use this for delivery jobs.

    **Diagnosis pattern when delivery isn't working — check in this exact order:**

    | # | Check | Symptom if broken |
    |--|-------|-------------------|
    | 1 | Script path (`which` + `ls` confirm it exists) | SCRIPT-NOT-FOUND error |
    | 2 | grep `"of [0-9]"` or `"All [0-9]"` in script text | Wrong header, premature DONE |
    | 3 | `python3 deliver-next.py` dry-run (then reset index to 0) | Index mismatch, off-by-one on first real run |
    | 4 | `cronjob list` — enabled + scheduled | Cron expired/disabled, pipeline dead |
    | 5 | `grep '#READY' queue.md | wc -l` vs `len(items)` in JSON | Queue/sync out of date |

    **Never claim delivery is working until all 5 checks pass.**