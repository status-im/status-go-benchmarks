#!/usr/bin/env python3
"""
Script to update README.md with the latest benchmark results.
Usage: python scripts/update_readme.py

Dependencies:
    pip install tabulate matplotlib
"""

import json
import os
import glob
from datetime import datetime, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def parse_directory_name(dir_name):
    """Parse directory name to extract timestamp and commit hash."""
    # Format: 20241208T172603_9207eaf
    parts = dir_name.split('_')
    if len(parts) != 2:
        return None, None
    
    timestamp_str = parts[0]
    commit_hash = parts[1]
    
    # Parse timestamp: 20241208T172603
    try:
        dt = datetime.strptime(timestamp_str, "%Y%m%dT%H%M%S")
        return dt, commit_hash
    except ValueError:
        return None, None


def load_benchmark_data(benchmark_dir):
    """Load benchmark data from JSON files in a directory."""
    data = {}
    json_files = glob.glob(os.path.join(benchmark_dir, "*.json"))
    
    for json_file in json_files:
        filename = os.path.basename(json_file)
        # Extract test name from filename
        test_name = filename.split('-')[0]  # e.g., "test_idle[waku_light_client_True]"
        
        with open(json_file, 'r') as f:
            data[test_name] = json.load(f)
    
    return data


def calculate_delta(current, previous):
    """Calculate percentage change between current and previous values."""
    if previous == 0:
        return "N/A" if current == 0 else "+∞"
    
    delta = ((current - previous) / previous) * 100
    if delta > 0:
        return f"(+{delta:.1f}%)"
    elif delta < 0:
        return f"({delta:.1f}%)"
    else:
        return "(0%)"


def format_bytes(bytes_value):
    """Format bytes to human readable format."""
    if bytes_value < 1024:
        return f"{bytes_value} B"
    elif bytes_value < 1024 * 1024:
        return f"{bytes_value / 1024:.1f} KB"
    else:
        return f"{bytes_value / (1024 * 1024):.2f} MB"


def format_memory(mb_value):
    """Format memory value."""
    return f"{mb_value:.2f} MB"


def get_metric_value(data, test_name, metric_path):
    """Extract metric value from nested data structure."""
    if test_name not in data:
        return None
    
    current = data[test_name]
    for key in metric_path:
        if key in current:
            current = current[key]
        else:
            return None
    return current


def load_historical_data(benchmarks_dir, days=365):
    """Load historical benchmark data from the last N days."""
    cutoff_date = datetime.now() - timedelta(days=days)
    
    # Get all benchmark directories
    benchmark_dirs = [d for d in os.listdir(benchmarks_dir) 
                     if os.path.isdir(os.path.join(benchmarks_dir, d))]
    
    historical_data = []
    
    for dir_name in benchmark_dirs:
        dt, commit_hash = parse_directory_name(dir_name)
        if dt and dt >= cutoff_date:
            dir_path = os.path.join(benchmarks_dir, dir_name)
            data = load_benchmark_data(dir_path)
            historical_data.append({
                'date': dt,
                'commit': commit_hash,
                'data': data
            })
    
    # Sort by date
    historical_data.sort(key=lambda x: x['date'])
    return historical_data


def create_history_plots(historical_data, output_dir="docs"):
    """Create 30-day history plots for each metric."""
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Test names and their display names
    test_configs = [
        ("test_idle[waku_light_client_True]", "Idle (Light Client)", "blue"),
        ("test_one_to_one_messages[waku_light_client_True]", "One-to-One (Light Client)", "green"), 
        ("test_one_to_one_messages[waku_light_client_False]", "One-to-One (Full Node)", "red")
    ]
    
    # Metrics configuration
    metrics_config = [
        ("CPU Median", ["metrics", "cpu", "median"], "%"),
        ("CPU Max", ["metrics", "cpu", "max"], "%"),
        ("RAM Median", ["metrics", "ram", "median"], "MB"),
        ("RAM Max", ["metrics", "ram", "max"], "MB"),
        ("RX Total", ["metrics", "network", "rx", "total_bytes"], "Bytes"),
        ("TX Total", ["metrics", "network", "tx", "total_bytes"], "Bytes"),
    ]
    
    # Create plots
    for metric_name, metric_path, unit in metrics_config:
        plt.figure(figsize=(12, 6))
        
        unit_display = unit  # Default unit display
        has_data = False  # Track if we have any data to plot
        
        # Plot each test configuration
        for test_name, display_name, color in test_configs:
            dates = []
            values = []
            
            for entry in historical_data:
                value = get_metric_value(entry['data'], test_name, metric_path)
                if value is not None:
                    dates.append(entry['date'])
                    # Convert bytes to KB/MB for better readability
                    if unit == "Bytes":
                        if value < 1024 * 1024:
                            value = value / 1024  # Convert to KB
                            unit_display = "KB"
                        else:
                            value = value / (1024 * 1024)  # Convert to MB
                            unit_display = "MB"
                    values.append(value)
            
            if dates and values:
                has_data = True
                plt.plot(dates, values, marker='o', label=display_name, color=color, linewidth=2, markersize=4)
        
        # Format the plot
        plt.title(f"{metric_name} - 30 Day History", fontsize=14, fontweight='bold')
        plt.xlabel("Date", fontsize=12)
        
        # Set y-label with appropriate unit
        if metric_name.startswith("CPU"):
            plt.ylabel("CPU Usage (%)", fontsize=12)
        elif metric_name.startswith("RAM"):
            plt.ylabel("Memory Usage (MB)", fontsize=12)
        elif "RX" in metric_name or "TX" in metric_name:
            plt.ylabel(f"Network Transfer ({unit_display})", fontsize=12)
        
        # Only add legend if we have data
        if has_data:
            plt.legend(loc='best')
        else:
            plt.text(0.5, 0.5, 'No data available for the last 30 days', 
                    ha='center', va='center', transform=plt.gca().transAxes, 
                    fontsize=12, alpha=0.7)
        
        # Set x-axis to show 30 days from the most recent data point
        if historical_data:
            # Find the most recent date in the data
            most_recent_date = max(entry['date'] for entry in historical_data)
            end_date = most_recent_date + timedelta(days=1)  # Add a small buffer
            start_date = most_recent_date - timedelta(days=30)
        else:
            # Fallback to current date if no data
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
        plt.xlim(start_date, end_date)
        
        # Format x-axis dates with more frequent marks
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Major ticks every 2 days
        plt.gca().xaxis.set_minor_locator(mdates.DayLocator(interval=1))  # Minor ticks every day
        plt.xticks(rotation=45)
        
        # Enable both major and minor grid lines
        plt.grid(True, which='major', alpha=0.5, linewidth=0.8)
        plt.grid(True, which='minor', alpha=0.2, linewidth=0.4)
        
        # Remove padding around the plot
        plt.tight_layout(pad=0.5)
        
        # Save plot
        filename = f"{metric_name.lower().replace(' ', '_')}_history.png"
        filepath = os.path.join(output_dir, filename)
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Created history plot: {filepath}")
    
    return output_dir


def create_history_plots_table(plots_dir):
    """Create a markdown table displaying the history plots."""
    
    # Organize plots into a 2x3 grid
    plot_files = [
        ("cpu_median_history.png", "cpu_max_history.png"),
        ("ram_median_history.png", "ram_max_history.png"),
        ("rx_total_history.png", "tx_total_history.png")
    ]
    
    table_rows = []
    
    for left_plot, right_plot in plot_files:
        left_path = os.path.join(plots_dir, left_plot)
        right_path = os.path.join(plots_dir, right_plot)
        
        left_img = f"![{left_plot}]({left_path})" if os.path.exists(left_path) else "N/A"
        right_img = f"![{right_plot}]({right_path})" if os.path.exists(right_path) else "N/A"
        
        table_rows.append([left_img, right_img])
    
    headers = ["Metric History", "Metric History"]
    return tabulate(table_rows, headers=headers, tablefmt="github")


def create_run_info_table(current_dir, previous_dir):
    """Create the run information table."""
    current_dt, current_commit = parse_directory_name(os.path.basename(current_dir))
    previous_dt, previous_commit = parse_directory_name(os.path.basename(previous_dir)) if previous_dir else (None, None)
    
    table_data = []
    
    if current_dt and current_commit:
        table_data.append([
            "Contender", 
            current_dt.strftime('%Y-%m-%d'), 
            current_dt.strftime('%H:%M:%S'), 
            f"`{current_commit}`"
        ])
    
    if previous_dt and previous_commit:
        table_data.append([
            "Baseline", 
            previous_dt.strftime('%Y-%m-%d'), 
            previous_dt.strftime('%H:%M:%S'), 
            f"`{previous_commit}`"
        ])
    
    headers = ["Run", "Date", "Time", "Commit"]
    return tabulate(table_data, headers=headers, tablefmt="github")


def create_metrics_table(current_dir, current_data, previous_data):
    """Create the main metrics table."""
    # Test names in order
    test_names = [
        "test_idle[waku_light_client_True]",
        "test_one_to_one_messages[waku_light_client_True]", 
        "test_one_to_one_messages[waku_light_client_False]"
    ]
    
    # Metrics to extract (excluding network errors)
    metrics = [
        ("CPU Median", ["metrics", "cpu", "median"], lambda x: f"{x:.2f}%"),
        ("CPU Max", ["metrics", "cpu", "max"], lambda x: f"{x:.2f}%"),
        ("RAM Median", ["metrics", "ram", "median"], format_memory),
        ("RAM Max", ["metrics", "ram", "max"], format_memory),
        ("RX Total", ["metrics", "network", "rx", "total_bytes"], format_bytes),
        ("TX Total", ["metrics", "network", "tx", "total_bytes"], format_bytes),
    ]
    
    # Build table data
    table_data = []
    
    for metric_name, metric_path, formatter in metrics:
        row = [metric_name]
        
        for test_name in test_names:
            current_value = get_metric_value(current_data, test_name, metric_path)
            previous_value = get_metric_value(previous_data, test_name, metric_path) if previous_data else None
            
            if current_value is not None:
                formatted_current = formatter(current_value)
                
                if previous_value is not None:
                    delta = calculate_delta(current_value, previous_value)
                    cell_content = f"{formatted_current} {delta}"
                else:
                    cell_content = formatted_current
            else:
                cell_content = "N/A"
            
            row.append(cell_content)
        
        table_data.append(row)
    
    # Add performance charts row
    chart_row = ["**Performance Chart**"]
    for test_name in test_names:
        # Find the corresponding image file using os.listdir to avoid glob escaping issues
        png_files = []
        if os.path.exists(current_dir):
            for filename in os.listdir(current_dir):
                if filename.startswith(test_name) and filename.endswith('.png'):
                    png_files.append(os.path.join(current_dir, filename))
        
        if png_files:
            # Use relative path from repository root
            rel_path = os.path.relpath(png_files[0], start=".")
            chart_row.append(f"![{test_name}]({rel_path})")
        else:
            chart_row.append("N/A")
    
    table_data.append(chart_row)
    
    # Create headers with line breaks for better readability
    headers = ["Metric"]
    for test_name in test_names:
        header_name = test_name.replace("[", "<br>[")
        headers.append(header_name)
    
    return tabulate(table_data, headers=headers, tablefmt="github")


def generate_readme_content(current_dir, previous_dir, current_data, previous_data, plots_dir):
    """Generate the complete README content."""
    
    # Start building README content
    content = [
        "# status-go-benchmarks",
        "",
        "Benchmark metrics with 30-day history and latest comparison.",
        ""
    ]
    
    # Add 30-day history section first
    content.append("## 30-Day History")
    content.append("")
    history_table = create_history_plots_table(plots_dir)
    content.append(history_table)
    content.append("")
    
    # Add date header for latest report
    current_date = datetime.now().strftime("%Y-%m-%d")
    content.append(f"## Latest Report ({current_date})")
    content.append("")
    
    # Add run comparison table
    run_table = create_run_info_table(current_dir, previous_dir)
    content.append(run_table)
    content.append("")
    
    # Add metrics table
    metrics_table = create_metrics_table(current_dir, current_data, previous_data)
    content.append(metrics_table)
    content.append("")
    
    return "\n".join(content)


def main():
    """Main function to update README."""
    # Change to repository root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    os.chdir(repo_root)
    
    benchmarks_dir = "benchmarks"
    
    if not os.path.exists(benchmarks_dir):
        print(f"Error: {benchmarks_dir} directory not found!")
        return
    
    # Get all benchmark directories sorted by name (newest first)
    benchmark_dirs = [d for d in os.listdir(benchmarks_dir) 
                     if os.path.isdir(os.path.join(benchmarks_dir, d))]
    benchmark_dirs.sort(reverse=True)
    
    if len(benchmark_dirs) < 1:
        print("Error: No benchmark directories found!")
        return
    
    # Get current (latest) and previous directories
    current_dir = os.path.join(benchmarks_dir, benchmark_dirs[0])
    previous_dir = os.path.join(benchmarks_dir, benchmark_dirs[1]) if len(benchmark_dirs) > 1 else None
    
    print(f"Loading current benchmark data from: {current_dir}")
    current_data = load_benchmark_data(current_dir)
    
    previous_data = None
    if previous_dir:
        print(f"Loading previous benchmark data from: {previous_dir}")
        previous_data = load_benchmark_data(previous_dir)
    
    # Load historical data and create plots
    print("Loading historical data for 30-day trends...")
    historical_data = load_historical_data(benchmarks_dir)
    print(f"Found {len(historical_data)} historical benchmark runs")
    
    print("Creating 30-day history plots...")
    plots_dir = create_history_plots(historical_data)
    
    # Generate README content
    readme_content = generate_readme_content(current_dir, previous_dir, current_data, previous_data, plots_dir)
    
    # Write to README.md
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print("README.md updated successfully!")


if __name__ == "__main__":
    main()
