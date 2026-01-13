import time
import requests
import psutil
import platform
import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.prompt import Prompt

console = Console()

def get_network_health():
    """Solves the 'Is my internet slow?' problem."""
    try:
        start = time.time()
        requests.get("https://1.1.1.1", timeout=2) # Cloudflare DNS is fastest for testing
        latency = int((time.time() - start) * 1000)
        if latency < 50: return f"[bold green]{latency}ms (Excellent)[/]"
        if latency < 150: return f"[bold yellow]{latency}ms (Stable)[/]"
        return f"[bold red]{latency}ms (High Latency)[/]"
    except:
        return "[bold red]OFFLINE[/]"

def get_bloatware_alerts():
    """Identifies resource-heavy processes that might need closing."""
    alerts = []
    for proc in psutil.process_iter(['name', 'memory_percent']):
        try:
            # If a single process takes more than 10% of total RAM, flag it
            if proc.info['memory_percent'] > 10.0:
                alerts.append(f"⚠️ [bold yellow]{proc.info['name']}[/] is consuming [red]{proc.info['memory_percent']:.1f}%[/] RAM")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return alerts if alerts else [" [green]No resource hogs detected.[/]"]

def fetch_github_data(user):
    try:
        r = requests.get(f"https://api.github.com/users/{user}/repos", timeout=5)
        if r.status_code == 200:
            return sorted(r.json(), key=lambda x: x.get('stargazers_count', 0), reverse=True)[:3]
        return []
    except:
        return []

def make_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", minimum_size=15),
        Layout(name="footer", size=6)
    )
    layout["body"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=1)
    )
    return layout

def update_content(layout, user, github_repos):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Header
    layout["header"].update(Panel(
        f"[bold white]SENTINEL PRO[/] | [cyan]NODE: {platform.node()}[/] | [green]NET: {get_network_health()}[/] | [yellow]{now}[/]",
        border_style="bright_blue"
    ))

    # Left Panel: Project Intelligence
    github_table = Table(title="[bold cyan]Project & Dev Stats", border_style="cyan", expand=True)
    github_table.add_column("Repository", style="bold white")
    github_table.add_column("Language", style="magenta")
    github_table.add_column("Stars", justify="right")
    
    if github_repos:
        for repo in github_repos:
            github_table.add_row(repo['name'], repo['language'] or "N/A", f"{repo['stargazers_count']} ⭐")
    else:
        github_table.add_row("No Data Found", "-", "-")
    layout["left"].update(Panel(github_table, border_style="cyan"))

    # Right Panel: Smart Diagnostics
    diag_table = Table(title="[bold red]Stability Monitor", border_style="red", expand=True)
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    
    diag_table.add_column("System Metric")
    diag_table.add_column("Value")
    diag_table.add_row("Global CPU Load", f"[{'red' if cpu > 80 else 'green'}]{cpu}%[/]")
    diag_table.add_row("Global RAM Usage", f"[{'red' if ram > 80 else 'green'}]{ram}%[/]")
    
    # Process Alerts in the table
    alerts = get_bloatware_alerts()
    for alert in alerts[:3]: # Show top 3 alerts
        diag_table.add_row("Alert", alert)
        
    layout["right"].update(Panel(diag_table, border_style="red"))

    # Footer: System Health Score
    health_score = 100 - (cpu/2 + ram/2)
    score_color = "green" if health_score > 70 else "yellow" if health_score > 40 else "red"
    
    layout["footer"].update(Panel(
        Text(f"SYSTEM HEALTH SCORE: {health_score:.1f}%", justify="center", style=f"bold {score_color}"),
        title="[bold white]Sentinel Analysis",
        subtitle="[dim]Real-time Hardware & API Monitoring Active[/]"
    ))

if __name__ == "__main__":
    console.clear()
    console.print(Panel.fit("[bold green]SENTINEL PRO v2.5[/]\nProfessional System & API Intelligence Terminal", border_style="green"))
    
    target_user = Prompt.ask("[bold yellow]Initiate Sync - Enter GitHub Username[/]")
    
    with console.status(f"[bold cyan]Connecting to GitHub APIs for {target_user}...", spinner="bouncingBar"):
        repos = fetch_github_data(target_user)
        time.sleep(1)

    app_layout = make_layout()
    with Live(app_layout, refresh_per_second=2, screen=True):
        try:
            while True:
                update_content(app_layout, target_user, repos)
                time.sleep(0.5)
        except KeyboardInterrupt:
            pass