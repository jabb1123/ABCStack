## Network Layer RFC
##### Feb 27, 2015
In order to facilitate the communication between class, the following Network layer addressing scheme and related protocols was proposed on Thursday, the 26th of Febuary, 2015. Subsequent edits have been applied.

#### Addressing Scheme
Each nework layer "IP" address consists of two fields each with values A-Z, 0-9. The first field refers to a LAN address and the second to a specific host within that LAN. Each team's LAN has a letter associated with it, assigned as follows:

<ul>
	<li>A - Team ABC</li>
	<li>B - Team ??, Currently known as the Interro-terro-bang-bangs</li>
	<li>C - Team #GPI-Joes</li>
	<li>D - Team Blinkblink</li>
</ul>

Addressing example: If Alex were a part of team ABC, part Alex's Raspberry Pi would be situated on LAN A. Team ABC would designate a character A-Z or 0-9 uniquely to his Pi. For example, if it is the fourth Pi on the network, it could be designated '4'. Therefore to send a message to Alex's Pi, regardless of the sender's location in the network, the message would be addressed to 'A4' at the network layer.

#### Network Packet Fields
In order to standardize the packets sent over the network so that a router on any LAN can read them easily, the class has established a common, fixed length set of header fields as shown below.

<table>
	<tr>
		<td><strong>Source LAN</strong> (1 field, Alphanumeric)</td>
		<td><strong>Source Host</strong> (1 field, Alphanumeric)</td>
		<td><strong>Destination LAN</strong> (1 fields, Alphanumeric)</td>
		<td><strong>Destination Host</strong> (1 field, Alphanumeric)</td>
		<td><strong>Next Protocol</strong> (1 field, Alphanumeric*)</td>
		<td><strong>Header Checksum</strong> (4 fields, Hexidecimal)</td>
		<td><strong>Payload</strong> (Variable length, Alphanumeric)</td>
		
	</tr>
</table>
* - for the Next Protocol field: A = UDP, B = TCP

For the checksum calculation, we will be following the <a href="http://en.wikipedia.org/wiki/IPv4_header_checksum">IPv4 header checksum protocol</a>. You will asked to implement this yourself. To facilitate performing the operations specified in the IPv4 header checksum protocol, we suggest placing the header fields into a python bytearray.

