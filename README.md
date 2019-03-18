# pinger
ICMP file transfer

This was an idea I had and I am sure it has been implemented many times before me. And maybe I had read that there exists programs that accomplish this in some of my years of computer stuffs. I thought this would be a good opportunity to integrate knowledge from multiple areas: networking, programming, and security. I have coded this without resorting to other resources as a challenge to determine if I have enough knowhow to go from concept to code. 

Pinger is a program that uses the ICMP protocol to send/receive small files over a network. This can be useful if certain programs are restricted by the network or when the network is not functioning properly or efficiently to enable file transfers. Because ICMP packets only allow 65535 bytes of data to be transmitted, small file transfers are possible by modifying the payload portion of the packet. This allows you to break up a simple file, like a jpeg, into small portions to send via ICMP.


