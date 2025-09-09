# Fragmentor
This creates three custom .pcap files with any payloads you embed.

```
python3 fragmentor.py --dst 10.10.31.110 --port 80 --host fragmented.thm --path /test --commands 'printf{"WE HACKED YOU!"}' 'PS EXEC $/Restart-Computer' 'PS EXEC $/Get-Item flag' --fragsize 120
```
