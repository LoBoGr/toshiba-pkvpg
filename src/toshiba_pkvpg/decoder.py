from pathlib import Path

from broadlink import decode_base64, decode_ir_packet


CAPTURE_DIR = Path(__file__).resolve().parent.parent / "captures"


def main():

    for file in sorted(CAPTURE_DIR.glob("*.txt")):

        print("=" * 60)

        print(file.name)

        data = file.read_text().strip()

        packet = decode_base64(data)

        pulses = decode_ir_packet(packet)

        print(f"Pulses : {len(pulses)}")

        print(f"First 20 : {pulses[:20]}")

        print()


if __name__ == "__main__":
    main()
