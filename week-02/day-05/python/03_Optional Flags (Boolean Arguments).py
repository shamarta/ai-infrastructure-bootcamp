import argparse

def main():
    parser = argparse.ArgumentParser(description="Deploy a service")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without applying changes")
    args = parser.parse_args()

    if args.dry_run:
        print("🧪 Dry run mode: no changes will be made.")
    else:
        print("🚀 Deploying for real...")

if __name__ == "__main__":
    main()