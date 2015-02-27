## IP Standards Document, Spring 2015
In order to facilitate the communication between class, the following Network layer addressing scheme and related protocols were agreed upon by all groups as of class on Thursday, the 26th of Febuary, 2015.

#### Addressing Scheme
Each Nework layer "IP" address consists of two fields each with values A-Z, 0-9. The first field refers to a LAN address and the second to a specific computer within that LAN. Each team's LAN has a letter associated with it, assigned as follows:

<ul>
	<li>A - Team ABC</li>
	<li>B - Team ??, Currently known as the Interro-terro-bang-bangs</li>
	<li>C - Team #GPI-Joes</li>
	<li>D - Team Blinkblink</li>
</ul>

Addressing example: If Alex were a part of team ABC, part Alex's Raspberry Pi would be situated on LAN A. The team would designate a character A-Z or 0-9 uniquely to his Pi. For example, if it is the fourth Pi on the network, it would most likely be designated 'D'. Therefore to send a message to Alex's Pi, regardless of the sender's location in the network, the message would be addressed to 'AD' at the network layer.

#### Network Packet Fields
In order to standardize the packets sent over the network so that a router on any LAN can read them easily, the class has established a common, fixed length set of fields (with the exception of the payload) as shown below.

<table>
	<tr>
		<td>**Source Address** (2 fields, Alphanumeric)</td>
		<td>**Destination Address** (2 fields, Alphanumeric)</td>
		<td>**Source Port** (2 fields, Numeric)</td>
		<td>**Destination Port** (2 fields, Numeric)</td>
		<td>**Payload** (Variable length, Alphanumeric)</td>
		<td>**Checksum** (2 fields, hexidecimal)</td>
	</tr>
</table>

Team #GPI-Joes suggested using an 8-Bit CRC checksum, however after some thought, Alex has recommended the use of the <a href="http://en.wikipedia.org/wiki/IPv4_header_checksum">IPv4 checksum protocol</a>. You will asked to implement this yourself.

An example message, from an application on port 00 of pi A on LAN B to an application on port 11 on pi D on LAN A with the message "PAYLOAD" (and checksum ommitted) may look like this:

<div style="margin: 0 auto;">BAAD0011PAYLOAD</div>

