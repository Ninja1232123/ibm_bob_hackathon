#!/usr/bin/env python3
"""
Explore DevMaster databases to understand what's stored and find insights
"""

import sqlite3
from pathlib import Path
import json

def explore_database(db_path: Path):
    """Explore a SQLite database and show its structure and sample data"""
    print(f"\n{'='*70}")
    print(f"Database: {db_path.name}")
    print(f"{'='*70}\n")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        print(f"Tables found: {len(tables)}")
        print(f"  {', '.join(tables)}\n")
        
        # Explore each table
        for table in tables:
            print(f"\n--- Table: {table} ---")
            
            # Get schema
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            print(f"Columns: {len(columns)}")
            for col in columns:
                print(f"  - {col[1]} ({col[2]})")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"Rows: {count}")
            
            # Show sample data (first 5 rows)
            if count > 0:
                cursor.execute(f"SELECT * FROM {table} LIMIT 5")
                rows = cursor.fetchall()
                print(f"\nSample data (first {min(5, count)} rows):")
                for i, row in enumerate(rows, 1):
                    print(f"  Row {i}:")
                    for col_idx, col_info in enumerate(columns):
                        col_name = col_info[1]
                        value = row[col_idx]
                        # Truncate long values
                        if isinstance(value, str) and len(value) > 100:
                            value = value[:100] + "..."
                        print(f"    {col_name}: {value}")
        
        conn.close()
        
    except Exception as e:
        print(f"Error exploring {db_path.name}: {e}")


def main():
    """Explore all DevMaster databases"""
    print("\n" + "="*70)
    print("DevMaster Database Explorer")
    print("="*70)
    
    # Find databases
    base_path = Path(__file__).parent.parent
    db_files = [
        base_path / "kb.db",
        base_path / "learner.db",
        base_path / "nervous_system.db",
    ]
    
    for db_file in db_files:
        if db_file.exists():
            explore_database(db_file)
        else:
            print(f"\n⚠️  Database not found: {db_file}")
    
    print("\n" + "="*70)
    print("Exploration complete!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
