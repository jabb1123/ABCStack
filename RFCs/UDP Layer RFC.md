## UDP Protocol RFC
##### Mar 3, 2015
##### Author: Nick Francisci
User Datagram Protocol (UDP) is a transport layer protocol which allows for the transmission of data from a source appliation to a destination application (often on a different host). The sockets interface, implemented by the kernel of the OS, maps internal process IDs to the "ports" used by transport layer protocols.

UDP is quite simple. Unlike TCP, it does not verify the reception of the data, nor does it control sending rate, or maintain connection state information. It is a simple, "fire-and-forget" protocol for getting data from one application to another.

#### UDP Packet Fields
Checksum to be specified at a later date.

<table>
    <tr>
        <td><strong>Source Port</strong> (2 fields, Numeric)</td>
        <td><strong>Dest Port</strong> (2 field, Numeric)</td>
        <td><strong>Payload</strong> (Variable length, Alphanumeric)</td>
    </tr>
</table>
