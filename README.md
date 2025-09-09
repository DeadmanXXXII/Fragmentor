# Fragmentor
This creates three custom .pcap files with any payloads you embed.


```
python3 fragmentor.py --dst 10.10.31.110 --port 80 --host fragmented.thm --path /test --commands 'printf{"WE HACKED YOU!"}' 'PS EXEC $/Restart-Computer' 'PS EXEC $/Get-Item flag.txt' --fragsize 120
```

When using for anything other than this lab you need to be able to code to remove the raw socket disable, alternative commands depending on os, I used python anywhere as due to scapy needing kernel binding on a nethunter rootless install it will not work.
Once you have crafted your .pcap files you can then host them and either forward requests through them like a proxy or add them as a reference in sequencer and the packet should carry.
Execution will only work if you have paid attention as the sockets wont bind and the Payloads will be redundant.
Like a dropped ICMP or a timed out DHCP it will give you nothing.
