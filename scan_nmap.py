import subprocess, sys, datetime

def nmap_scan(target):
    print(f" Scanning target: {target} ...\n")
    try:
        result = subprocess.run(["nmap", "-sV", target],
                                capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error running nmap: {e}"

def save_report(target, data):
    filename = f"{target.replace('.', '_')}_report.txt"
    with open(filename, "w") as f:
        f.write(f"Scan Report for {target}\n")
        f.write(f"Timestamp: {datetime.datetime.now()}\n\n")
        f.write(data)
    print(f"\n Report saved as {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scan_nmap.py <target>")
        sys.exit(1)

    target = sys.argv[1]
    output = nmap_scan(target)
    print(output)            
    save_report(target, output)
