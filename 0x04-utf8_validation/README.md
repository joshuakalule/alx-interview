# UTF-8 validation

Unicode was a replacement for ASCII to unify character encoding from across the world.
utf-8 uses variable length encoding that can represent each character (Singlugar grahphene such as a, 👍, 他) using a code point
A code point is in the format U+XXXX
This means that graphenes can be represented as 1 byte, 2 bytes, 3 bytes or 4 bytes

## Codepoints

| Bytes  | Code point start | Code point stop |
|--------|------------------|-----------------|
| 1 byte | U+0000           | U+007F          |
| 2 byte | U+0080           | U+007F          |
| 3 byte | U+0800           | U+007F          |
| 4 byte | U+0000           | U+007F          |

## Codepoints in binary

The start of a byte communicates the meaning of the byte

* 0 - 1 byte: The current byte contains all the data bits
* 110 - 2 bytes: The current byte and the next 1 byte contain the data bits
* 1110 - 3 bytes: The current byte and the next 2 bytes contain the data bits
* 11110 - 4 bytes: The current byte and the next 3 bytes contain the data bits
