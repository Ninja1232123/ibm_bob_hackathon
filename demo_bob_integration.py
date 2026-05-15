#!/usr/bin/env python3
"""
Demo: Bob Shell Integrated with DevMaster

This demo showcases how Bob Shell acts as the intelligent brain
powering the entire DevMaster ecosystem.

What Bob Does:
1. Monitors the nervous system for events
2. Learns from error patterns and fixes
3. Provides conversational guidance
4. Automates debugging workflows
5. Suggests next actions based on context
6. Generates insights about coding patterns

Run this demo to see Bob in action!
"""

import sys
import time
from pathlib import Path

# Add devmaster to path
sys.path.insert(0, str(Path(__file__).parent / "devmaster"))

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live
from rich.table import Table
from rich import box

from devmaster.bob_brain import BobBrain
from devmaster.nervous_system import NervousSystem, Event

console = Console()


def demo_header():
    """Display demo header."""
    console.print("\n" + "="*80)
    console.print("[bold cyan]BOB SHELL + DEVMASTER INTEGRATION DEMO[/bold cyan]")
    console.print("="*80 + "\n")
    
    console.print("[bold]What you'll see:[/bold]")
    console.print("  1. Bob monitoring the nervous system")
    console.print("  2. Bob learning from error patterns")
    console.print("  3. Bob providing intelligent suggestions")
    console.print("  4. Bob analyzing errors and suggesting fixes")
    console.print("  5. Bob generating insights about your code")
    console.print("\n[dim]Press Ctrl+C to skip ahead at any time[/dim]\n")
    time.sleep(2)


def demo_nervous_system():
    """Demo: Bob monitoring the nervous system."""
    console.print("\n[bold cyan]═══ DEMO 1: Bob Monitoring Nervous System ═══[/bold cyan]\n")
    
    console.print("Starting Bob Brain and Nervous System...")
    
    brain = BobBrain()
    brain.start()
    ns = NervousSystem()
    
    console.print("[green]✓[/green] Bob is now monitoring all tool events\n")
    
    # Simulate some events
    console.print("[yellow]Simulating tool events...[/yellow]\n")
    
    events = [
        Event(
            event_type='hotspot_detected',
            source_tool='codearchaeology',
            payload={'file_path': 'src/auth/login.py', 'churn_rate': 15, 'change_count': 50}
        ),
        Event(
            event_type='error_pattern_learned',
            source_tool='devmaster_learner',
            payload={'error_type': 'KeyError', 'pattern': "data['key']", 'frequency': 5}
        ),
        Event(
            event_type='fix_applied',
            source_tool='universal_debugger',
            payload={'error_type': 'KeyError', 'file_path': 'src/utils.py', 'fix_applied': "data.get('key')"}
        ),
    ]
    
    for event in events:
        console.print(f"[dim]→[/dim] {event.source_tool}: {event.event_type}")
        ns.publish(event)
        time.sleep(0.5)
    
    time.sleep(1)
    console.print(f"\n[green]✓[/green] Bob processed {len(events)} events")
    console.print(f"[dim]Bob is learning from these patterns...[/dim]\n")
    
    brain.stop()
    time.sleep(1)


def demo_error_analysis():
    """Demo: Bob analyzing errors."""
    console.print("\n[bold cyan]═══ DEMO 2: Bob Analyzing Errors ═══[/bold cyan]\n")
    
    brain = BobBrain()
    brain.start()
    
    # Simulate an error
    error_info = {
        'type': 'KeyError',
        'message': "KeyError: 'email'",
        'file': 'src/user_service.py',
        'line': 42
    }
    
    console.print("[yellow]Simulating error:[/yellow]")
    console.print(f"  File: {error_info['file']}, Line: {error_info['line']}")
    console.print(f"  Error: {error_info['message']}\n")
    
    console.print("[cyan]Bob is analyzing...[/cyan]\n")
    time.sleep(1)
    
    suggestion = brain.analyze_error(error_info)
    
    # Display Bob's analysis
    panel = Panel(
        f"[bold]Error Type:[/bold] {suggestion['error_type']}\n"
        f"[bold]Confidence:[/bold] {suggestion['confidence']}\n\n"
        f"[green]{suggestion['explanation']}[/green]\n\n"
        f"[bold yellow]Suggested Fix:[/bold yellow]\n"
        f"[green]{suggestion['suggested_fixes'][0]['fix'] if suggestion['suggested_fixes'] else 'Use .get() method'}[/green]\n\n"
        f"[dim]Reason: {suggestion['suggested_fixes'][0]['reason'] if suggestion['suggested_fixes'] else 'Safer dictionary access'}[/dim]",
        title="🧠 Bob's Analysis",
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(panel)
    console.print()
    
    brain.stop()
    time.sleep(2)


def demo_conversational():
    """Demo: Bob's conversational interface."""
    console.print("\n[bold cyan]═══ DEMO 3: Conversational Bob ═══[/bold cyan]\n")
    
    brain = BobBrain()
    brain.start()
    
    questions = [
        "What errors have I been making recently?",
        "What should I work on next?",
        "How can I improve my code quality?"
    ]
    
    for question in questions:
        console.print(f"[bold green]You:[/bold green] {question}\n")
        time.sleep(0.5)
        
        response = brain.ask(question)
        
        panel = Panel(
            Markdown(response),
            title="🧠 Bob",
            border_style="cyan",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()
        time.sleep(1.5)
    
    brain.stop()
    time.sleep(1)


def demo_insights():
    """Demo: Bob generating insights."""
    console.print("\n[bold cyan]═══ DEMO 4: Bob's Insights ═══[/bold cyan]\n")
    
    brain = BobBrain()
    brain.start()
    
    # Add some data for Bob to analyze
    brain.context.fixes_applied = 12
    brain.context.active_files = ['src/auth.py', 'src/api.py', 'src/db.py', 'src/utils.py', 'src/models.py', 'src/views.py']
    brain.knowledge['error_patterns'] = [
        {'error_type': 'KeyError', 'frequency': 8},
        {'error_type': 'TypeError', 'frequency': 5},
        {'error_type': 'AttributeError', 'frequency': 3}
    ]
    
    console.print("[cyan]Bob is analyzing your coding patterns...[/cyan]\n")
    time.sleep(1)
    
    insights = brain.get_insights()
    
    for insight in insights:
        if insight['type'] == 'achievement':
            color = "green"
            icon = "🎉"
        elif insight['type'] == 'warning':
            color = "yellow"
            icon = "⚠️"
        else:
            color = "blue"
            icon = "🔍"
        
        panel = Panel(
            f"[{color}]{insight['description']}[/{color}]\n\n"
            f"[dim]💡 {insight['suggestion']}[/dim]",
            title=f"{icon} {insight['title']}",
            border_style=color
        )
        console.print(panel)
        console.print()
        time.sleep(1)
    
    brain.stop()
    time.sleep(1)


def demo_session_summary():
    """Demo: Bob's session summary."""
    console.print("\n[bold cyan]═══ DEMO 5: Session Summary ═══[/bold cyan]\n")
    
    brain = BobBrain()
    brain.start()
    
    # Populate some session data
    brain.context.fixes_applied = 12
    brain.context.active_files = ['src/auth.py', 'src/api.py', 'src/db.py']
    brain.context.recent_errors = [
        {'type': 'KeyError', 'message': 'key not found'},
        {'type': 'TypeError', 'message': 'wrong type'},
    ]
    
    summary = brain.get_session_summary()
    
    # Create summary table
    table = Table(show_header=False, box=box.ROUNDED, title="🧠 Bob's Session Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="white")
    
    table.add_row("Session Duration", summary['duration'] or "Demo session")
    table.add_row("Fixes Applied", str(summary['fixes_applied']))
    table.add_row("Active Files", str(summary['active_files']))
    table.add_row("Errors Encountered", str(summary['errors_encountered']))
    
    console.print(table)
    console.print()
    
    # Next action suggestion
    next_action = brain.suggest_next_action()
    console.print(f"[bold yellow]💡 Bob Suggests:[/bold yellow]")
    console.print(f"   {next_action}\n")
    
    brain.stop()
    time.sleep(2)


def demo_integration_architecture():
    """Show the integration architecture."""
    console.print("\n[bold cyan]═══ INTEGRATION ARCHITECTURE ═══[/bold cyan]\n")
    
    architecture = """
    ┌─────────────────────────────────────────────────────────────┐
    │                      BOB SHELL (AI Brain)                    │
    │  • Natural Language Understanding                            │
    │  • Context-Aware Reasoning                                   │
    │  • Pattern Learning & Recognition                            │
    └─────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                    BOB BRAIN (Intelligence Layer)            │
    │  • Event Monitoring                                          │
    │  • Error Analysis                                            │
    │  • Insight Generation                                        │
    │  • Conversational Interface                                  │
    └─────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                  NERVOUS SYSTEM (Event Bus)                  │
    │  • Cross-Tool Communication                                  │
    │  • Event Publishing & Subscription                           │
    │  • Integration Triggers                                      │
    └───┬─────────┬─────────┬─────────┬─────────┬─────────┬──────┘
        │         │         │         │         │         │
        ▼         ▼         ▼         ▼         ▼         ▼
    ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
    │Universal││CodeSeek││DevNarra││CodeArch││Deploy  ││Type    │
    │Debugger││        ││tive    ││aeology ││Shield  ││Guardian│
    └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
    """
    
    console.print(architecture)
    console.print("\n[bold]Key Integration Points:[/bold]")
    console.print("  1. Bob monitors ALL tool events via Nervous System")
    console.print("  2. Bob learns from error patterns and fixes")
    console.print("  3. Bob provides intelligent suggestions based on context")
    console.print("  4. Bob automates workflows by orchestrating tools")
    console.print("  5. Bob maintains persistent knowledge across sessions\n")
    
    time.sleep(3)


def demo_cli_commands():
    """Show available CLI commands."""
    console.print("\n[bold cyan]═══ AVAILABLE CLI COMMANDS ═══[/bold cyan]\n")
    
    commands = [
        ("devmaster bob ask", "Ask Bob a question", "devmaster bob ask 'How do I fix this error?'"),
        ("devmaster bob ask -i", "Interactive conversation with Bob", "devmaster bob ask --interactive"),
        ("devmaster bob insights", "Get Bob's insights about your code", "devmaster bob insights"),
        ("devmaster bob status", "Show Bob's current status", "devmaster bob status"),
        ("devmaster bob analyze-error", "Have Bob analyze an error", "devmaster bob analyze-error TypeError --file app.py"),
        ("devmaster bob watch", "Start Bob's watch mode", "devmaster bob watch"),
        ("devmaster bob teach", "Teach Bob your preferences", "devmaster bob teach"),
        ("devmaster bob report", "Generate Bob's activity report", "devmaster bob report --export report.json"),
    ]
    
    table = Table(show_header=True, box=box.ROUNDED)
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="white")
    table.add_column("Example", style="dim")
    
    for cmd, desc, example in commands:
        table.add_row(cmd, desc, example)
    
    console.print(table)
    console.print()
    time.sleep(2)


def main():
    """Run the complete demo."""
    try:
        demo_header()
        demo_nervous_system()
        demo_error_analysis()
        demo_conversational()
        demo_insights()
        demo_session_summary()
        demo_integration_architecture()
        demo_cli_commands()
        
        # Final message
        console.print("\n" + "="*80)
        console.print("[bold green]DEMO COMPLETE![/bold green]")
        console.print("="*80 + "\n")
        
        console.print("[bold]What You Just Saw:[/bold]")
        console.print("  ✓ Bob monitoring and learning from tool events")
        console.print("  ✓ Bob analyzing errors and suggesting fixes")
        console.print("  ✓ Bob providing conversational guidance")
        console.print("  ✓ Bob generating insights about coding patterns")
        console.print("  ✓ Bob maintaining context across sessions")
        
        console.print("\n[bold cyan]Try It Yourself:[/bold cyan]")
        console.print("  1. Install DevMaster: pip install -e devmaster")
        console.print("  2. Start Bob: devmaster bob ask --interactive")
        console.print("  3. Let Bob help you code!")
        
        console.print("\n[bold yellow]For the Hackathon:[/bold yellow]")
        console.print("  • Bob Shell is MEANINGFULLY integrated as the AI brain")
        console.print("  • Bob powers intelligent debugging, learning, and guidance")
        console.print("  • Bob orchestrates all tools through the nervous system")
        console.print("  • Bob provides real-time assistance and automation")
        
        console.print("\n[dim]This is not just using AI to write code.")
        console.print("This is AI AS the intelligent system powering development.[/dim]\n")
        
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Demo interrupted. Thanks for watching![/yellow]\n")
    except Exception as e:
        console.print(f"\n[red]Demo error: {e}[/red]\n")


if __name__ == "__main__":
    main()
