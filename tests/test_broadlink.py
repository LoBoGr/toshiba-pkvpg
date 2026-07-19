from tools.broadlink import decode_base64


def test_decode():

    packet = decode_base64("JgA=")

    assert isinstance(packet, bytes)
