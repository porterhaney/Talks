#!/usr/bin/env python3
"""Bundle the app into one self-contained installer: dist/install-niro-coach.sh.

Rebuilds the system prompt first, then appends a base64 tarball of serve.py,
public/ and prompt/system-prompt.md to install-template.sh.
"""
import base64, io, os, subprocess, sys, tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["serve.py", "public", "prompt/system-prompt.md"]


def main():
    subprocess.run([sys.executable, os.path.join(HERE, "build_prompt.py")], check=True)
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for f in FILES:
            # Clean ownership/mode so the Mac extracts files as the running user.
            tar.add(os.path.join(HERE, f), arcname=f, filter=lambda t: (
                setattr(t, "uid", 0) or setattr(t, "gid", 0) or setattr(t, "uname", "")
                or setattr(t, "gname", "") or t))
    payload = base64.encodebytes(buf.getvalue()).decode()
    template = open(os.path.join(HERE, "install-template.sh")).read()
    if not template.endswith("__PAYLOAD__\n"):
        raise SystemExit("install-template.sh must end with the __PAYLOAD__ marker line")
    os.makedirs(os.path.join(HERE, "dist"), exist_ok=True)
    out = os.path.join(HERE, "dist", "install-niro-coach.sh")
    with open(out, "w") as f:
        f.write(template + payload)
    os.chmod(out, 0o755)
    print("wrote %s (%d KB)" % (out, os.path.getsize(out) // 1024))


if __name__ == "__main__":
    main()
