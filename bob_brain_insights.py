#!/usr/bin/env python3
"""
Bob Brain Insights - Interactive Intelligence Dashboard

Shows what Bob has learned about your coding style, patterns, and preferences.
Provides actionable insights and proactive suggestions.
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Tuple

class BobBrainInsights:
    """Interactive insights from Bob's learning databases"""
    
    def __init__(self, base_path: Path = None):
        if base_path is None:
            # Database files are in C:\Downloads\bob
            base_path = Path(__file__).parent.parent
        
        self.kb_db = base_path / "kb.db"
        self.learner_db = base_path / "learner.db"
        self.nervous_db = base_path / "nervous_system.db"
        
    def get_coding_style_profile(self) -> Dict:
        """Analyze learned coding patterns and preferences"""
        if not self.learner_db.exists():
            return {}
        
        conn = sqlite3.connect(self.learner_db)
        cursor = conn.cursor()
        
        # Get patterns
        cursor.execute("""
            SELECT pattern_type, name, description, frequency, confidence
            FROM patterns
            ORDER BY confidence DESC, frequency DESC
        """)
        patterns = cursor.fetchall()
        
        # Get preferences
        cursor.execute("""
            SELECT category, preference_key, preference_value, confidence, evidence_count
            FROM preferences
            ORDER BY confidence DESC
        """)
        preferences = cursor.fetchall()
        
        conn.close()
        
        return {
            'patterns': patterns,
            'preferences': preferences
        }
    
    def get_error_intelligence(self) -> Dict:
        """Analyze error patterns and learning"""
        if not self.learner_db.exists():
            return {}
        
        conn = sqlite3.connect(self.learner_db)
        cursor = conn.cursor()
        
        # Most common errors
        cursor.execute("""
            SELECT error_type, COUNT(*) as count
            FROM error_history
            GROUP BY error_type
            ORDER BY count DESC
            LIMIT 10
        """)
        common_errors = cursor.fetchall()
        
        # Fixed vs unfixed
        cursor.execute("""
            SELECT 
                SUM(CASE WHEN fixed = 1 THEN 1 ELSE 0 END) as fixed,
                SUM(CASE WHEN fixed = 0 THEN 1 ELSE 0 END) as unfixed
            FROM error_history
        """)
        fix_stats = cursor.fetchone()
        
        # Recent errors
        cursor.execute("""
            SELECT error_type, error_message, file_path, occurred_at
            FROM error_history
            ORDER BY occurred_at DESC
            LIMIT 5
        """)
        recent_errors = cursor.fetchall()
        
        conn.close()
        
        return {
            'common_errors': common_errors,
            'fix_stats': fix_stats,
            'recent_errors': recent_errors
        }
    
    def get_progress_metrics(self) -> Dict:
        """Get development progress over time"""
        if not self.learner_db.exists():
            return {}
        
        conn = sqlite3.connect(self.learner_db)
        cursor = conn.cursor()
        
        # Progress metrics
        cursor.execute("""
            SELECT metric_name, value, recorded_at
            FROM progress
            ORDER BY recorded_at DESC
        """)
        metrics = cursor.fetchall()
        
        # Session stats
        cursor.execute("""
            SELECT 
                COUNT(*) as total_sessions,
                SUM(files_changed) as total_files,
                SUM(lines_added) as total_added,
                SUM(lines_removed) as total_removed
            FROM sessions
        """)
        session_stats = cursor.fetchone()
        
        conn.close()
        
        return {
            'metrics': metrics,
            'session_stats': session_stats
        }
    
    def get_ecosystem_activity(self) -> Dict:
        """Get nervous system activity and tool coordination"""
        if not self.nervous_db.exists():
            return {}
        
        conn = sqlite3.connect(self.nervous_db)
        cursor = conn.cursor()
        
        # Event types
        cursor.execute("""
            SELECT event_type, COUNT(*) as count
            FROM events
            GROUP BY event_type
            ORDER BY count DESC
        """)
        event_types = cursor.fetchall()
        
        # Tool activity
        cursor.execute("""
            SELECT source_tool, COUNT(*) as count
            FROM events
            GROUP BY source_tool
            ORDER BY count DESC
        """)
        tool_activity = cursor.fetchall()
        
        # Integration stats
        cursor.execute("""
            SELECT source_event, target_tool, trigger_count, enabled
            FROM integrations
            ORDER BY trigger_count DESC
        """)
        integrations = cursor.fetchall()
        
        # Recent events
        cursor.execute("""
            SELECT event_type, source_tool, timestamp
            FROM events
            ORDER BY created_at DESC
            LIMIT 10
        """)
        recent_events = cursor.fetchall()
        
        conn.close()
        
        return {
            'event_types': event_types,
            'tool_activity': tool_activity,
            'integrations': integrations,
            'recent_events': recent_events
        }
    
    def get_actionable_insights(self) -> List[Dict]:
        """Get actionable insights and suggestions"""
        if not self.learner_db.exists():
            return []
        
        conn = sqlite3.connect(self.learner_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT category, title, description, suggestion, actionable
            FROM insights
            WHERE actionable = 1 AND acknowledged = 0
            ORDER BY id DESC
            LIMIT 10
        """)
        insights = cursor.fetchall()
        
        conn.close()
        
        return [
            {
                'category': row[0],
                'title': row[1],
                'description': row[2],
                'suggestion': row[3]
            }
            for row in insights
        ]
    
    def display_dashboard(self):
        """Display comprehensive insights dashboard"""
        print("\n" + "="*70)
        print("🧠 Bob Brain Insights Dashboard")
        print("="*70)
        
        # Coding Style Profile
        print("\n" + "─"*70)
        print("📊 Your Coding Style Profile")
        print("─"*70)
        
        style = self.get_coding_style_profile()
        if style.get('patterns'):
            print("\n🎯 Learned Patterns:")
            for ptype, name, desc, freq, conf in style['patterns'][:5]:
                print(f"\n  • {name.replace('_', ' ').title()}")
                print(f"    Type: {ptype}")
                print(f"    {desc}")
                print(f"    Frequency: {freq} occurrences")
                print(f"    Confidence: {conf:.1%}")
        
        if style.get('preferences'):
            print("\n💡 Your Preferences:")
            for cat, key, value, conf, evidence in style['preferences']:
                print(f"\n  • {key.replace('_', ' ').title()}: {value.replace('_', ' ').title()}")
                print(f"    Category: {cat}")
                print(f"    Confidence: {conf:.1%} (based on {evidence} examples)")
        
        # Error Intelligence
        print("\n" + "─"*70)
        print("🔍 Error Intelligence")
        print("─"*70)
        
        errors = self.get_error_intelligence()
        if errors.get('common_errors'):
            print("\n⚠️  Most Common Errors:")
            for error_type, count in errors['common_errors'][:5]:
                print(f"  • {error_type}: {count:,} occurrences")
        
        if errors.get('fix_stats'):
            fixed, unfixed = errors['fix_stats']
            total = fixed + unfixed
            if total > 0:
                fix_rate = (fixed / total) * 100
                print(f"\n✅ Fix Rate: {fix_rate:.1f}%")
                print(f"   Fixed: {fixed:,} | Unfixed: {unfixed:,}")
        
        # Progress Metrics
        print("\n" + "─"*70)
        print("📈 Development Progress")
        print("─"*70)
        
        progress = self.get_progress_metrics()
        if progress.get('session_stats'):
            sessions, files, added, removed = progress['session_stats']
            print(f"\n📊 Overall Stats:")
            print(f"  • Total Sessions: {sessions}")
            print(f"  • Files Changed: {files:,}")
            print(f"  • Lines Added: {added:,}")
            print(f"  • Lines Removed: {removed:,}")
        
        # Ecosystem Activity
        print("\n" + "─"*70)
        print("🌐 Ecosystem Activity")
        print("─"*70)
        
        ecosystem = self.get_ecosystem_activity()
        if ecosystem.get('tool_activity'):
            print("\n🔧 Tool Activity:")
            for tool, count in ecosystem['tool_activity'][:5]:
                print(f"  • {tool}: {count} events")
        
        if ecosystem.get('event_types'):
            print("\n📡 Event Types:")
            for event_type, count in ecosystem['event_types'][:5]:
                print(f"  • {event_type}: {count} times")
        
        if ecosystem.get('integrations'):
            print("\n🔗 Active Integrations:")
            active = [i for i in ecosystem['integrations'] if i[3] == 1]
            for source, target, triggers, _ in active[:5]:
                print(f"  • {source} → {target}: {triggers} triggers")
        
        # Actionable Insights
        print("\n" + "─"*70)
        print("💡 Actionable Insights")
        print("─"*70)
        
        insights = self.get_actionable_insights()
        if insights:
            for insight in insights[:3]:
                print(f"\n  📌 {insight['title']}")
                print(f"     {insight['description']}")
                if insight['suggestion']:
                    print(f"     💡 Suggestion: {insight['suggestion']}")
        else:
            print("\n  ✨ No pending insights - you're doing great!")
        
        # Summary
        print("\n" + "="*70)
        print("🎯 Summary")
        print("="*70)
        
        total_patterns = len(style.get('patterns', []))
        total_errors = sum(count for _, count in errors.get('common_errors', []))
        total_events = sum(count for _, count in ecosystem.get('event_types', []))
        
        print(f"\n  Bob has learned:")
        print(f"    • {total_patterns} coding patterns")
        print(f"    • {total_errors:,} error patterns")
        print(f"    • {total_events} ecosystem events")
        print(f"\n  The ecosystem is alive and learning! 🚀")
        print("="*70 + "\n")


def main():
    """Run the insights dashboard"""
    dashboard = BobBrainInsights()
    dashboard.display_dashboard()


if __name__ == "__main__":
    main()
