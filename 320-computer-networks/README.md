# CS 320 — Computer Networks

**Prerequisites:** CS 220
**Language:** C or Python (socket programming)

## Course Description

How the Internet works, layer by layer — from application protocols you use
daily (HTTP, DNS) down through transport (TCP/UDP), routing (IP), and the
link layer. Taught top-down: start with what you know as a backend engineer,
then peel back each abstraction.

## Learning Objectives

- Describe the layered architecture and what guarantee each layer adds
  (or doesn't).
- Explain HTTP (1.1/2/3), DNS, and TLS at the protocol level.
- Explain TCP: connection setup, reliability, flow control, and congestion
  control — and when UDP or QUIC is the better choice.
- Explain IP addressing, subnets, and how routing protocols move packets
  across networks.
- Write socket-level network programs and diagnose problems with standard
  tools (tcpdump/wireshark, dig, traceroute).

## Topic Outline

1. Internet architecture: layering, encapsulation, the end-to-end principle.
2. Application layer: HTTP semantics and evolution (1.1 → 2 → 3), REST at
   the wire level.
3. DNS: hierarchy, resolution, caching, failure modes.
4. Socket programming: TCP and UDP clients and servers.
5. Transport: UDP; TCP connection management (handshake, teardown), sliding
   windows, retransmission.
6. TCP congestion control: slow start, AIMD, and why your throughput is
   what it is; QUIC.
7. Network layer: IPv4/IPv6, addressing and subnets, NAT, DHCP, ICMP.
8. Routing: intra-domain (OSPF concepts) and inter-domain (BGP concepts).
9. Link layer: Ethernet, switching, ARP; a glance at wireless.
10. Security across the layers: TLS, certificates, common attacks
    (spoofing, hijacking, DDoS) and defenses.
