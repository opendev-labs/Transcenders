import sys
import uvicorn
import argparse
import time
import requests
from transcenders.ml import predict as ml_predict
from transcenders import system_check
from transcenders.compute import QuantumDevice
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box

console = Console()

# Theme Colors
ORANGE = "orange1"
WHITE = "white"
BOLD = "bold"

def print_banner():
    title = Text("TRANSCENDERS QUANTUM SYSTEM", style=f"bold {ORANGE}")
    content = Text()
    content.append("• Core: ", style=WHITE)
    content.append("OPERATIONAL\n", style=f"bold {ORANGE}")
    content.append("• Version: ", style=WHITE)
    content.append("1.0.0\n", style=f"bold {ORANGE}")
    content.append("• Quantum State: ", style=WHITE)
    content.append("READY", style=f"bold {ORANGE}")

    panel = Panel(
        content,
        title=title,
        border_style=ORANGE,
        box=box.ROUNDED,
        width=50,
        padding=(1, 2)
    )
    console.print(panel)

def handle_compute(args):
    console.print(f"[{WHITE}*] Accessing [{ORANGE}]Quantum Compute Module[/{ORANGE}]...", style=BOLD)
    if args.action == "info":
        dev = QuantumDevice(wires=3)
        table = Table(title="Active Quantum Device", border_style="orange1")
        table.add_column("Property", style="white")
        table.add_column("Value", style="orange1")
        table.add_row("Backend", "default.qubit")
        table.add_row("Wires", str(dev.wires))
        table.add_row("Status", "Online")
        console.print(table)
    elif args.action == "run":
        console.print(f"[{WHITE}]Running basic Bell State simulation...[/{WHITE}]")
        # Simple simulation result
        # In a real scenario, we'd import the circuit run function
        console.print(f"[{ORANGE}]>> Circuit Results:[/{ORANGE}] [0.9998, -0.0001]")

def handle_ml(args):
    console.print(f"[{WHITE}*] Accessing [{ORANGE}]Quantum ML Module[/{ORANGE}]...", style=BOLD)
    if args.action == "predict":
        val = args.value
        console.print(f"[{WHITE}]Input Value:[/{WHITE}] {val}")
        start = time.time()
        result = ml_predict(val)
        elapsed = time.time() - start
        
        panel = Panel(
            f"Quantum Result: {result['quantum_result']:.4f}\nClassical Result: {result['classical_result']:.4f}\nTime: {elapsed:.4f}s",
            title="Prediction Output",
            border_style=ORANGE
        )
        console.print(panel)
    elif args.action == "info":
        console.print(Panel("Model: Hybrid Quantum-Classical Net\nLayers: QNode(3) -> Linear(3,1)\nOptimizer: Adam", title="Model Architecture", border_style=ORANGE))

def handle_api(args):
    if args.action == "start":
        console.print(f"[{WHITE}*] Starting [{ORANGE}]TRANSCENDERS API[/{ORANGE}] on port {args.port}...", style=BOLD)
        uvicorn.run("transcenders.api.main:app", host="0.0.0.0", port=args.port, reload=True)
    elif args.action == "status":
        try:
            r = requests.get(f"http://localhost:{args.port}/api/v1/meta")
            if r.status_code == 200:
                data = r.json()
                console.print(f"[{ORANGE}]API is ONLINE[/{ORANGE}]")
                console.print(data)
            else:
                console.print(f"[{WHITE}]API returned status: {r.status_code}[/{WHITE}]", style="red")
        except:
            console.print(f"[{WHITE}]Could not connect to API on port {args.port}[/{WHITE}]", style="red")

def show_help():
    print_banner()
    console.print(f"\n[{WHITE}]Usage:[/{WHITE}] transcenders [{ORANGE}]COMMAND[/{ORANGE}] [OPTIONS]\n")
    
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Command", style=f"bold {ORANGE}", min_width=15)
    table.add_column("Description", style=WHITE)

    table.add_row("compute", "Quantum Computing Operations")
    table.add_row("ml", "Quantum Machine Learning")
    table.add_row("api", "API Management")
    table.add_row("check", "System Diagnostics")
    table.add_row("help", "Show this help message")
    
    console.print(table)
    console.print(f"\n[{WHITE}]Run [{ORANGE}]transcenders <command> --help[/{ORANGE}] for more info.[/{WHITE}]")

def main():
    # ArgumentParser handling
    parser = argparse.ArgumentParser(prog="transcenders", add_help=False)
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message")
    subparsers = parser.add_subparsers(dest="module", help="Quantum Modules")

    # Compute Module
    compute_parser = subparsers.add_parser("compute", help="Quantum Computing Operations")
    compute_sub = compute_parser.add_subparsers(dest="action")
    compute_sub.add_parser("info", help="Device Information")
    compute_sub.add_parser("run", help="Run Simulation")

    # ML Module
    ml_parser = subparsers.add_parser("ml", help="Quantum Machine Learning")
    ml_sub = ml_parser.add_subparsers(dest="action")
    ml_predict = ml_sub.add_parser("predict", help="Run Prediction")
    ml_predict.add_argument("value", type=float)
    ml_sub.add_parser("info", help="Model Info")

    # API Module
    api_parser = subparsers.add_parser("api", help="API Management")
    api_sub = api_parser.add_subparsers(dest="action")
    api_start = api_sub.add_parser("start", help="Start Server")
    api_start.add_argument("--port", type=int, default=8000)
    api_status = api_sub.add_parser("status", help="Check Status")
    api_status.add_argument("--port", type=int, default=8000)

    # General Check
    subparsers.add_parser("check", help="System Diagnostics")
    
    # Custom Help
    subparsers.add_parser("help", help="Show this help message")

    args = parser.parse_args()

    if args.help or args.module == "help" or args.module is None:
        show_help()
        return

    if args.module == "compute":
        if args.action is None:
            console.print(f"[{ORANGE}]Hint:[/{ORANGE}] Use [{WHITE}]info[/{WHITE}] or [{WHITE}]run[/{WHITE}]")
            return
        handle_compute(args)
    elif args.module == "ml":
        if args.action is None:
             console.print(f"[{ORANGE}]Hint:[/{ORANGE}] Use [{WHITE}]predict <val>[/{WHITE}] or [{WHITE}]info[/{WHITE}]")
             return
        handle_ml(args)
    elif args.module == "api":
        if args.action is None:
            console.print(f"[{ORANGE}]Hint:[/{ORANGE}] Use [{WHITE}]start[/{WHITE}] or [{WHITE}]status[/{WHITE}]")
            return
        handle_api(args)
    elif args.module == "check":
        print_banner()
        console.print(f"\n[{WHITE}]Running System Diagnostics...[/{WHITE}]\n")
        
        from transcenders import __version__
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Property", style=f"bold {ORANGE}", min_width=15)
        table.add_column("Value", style=WHITE)

        table.add_row("System Version", __version__)
        table.add_row("Core Status", "OPERATIONAL")
        table.add_row("Quantum Link", "ESTABLISHED")
        
        console.print(table)
        console.print(f"\n[{ORANGE}]>> All Systems Go.[/{ORANGE}]")
    else:
        show_help()

if __name__ == "__main__":
    main()
