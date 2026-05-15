#!/usr/bin/env python3
"""
Speed Guardian + DevMaster Nervous System Integration Demo

Demonstrates how Speed Guardian integrates with the DevMaster ecosystem:
1. Publishes performance events to nervous system
2. Subscribes to events from other tools
3. Learns from Bob Brain's knowledge
4. Shares optimization patterns with the learner

This is the "living, breathing" version where tools talk to each other.
"""

import sys
import time
from pathlib import Path

# Add paths
sys.path.insert(0, str(Path(__file__).parent / "speed-guardian"))
sys.path.insert(0, str(Path(__file__).parent / "devmaster"))

from speed_guardian.core_with_nervous import SpeedGuardianCore
from speed_guardian.nervous_integration import get_integration

# Try to import nervous system
try:
    from devmaster.nervous_system import NervousSystem, Event
    from devmaster.bob_brain import BobBrain
    from devmaster.learner import CodingLearner
    NERVOUS_SYSTEM_AVAILABLE = True
except ImportError:
    NERVOUS_SYSTEM_AVAILABLE = False
    print("⚠️  DevMaster nervous system not available - running in standalone mode")


def demo_event_publishing():
    """Demo: Speed Guardian publishes events."""
    print("\n" + "="*70)
    print("DEMO 1: Event Publishing")
    print("="*70)
    print("\nSpeed Guardian finds bottlenecks and publishes events...")
    
    integration = get_integration()
    
    # Simulate finding a bottleneck
    finding = {
        'pattern_name': 'loop_with_append',
        'severity': 'HIGH',
        'line_number': 42,
        'estimated_speedup': 5.0,
        'description': 'Loop appending to list - vectorize with NumPy'
    }
    
    print(f"\n🔍 Bottleneck detected:")
    print(f"   Pattern: {finding['pattern_name']}")
    print(f"   Severity: {finding['severity']}")
    print(f"   Line: {finding['line_number']}")
    print(f"   Estimated speedup: {finding['estimated_speedup']}x")
    
    if integration:
        integration.publish_bottleneck_detected("demo_file.py", finding)
        print("\n✅ Event published to nervous system!")
        print("   Other tools can now react to this bottleneck")
    else:
        print("\n⚠️  Nervous system not available")


def demo_optimization_learning():
    """Demo: Speed Guardian learns from optimizations."""
    print("\n" + "="*70)
    print("DEMO 2: Learning from Optimizations")
    print("="*70)
    print("\nSpeed Guardian records successful optimizations...")
    
    integration = get_integration()
    
    # Simulate applying an optimization
    optimization = {
        'pattern_name': 'loop_vectorization',
        'lines_changed': 5,
        'optimization_type': 'loop',
        'before_code': 'for i in range(len(data)):\n    result.append(data[i] * 2)',
        'after_code': 'result = np.array(data) * 2'
    }
    
    print(f"\n🔧 Optimization applied:")
    print(f"   Pattern: {optimization['pattern_name']}")
    print(f"   Type: {optimization['optimization_type']}")
    print(f"   Lines changed: {optimization['lines_changed']}")
    
    print(f"\n   Before:")
    for line in optimization['before_code'].split('\n'):
        print(f"      {line}")
    
    print(f"\n   After:")
    for line in optimization['after_code'].split('\n'):
        print(f"      {line}")
    
    if integration:
        integration.publish_optimization_applied("demo_file.py", optimization)
        print("\n✅ Optimization recorded in learner database!")
        print("   Future runs will prioritize similar patterns")
    else:
        print("\n⚠️  Nervous system not available")


def demo_speedup_verification():
    """Demo: Speed Guardian verifies and publishes speedups."""
    print("\n" + "="*70)
    print("DEMO 3: Speedup Verification")
    print("="*70)
    print("\nSpeed Guardian verifies actual performance improvements...")
    
    integration = get_integration()
    
    # Simulate speedup verification
    speedup = {
        'pattern_name': 'loop_vectorization',
        'speedup_factor': 4.2,
        'before_time': 1.5,
        'after_time': 0.357,
        'verified': True
    }
    
    print(f"\n⚡ Speedup verified:")
    print(f"   Pattern: {speedup['pattern_name']}")
    print(f"   Before: {speedup['before_time']:.3f}s")
    print(f"   After: {speedup['after_time']:.3f}s")
    print(f"   Speedup: {speedup['speedup_factor']:.1f}x faster!")
    
    if integration:
        integration.publish_speedup_achieved("demo_file.py", speedup)
        print("\n✅ Speedup recorded as progress metric!")
        print("   Bob Brain can now track your performance improvements")
    else:
        print("\n⚠️  Nervous system not available")


def demo_cross_tool_integration():
    """Demo: Speed Guardian reacts to other tools."""
    print("\n" + "="*70)
    print("DEMO 4: Cross-Tool Integration")
    print("="*70)
    print("\nSpeed Guardian subscribes to events from other tools...")
    
    if not NERVOUS_SYSTEM_AVAILABLE:
        print("\n⚠️  Nervous system not available - skipping demo")
        return
    
    integration = get_integration()
    nervous_system = NervousSystem()
    
    print("\n📡 Subscribed to events:")
    print("   - fix_applied (from Universal Debugger)")
    print("   - code_indexed (from CodeSeek)")
    print("   - error_pattern_learned (from Learner)")
    
    # Simulate Universal Debugger fixing code
    print("\n🔧 Universal Debugger fixes an error...")
    event = Event(
        event_type='fix_applied',
        source_tool='universal_debugger',
        payload={
            'file_path': 'demo_file.py',
            'error_type': 'TypeError',
            'fix_type': 'type_conversion'
        }
    )
    nervous_system.publish(event)
    print("   ✅ Speed Guardian queued file for performance check")
    print("   (Some fixes can introduce performance issues)")
    
    # Simulate CodeSeek indexing new code
    print("\n📚 CodeSeek indexes new code...")
    event = Event(
        event_type='code_indexed',
        source_tool='codeseek',
        payload={
            'file_path': 'new_module.py',
            'functions': 15,
            'classes': 3
        }
    )
    nervous_system.publish(event)
    print("   ✅ Speed Guardian will profile new code")
    print("   (Creates baseline performance profile)")
    
    # Simulate Learner detecting error pattern
    print("\n🧠 Learner detects performance-related error...")
    event = Event(
        event_type='error_pattern_learned',
        source_tool='devmaster_learner',
        payload={
            'pattern_type': 'error',
            'error_type': 'TimeoutError',
            'frequency': 5
        }
    )
    nervous_system.publish(event)
    print("   ✅ Speed Guardian flagged for investigation")
    print("   (Timeout errors often indicate performance issues)")


def demo_learned_patterns():
    """Demo: Speed Guardian retrieves learned patterns."""
    print("\n" + "="*70)
    print("DEMO 5: Learned Optimization Patterns")
    print("="*70)
    print("\nSpeed Guardian retrieves patterns learned from previous runs...")
    
    integration = get_integration()
    
    if not integration:
        print("\n⚠️  Nervous system not available - skipping demo")
        return
    
    patterns = integration.get_learned_optimizations()
    
    if patterns:
        print(f"\n📚 Found {len(patterns)} learned pattern(s):")
        for i, pattern in enumerate(patterns[:5], 1):
            print(f"\n   {i}. {pattern['name']}")
            print(f"      Frequency: {pattern['frequency']} times")
            print(f"      Confidence: {pattern['confidence']:.1%}")
            print(f"      Description: {pattern['description']}")
    else:
        print("\n📚 No patterns learned yet")
        print("   Run Speed Guardian on your code to start learning!")


def demo_bob_brain_integration():
    """Demo: Bob Brain uses Speed Guardian data."""
    print("\n" + "="*70)
    print("DEMO 6: Bob Brain Integration")
    print("="*70)
    print("\nBob Brain monitors Speed Guardian and provides insights...")
    
    if not NERVOUS_SYSTEM_AVAILABLE:
        print("\n⚠️  Nervous system not available - skipping demo")
        return
    
    try:
        bob = BobBrain()
        bob.start()
        
        print("\n🧠 Bob Brain is monitoring:")
        print("   - Performance bottlenecks detected")
        print("   - Optimizations applied")
        print("   - Speedups achieved")
        
        print("\n💡 Bob can now:")
        print("   - Suggest when to run Speed Guardian")
        print("   - Identify performance-critical files")
        print("   - Track your optimization progress")
        print("   - Recommend optimization strategies")
        
        bob.stop()
        print("\n✅ Bob Brain integration active!")
        
    except Exception as e:
        print(f"\n⚠️  Bob Brain not available: {e}")


def demo_full_workflow():
    """Demo: Complete optimization workflow with ecosystem."""
    print("\n" + "="*70)
    print("DEMO 7: Complete Workflow")
    print("="*70)
    print("\nComplete optimization workflow with full ecosystem integration...")
    
    # Create a simple test file
    test_file = Path(__file__).parent / "test_optimization_demo.py"
    test_code = '''
import time

def slow_function(data):
    """A deliberately slow function for demo."""
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result

def another_slow_function(items):
    """Another slow function."""
    total = 0
    for item in items:
        total = total + item
    return total

if __name__ == "__main__":
    data = list(range(1000))
    result = slow_function(data)
    total = another_slow_function(result)
    print(f"Total: {total}")
'''
    
    print(f"\n📝 Creating test file: {test_file.name}")
    test_file.write_text(test_code)
    
    print("\n🚀 Running Speed Guardian with full integration...")
    
    try:
        core = SpeedGuardianCore(dry_run=True)
        result = core.optimize_file(str(test_file))
        
        print("\n📊 Results:")
        print(f"   Bottlenecks found: {result['findings']}")
        print(f"   Optimizations applied: {result['optimizations']}")
        print(f"   Session duration: {result['session_duration']:.2f}s")
        
        if NERVOUS_SYSTEM_AVAILABLE:
            print("\n🌐 Ecosystem Effects:")
            print("   ✅ Events published to nervous system")
            print("   ✅ Patterns recorded in learner database")
            print("   ✅ Bob Brain notified of optimizations")
            print("   ✅ Other tools can react to changes")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        # Cleanup
        if test_file.exists():
            test_file.unlink()
            print(f"\n🧹 Cleaned up test file")


def main():
    """Run all demos."""
    print("\n" + "="*70)
    print("Speed Guardian + DevMaster Nervous System Integration")
    print("="*70)
    print("\nThis demo shows how Speed Guardian integrates with the")
    print("DevMaster ecosystem to create a living, learning system.")
    
    if NERVOUS_SYSTEM_AVAILABLE:
        print("\n✅ Nervous system available - full integration active!")
    else:
        print("\n⚠️  Nervous system not available - some demos will be limited")
    
    input("\nPress ENTER to start demos...")
    
    # Run demos
    demo_event_publishing()
    input("\nPress ENTER for next demo...")
    
    demo_optimization_learning()
    input("\nPress ENTER for next demo...")
    
    demo_speedup_verification()
    input("\nPress ENTER for next demo...")
    
    demo_cross_tool_integration()
    input("\nPress ENTER for next demo...")
    
    demo_learned_patterns()
    input("\nPress ENTER for next demo...")
    
    demo_bob_brain_integration()
    input("\nPress ENTER for final demo...")
    
    demo_full_workflow()
    
    # Final summary
    print("\n" + "="*70)
    print("Demo Complete!")
    print("="*70)
    print("\n🎯 Key Takeaways:")
    print("   1. Speed Guardian publishes events to nervous system")
    print("   2. Other tools can react to performance events")
    print("   3. Optimizations are learned and reused")
    print("   4. Bob Brain monitors and provides insights")
    print("   5. The ecosystem gets smarter over time")
    
    print("\n💡 Next Steps:")
    print("   - Run Speed Guardian on your actual code")
    print("   - Let it learn your optimization patterns")
    print("   - Watch Bob Brain provide performance insights")
    print("   - See the ecosystem improve your workflow")
    
    print("\n🚀 The tools are alive and learning!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
