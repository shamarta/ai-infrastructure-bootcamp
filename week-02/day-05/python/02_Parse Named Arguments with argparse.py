import argparse

def main():
    parser = argparse.ArgumentParser(description="Check node status")
    parser.add_argument("--node-id", required=True, help="ID of the node")
    parser.add_argument("--threshold", type=int, default=80, help="CPU threshold")
    args = parser.parse_args()

    print(f"Checking {args.node_id} against threshold {args.threshold}%")

if __name__ == "__main__":
    main()