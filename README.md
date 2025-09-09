# Fragmentor
This creates custom .pcap files with any payloads you embed each Payload is given its own packet and can be encoded for obfuscation.


```
python3 fragmentor.py --dst 10.10.31.110 --port 80 --host fragmented.thm --path /test --commands 'printf{"WE HACKED YOU!"}' 'PS EXEC $/Restart-Computer' 'PS EXEC $/Get-Item flag.txt' --fragsize 120
```

I used python anywhere as due to scapy needing kernel and socket binding on a nethunter rootless install it will not work.

Once you have crafted your .pcap files you can then host them and either forward requests through them like a proxy or add them as a reference in sequencer and the packet should carry.

Execution will only work if you have paid attention as the sockets wont bind and the Payloads will be redundant.
Like a dropped ICMP or a timed out DHCP it will give you nothing.

---

1. Command Explanation
```
python3 fragmentor.py \
  --dst 10.10.31.110 \
  --port 80 \
  --host fragmented.thm \
  --path /test \
  --commands 'printf{"WE HACKED YOU!"}' 'PS EXEC $/Restart-Computer' 'PS EXEC $/Get-Item flag.txt' \
  --fragsize 120
```
--dst 10.10.31.110 → Target IP.

--port 80 → Target port.

--host fragmented.thm → HTTP host header to use.

--path /test → Request path.

--commands ... → Commands you want the payload to attempt when reassembled.

--fragsize 120 → Maximum fragment size for the IP fragments.


Note: PS EXEC $/... commands simulate Windows PowerShell execution for testing purposes.


---

2. Why PythonAnywhere Works

Scapy often requires raw sockets and kernel-level access.

On rootless NetHunter, raw socket binding fails → you can’t generate packets in real-time.

PythonAnywhere is enough for crafting .pcap files because it doesn’t need actual packet sending.



---

3. Usage Considerations

Hosting .pcap files:

You can forward traffic through them (like a proxy).

Use tools like Sequencer to replay the packets in an order or?


Execution won’t happen automatically unless:

Sockets bind successfully.

Payloads are compatible with the target OS.

Timing/ICMP/DHCP fragmentation issues are handled correctly.




---

4. Advanced Notes

To use outside the lab:

You’ll need OS-specific payloads.

Remove the raw socket disable if you want active testing.

Be careful: running arbitrary commands through packet delivery remotely can break systems or trigger security alerts and cause thousands in damages.




---

[fragcmd1](https://raw.githubusercontent.com/DeadmanXXXII/Fragmentor/Screenshot_20250909-214559.png)

![](https://raw.githubusercontent.com/DeadmanXXXII/Fragmentor/Screenshot_20250909-214756.png)
