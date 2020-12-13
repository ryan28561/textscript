# SendText

This is a quick and simple script for sending texts via adb.

Example: `sendtext +19999999999 "hello world"`

I always turn my laptop off when I'm leaving work, so I created this to be added to a cron task to let my wife know when I'm running late:
```
5 5 * * * ~/scripts/senttext +19999999999 "I'm still at work, I'll let you know when I'm leaving."
