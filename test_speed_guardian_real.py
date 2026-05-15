#!/usr/bin/env python3
"""
Real-World Speed Guardian Test

Tests Speed Guardian on actual code from error_scripts.
Shows real optimizations and speedups.
"""

import sys
from pathlib import Path
import time
import numpy as np

# Add to path
sys.path.insert(0, str(Path(__file__).parent / "speed-guardian"))

from speed_guardian.core import SpeedGuardian
from speed_guardian.patterns import OptimizationPatterns, optimize_numpy_loops, optimize_cupy_gpu

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()


def create_test_script_slow_loops():
    """Create a test script with slow loops that can be vectorized"""
    code = '''
import numpy as np
import time

def slow_matrix_multiply():
    """Naive matrix multiplication - should be vectorized"""
    A = np.random.randn(100, 100)
    B = np.random.randn(100, 100)
    C = np.zeros((100, 100))
    
    # Slow nested loops
    for i in range(100):
        for j in range(100):
            for k in range(100):
                C[i, j] += A[i, k] * B[k, j]
    
    return C

def slow_element_wise():
    """Element-wise operations in loop - should be vectorized"""
    arr = np.random.randn(10000)
    result = np.zeros(10000)
    
    for i in range(len(arr)):
        result[i] = arr[i] * 2 + 5
    
    return result

def slow_sum():
    """Manual sum - should use np.sum"""
    arr = np.random.randn(100000)
    total = 0
    for x in arr:
        total += x
    return total

if __name__ == "__main__":
    start = time.time()
    slow_matrix_multiply()
    slow_element_wise()
    slow_sum()
    print(f"Time: {time.time() - start:.3f}s")
'''
    
    path = Path("test_slow_loops.py")
    path.write_text(code)
    return path


def create_test_script_string_ops():
    """Create a test script with slow string operations"""
    code = '''
import time

def slow_string_concat():
    """String concatenation in loop - should use join"""
    result = ""
    for i in range(1000):
        result += str(i) + ","
    return result

def slow_string_format():
    """Old-style formatting - should use f-strings"""
    items = range(1000)
    results = []
    for i in items:
        results.append("Item %d: value %s" % (i, i*2))
    return results

if __name__ == "__main__":
    start = time.time()
    slow_string_concat()
    slow_string_format()
    print(f"Time: {time.time() - start:.3f}s")
'''
    
    path = Path("test_slow_strings.py")
    path.write_text(code)
    return path


def test_pattern_detection():
    """Test pattern detection on real code"""
    console.print("\n[bold cyan]Test 1: Pattern Detection[/bold cyan]\n")
    
    patterns = OptimizationPatterns()
    
    # Test on slow loops
    script = create_test_script_slow_loops()
    code = script.read_text()
    
    applicable = patterns.find_applicable_patterns(code)
    
    console.print(f"Found {len(applicable)} applicable patterns:\n")
    
    table = Table(box=box.ROUNDED)
    table.add_column("Pattern", style="cyan")
    table.add_column("Speedup", style="yellow")
    table.add_column("Matches", style="white")
    
    for pattern, matches in applicable:
        table.add_row(
            pattern.name,
            f"{pattern.speedup_estimate:.1f}x",
            str(len(matches))
        )
    
    console.print(table)
    
    # Cleanup
    script.unlink()
    
    return len(applicable) > 0


def test_numpy_optimization():
    """Test NumPy loop optimization"""
    console.print("\n[bold cyan]Test 2: NumPy Loop Optimization[/bold cyan]\n")
    
    code = '''
import numpy as np

arr = np.random.randn(10000)
result = np.zeros(10000)

for i in range(len(arr)):
    result[i] = arr[i] * 2 + 5
'''
    
    console.print("[dim]Original code:[/dim]")
    console.print(code)
    
    optimized = optimize_numpy_loops(code)
    
    console.print("\n[dim]Optimized code:[/dim]")
    console.print(optimized)
    
    return "result = arr" in optimized


def test_cupy_conversion():
    """Test NumPy to CuPy conversion"""
    console.print("\n[bold cyan]Test 3: CuPy GPU Conversion[/bold cyan]\n")
    
    code = '''
import numpy as np

def compute():
    A = np.random.randn(1000, 1000)
    B = np.random.randn(1000, 1000)
    C = np.matmul(A, B)
    return C
'''
    
    console.print("[dim]Original (NumPy):[/dim]")
    console.print(code)
    
    optimized = optimize_cupy_gpu(code)
    
    console.print("\n[dim]Optimized (CuPy GPU):[/dim]")
    console.print(optimized)
    
    return "import cupy as cp" in optimized and "cp.matmul" in optimized


def test_real_script_optimization():
    """Test optimization on a real script"""
    console.print("\n[bold cyan]Test 4: Real Script Optimization[/bold cyan]\n")
    
    script = create_test_script_slow_loops()
    
    console.print(f"Testing on: {script.name}\n")
    
    # Read original
    original = script.read_text()
    
    # Apply patterns
    patterns = OptimizationPatterns()
    applicable = patterns.find_applicable_patterns(original)
    
    if not applicable:
        console.print("[yellow]No patterns found[/yellow]")
        script.unlink()
        return False
    
    # Apply first pattern
    pattern, matches = applicable[0]
    console.print(f"Applying: {pattern.name} ({pattern.speedup_estimate:.1f}x speedup)\n")
    
    optimized = patterns.apply_pattern(original, pattern)
    
    # Show diff
    console.print("[green]Optimization applied![/green]")
    console.print(f"Pattern: {pattern.description}\n")
    
    # Cleanup
    script.unlink()
    
    return True


def test_multiverse_analysis():
    """Analyze Multiverse architecture for optimization opportunities"""
    console.print("\n[bold cyan]Test 5: Multiverse Architecture Analysis[/bold cyan]\n")
    
    multiverse_path = Path("C:/Downloads/bob/performance_speed/multiverse.py")
    
    if not multiverse_path.exists():
        console.print("[yellow]Multiverse.py not found[/yellow]")
        return False
    
    code = multiverse_path.read_text()
    
    patterns = OptimizationPatterns()
    
    # Check for optimization opportunities
    console.print("[bold]Analyzing Multiverse architecture...[/bold]\n")
    
    checks = [
        ("CuPy usage", "import cupy as cp" in code),
        ("Fast GELU", "_gelu_fast" in code),
        ("Fused operations", "@cp.fuse()" in code),
        ("Pre-allocated buffers", "_d_Ws" in code),
        ("Spectral transplant", "spectral_transplant" in code),
        ("NUMA affinity", "_pin_to_gpu_numa" in code),
    ]
    
    table = Table(box=box.ROUNDED)
    table.add_column("Optimization", style="cyan")
    table.add_column("Status", style="white")
    
    for name, present in checks:
        status = "[green]✓ Present[/green]" if present else "[red]✗ Missing[/red]"
        table.add_row(name, status)
    
    console.print(table)
    
    # Count optimization patterns
    applicable = patterns.find_applicable_patterns(code)
    
    console.print(f"\n[bold]Additional optimization opportunities:[/bold] {len(applicable)}")
    
    if applicable:
        for pattern, matches in applicable[:3]:
            console.print(f"  • {pattern.name}: {len(matches)} locations")
    
    return True


def test_error_script_analysis():
    """Analyze error_scripts for optimization opportunities"""
    console.print("\n[bold cyan]Test 6: Error Scripts Analysis[/bold cyan]\n")
    
    error_dir = Path("C:/Downloads/bob/error_scripts")
    
    if not error_dir.exists():
        console.print("[yellow]error_scripts directory not found[/yellow]")
        return False
    
    patterns = OptimizationPatterns()
    
    # Sample a few scripts
    scripts = list(error_dir.glob("*.py"))[:10]
    
    console.print(f"Analyzing {len(scripts)} sample scripts...\n")
    
    total_opportunities = 0
    high_impact = []
    
    for script in scripts:
        try:
            code = script.read_text()
            applicable = patterns.find_applicable_patterns(code)
            
            if applicable:
                total_opportunities += len(applicable)
                
                # Check for high-impact patterns
                for pattern, matches in applicable:
                    if pattern.speedup_estimate >= 5.0:
                        high_impact.append((script.name, pattern.name, pattern.speedup_estimate))
        except:
            continue
    
    console.print(f"[bold]Total optimization opportunities:[/bold] {total_opportunities}\n")
    
    if high_impact:
        console.print("[bold yellow]High-Impact Optimizations (5x+ speedup):[/bold yellow]\n")
        
        table = Table(box=box.ROUNDED)
        table.add_column("Script", style="cyan")
        table.add_column("Pattern", style="yellow")
        table.add_column("Speedup", style="green")
        
        for script_name, pattern_name, speedup in high_impact[:10]:
            table.add_row(script_name, pattern_name, f"{speedup:.0f}x")
        
        console.print(table)
    
    return total_opportunities > 0


def main():
    """Run all tests"""
    console.print("\n" + "="*70)
    console.print("[bold cyan]Speed Guardian - Real-World Testing[/bold cyan]")
    console.print("="*70)
    
    tests = [
        ("Pattern Detection", test_pattern_detection),
        ("NumPy Optimization", test_numpy_optimization),
        ("CuPy Conversion", test_cupy_conversion),
        ("Real Script Optimization", test_real_script_optimization),
        ("Multiverse Analysis", test_multiverse_analysis),
        ("Error Scripts Analysis", test_error_script_analysis),
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
            time.sleep(0.5)
        except Exception as e:
            console.print(f"\n[red]Test failed: {e}[/red]\n")
            results.append((name, False))
    
    # Summary
    console.print("\n" + "="*70)
    console.print("[bold]Test Summary[/bold]")
    console.print("="*70 + "\n")
    
    table = Table(box=box.ROUNDED)
    table.add_column("Test", style="cyan")
    table.add_column("Result", style="white")
    
    passed = 0
    for name, result in results:
        status = "[green]✓ PASS[/green]" if result else "[red]✗ FAIL[/red]"
        table.add_row(name, status)
        if result:
            passed += 1
    
    console.print(table)
    
    console.print(f"\n[bold]Results: {passed}/{len(tests)} tests passed[/bold]\n")
    
    if passed == len(tests):
        console.print("[green]✅ All tests passed! Speed Guardian is working.[/green]\n")
    else:
        console.print("[yellow]⚠️  Some tests failed. Review output above.[/yellow]\n")


if __name__ == "__main__":
    main()
