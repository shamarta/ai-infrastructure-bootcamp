import sys

def main():
    args = sys.argv[1:]  # اولین عضو (sys.argv[0]) همیشه اسم خود فایل است
    print(f"You passed {len(args)} argument(s): {args}")

if __name__ == "__main__":
    main()