import csv
import time
import sys
import random
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.text import Text

# Configuration
console = Console()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "major_events.csv")

# Dynamic Future Scenarios
FUTURE_SCENARIOS = [
    {"year": "2032", "event": "Global Quantum Encryption Collapse", "risk": 9, "eco": "Total Market Reset"},
    {"year": "2040", "event": "First Human Colony on Mars Established", "risk": 2, "eco": "Interstellar Boom"},
    {"year": "2035", "event": "AI Singularity: Sentient Governance", "risk": 10, "eco": "Post-Wealth Shift"},
    {"year": "2045", "event": "Neural Link Global Integration Peak", "risk": 5, "eco": "Cognitive Economy"}
]

ASCII_HEADER = """
[bold cyan]
 ██████  ██████  ██████  ███████     ███████ ██   ██  █████  ██████   ██████  ██     ██
██      ██    ██ ██   ██ ██          ██      ██   ██ ██   ██ ██   ██ ██    ██ ██     ██
██      ██    ██ ██████  █████       ███████ ███████ ███████ ██   ██ ██    ██ ██  █  ██
██      ██    ██ ██   ██ ██               ██ ██   ██ ██   ██ ██   ██ ██    ██ ██ ███ ██
 ██████  ██████  ██   ██ ███████     ███████ ██   ██ ██   ██ ██████   ██████   ███ ███ 
[/bold cyan]
[dim white]  >> SECURE TERMINAL v13.0 | CINEMATIC DOCUMENTARY EDITION | REDACTED INTEL <<[/dim white]
"""

def typewriter(text, style="bold green", speed=0.06):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(speed)
    console.print()

def biometric_scan():
    console.clear()
    console.print(Align.center(ASCII_HEADER))
    time.sleep(1.2)
    with Progress(SpinnerColumn(spinner_name="dots12"), TextColumn("[bold white]INITIALIZING NEURAL LINK...[/bold white]"), BarColumn(bar_width=40), transient=True) as progress:
        task = progress.add_task("", total=100)
        while not progress.finished:
            progress.update(task, advance=1.1)
            time.sleep(0.05)

    console.print("[bold white]» AUTHOR IDENTIFIED:[/bold white] ", end=""); typewriter("Mayank", speed=0.1)
    console.print("[bold white]» NEURAL SIGNATURE:[/bold white] ", end=""); typewriter("CORE SHADOW", speed=0.1)
    console.print("[bold white]» DECRYPTION KEY :[/bold white] ", end=""); typewriter("*****", style="bold red", speed=0.2)
    time.sleep(1.5)
    console.print("\n[bold reverse blue]  WAR ROOM ACCESS GRANTED: VIDEO MODE ACTIVE  [/bold reverse blue]")
    time.sleep(2)

def create_layout():
    layout = Layout()
    layout.split_column(Layout(name="header", size=6), Layout(name="main"), Layout(name="footer", size=3))
    layout["main"].split_row(Layout(name="side", ratio=1), Layout(name="body", ratio=3))
    return layout

def get_tension_graph(risks):
    graph = []
    max_h = 5
    for r in risks[-15:]:
        try: val = int(r)
        except: val = 0
        h = int((val / 10) * max_h)
        graph.append("█" * h + " " * (max_h - h))
    rows = []
    for i in range(max_h - 1, -1, -1):
        row = "".join(["[red]█[/red]" if (len(g) > i and g[i] == "█") else "[dim blue]·[/dim blue]" for g in graph])
        rows.append(row)
    return "\n".join(rows)

def run_simulation():
    events = []
    if not os.path.exists(CSV_PATH): return

    with open(CSV_PATH, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        events = [row for row in reader if any(row.values())]

    layout = create_layout()
    table = Table(expand=True, border_style="dim blue", box=None)
    table.add_column("YEAR", style="bold white", width=6)
    table.add_column("STRATEGIC EVENT", style="cyan")
    table.add_column("PRIMARY LEADER", style="dim white")
    table.add_column("POWER SHIFT", justify="center")
    table.add_column("RISK", justify="right")

    layout["header"].update(Panel(Align.center(ASCII_HEADER), border_style="blue"))
    risk_history = []

    with Live(layout, refresh_per_second=10, screen=True):
        for i, event in enumerate(events):
            time.sleep(1.8) # Slowed down for viewers to read
            
            risk_val = event.get('Risk', '0')
            risk_history.append(risk_val)
            theme_color = "red" if int(risk_val) >= 8 else "yellow" if int(risk_val) >= 5 else "blue"
            
            table.add_row(
                event.get('Year', '????'),
                event.get('Event', 'NULL'),
                event.get('Leader', 'N/A'),
                f"[bold magenta]{event.get('Power_Shift', 'None')}[/bold magenta]",
                f"[bold {theme_color}]{risk_val}/10[/bold {theme_color}]"
            )
            
            # Detailed Sidebar with Cycling Intel
            side_content = [
                "[bold cyan]TENSION TREND[/bold cyan]",
                get_tension_graph(risk_history),
                "[dim blue]──────────────[/dim blue]",
                "[bold yellow]STAKES[/bold yellow]",
                f"[white]{event.get('Geopolitical_Stakes', '')[:85]}...[/white]",
                "[dim blue]──────────────[/dim blue]",
                "[bold red]REDACTED FACT[/bold red]",
                f"[bold white]{event.get('Redacted_Fact', '')[:85]}...[/bold white]",
                "[dim blue]──────────────[/dim blue]",
                f"[bold {theme_color}]KEY TECH: {event.get('Key_Tech', 'UNK').upper()}[/bold {theme_color}]"
            ]
            layout["side"].update(Panel("\n".join(side_content), title="[white]INTEL[/white]", border_style=theme_color))
            layout["body"].update(Panel(table, title="[white]WORLD_LOGS_DECRYPTED[/white]", border_style=theme_color))
            
            ticker = f" [cyan][*][/cyan] REGION: {event.get('Region', 'GLB')} | SYSTEM STATUS: OPTIMAL | DATA_SYNC: {random.randint(92, 99)}% | WAR_ROOM_v13 "
            layout["footer"].update(Panel(Align.center(ticker), border_style=theme_color))

        # IMPORTANT: Fix the screen at the end of history so viewers can read the final table
        layout["footer"].update(Panel(Align.center("[bold yellow]>>> HISTORY LOG COMPLETE. PAUSING FOR ANALYSIS... <<<[/bold yellow]"), border_style="yellow"))
        time.sleep(8) 

    # Autonomous Transition
    console.clear(); console.print(Panel(Align.center(ASCII_HEADER), border_style="red")); time.sleep(1.5)
    console.print("\n[bold red][ALERT][/bold red] History Log Terminated. Engaging Future Vector Oracle..."); time.sleep(2)
    
    scenario = random.choice(FUTURE_SCENARIOS)
    console.print("\n" + "─" * 60)
    console.print(f"[bold yellow]» TARGET YEAR  : {scenario['year']}[/bold yellow]")
    console.print(f"[bold yellow]» TARGET EVENT : {scenario['event'].upper()}[/bold yellow]")
    
    with Progress(SpinnerColumn(spinner_name="earth"), TextColumn("[bold red]Simulating 1,000,000 Geopolitical Timelines...[/bold red]"), transient=True) as progress:
        task = progress.add_task("", total=100)
        while not progress.finished:
            progress.update(task, advance=1.2); time.sleep(0.06)
            
    # Final Result with long pause
    risk_calc = scenario['risk']
    surv_calc = random.randint(5, 95)
    res_panel = [
        f"[bold white]PREDICTION: {scenario['event'].upper()}[/bold white]",
        f"[bold cyan]GEOPOLITICAL RISK:[/bold cyan] {'█' * risk_calc}{'░' * (10-risk_calc)} ({risk_calc}/10)",
        f"[bold cyan]PRIMARY OUTCOME  :[/bold cyan] [magenta]{scenario['eco']}[/magenta]",
        f"[bold cyan]SURVIVAL CHANCE  :[/bold cyan] [bold {'green' if surv_calc > 50 else 'red'}]{surv_calc}%[/bold {'green' if surv_calc > 50 else 'red'}]",
        "\n[dim white]Historical precedent suggests a massive shift in cognitive labor markets.[/dim white]"
    ]
    console.print(Panel("\n".join(res_panel), title="[bold red]ORACLE_FINAL_REPORT[/bold red]", border_style="red"))
    
    # Final pause so people can read the prediction in the video
    time.sleep(10) 
    console.print("\n[bold dim cyan]>> SATELLITE DISCONNECTED. MISSION ARCHIVED. <<[/bold dim cyan]")

if __name__ == "__main__":
    try: biometric_scan(); run_simulation()
    except KeyboardInterrupt: sys.exit(0)
    except Exception as e: console.print(f"[red]FATAL ERROR: {e}[/red]")
