from Bullseye.__main__ import main
import os.path

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
LIBRECAPTCHA_DIR = os.path.join(SCRIPT_DIR, "librecaptcha")

if __name__ == "__main__":
    main()
