import subprocess

# List of programs to verify
programs = [
    "build-essential",
    "curl",
    "eclipse",
    "firefox",
    "gcc",
    "gdu",
    "git",
    "htop",
    "openjdk-8-jdk",
    "openjdk-11-jdk",
    "nano",
    "vim",
    "code",  # Visual Studio Code
    "gdb",
    "nasm",
    "sasm",
    "pencil",
    "wget",
    "gpg",
    "autoconf",
    "automake",
    "rustc",
    "mpicc",  # OpenMPI
    "binutils",
    "sshd",  # OpenSSH Server
    "anaconda",  # Anaconda might need manual check
    "dot",  # Graphviz
    "mongo",  # MongoDB Compass
    "zookeeper",
    "protoc",  # Protobuf
]

def check_program(program):
    """Check if a program is installed on the system."""
    try:
        subprocess.run([program, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def main():
    print("Verifying installed programs...\n")
    for program in programs:
        if check_program(program):
            print(f"{program}: Installed")
        else:
            print(f"{program}: Not Installed")
    print("\nVerification complete.")

if __name__ == "__main__":
    main()
