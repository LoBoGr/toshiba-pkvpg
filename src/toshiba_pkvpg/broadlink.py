"""
BroadLink IR packet decoder.

Converts BroadLink Base64 strings into pulse timings.

Reference:
https://github.com/mjg59/python-broadlink
"""

from __future__ import annotations

import base64


TICK_US = 269 / 8192 * 1_000_000


def decode_base64(data: str) -> bytes:
    """Decode BroadLink Base64."""
    return base64.b64decode(data.strip())


def decode_ir_packet(packet: bytes) -> list[int]:
    """
    Decode a BroadLink IR packet into pulse timings (microseconds).

    Returns
    -------
    list[int]
        Alternating MARK/SPACE timings.
    """

    if packet[0] != 0x26:
        raise ValueError("Not a BroadLink IR packet")

    length = packet[2] | (packet[3] << 8)

    payload = packet[4:4 + length]

    pulses = []

    i = 0

    while i < len(payload):

        value = payload[i]

        if value == 0:
            break

        if value == 0x00:
            i += 1
            continue

        if value == 0xFF:
            duration = (payload[i + 1] << 8) | payload[i + 2]
            i += 3
        else:
            duration = value
            i += 1

        pulses.append(round(duration * TICK_US))

    return pulses
