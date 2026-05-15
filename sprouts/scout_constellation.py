import json
import subprocess
import random
import hashlib
import os

def get_contributions():
    """Fetches my global contributions using the GitHub CLI."""
    try:
        # Search for both issues and PRs created by me
        cmd = [
            "gh", "search", "issues", 
            "--author", "Manamama-Gemini-Cloud-AI-01", 
            "--limit", "100", 
            "--json", "repository"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        counts = {}
        for item in data:
            repo = item["repository"]["nameWithOwner"]
            counts[repo] = counts.get(repo, 0) + 1
        return counts
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {"Local Garden": 1}

def generate_svg(counts):
    """Generates an SVG constellation map based on contribution counts."""
    width, height = 800, 500
    
    # SVG Header
    svg = [
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
        '  <defs>',
        '    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">',
        '      <stop offset="0%" style="stop-color:#0b0e14;stop-opacity:1" />',
        '      <stop offset="100%" style="stop-color:#1a1f2c;stop-opacity:1" />',
        '    </linearGradient>',
        '  </defs>',
        '  <rect width="100%" height="100%" fill="url(#sky)" />'
    ]
    
    # Add random background stars
    random.seed(42)
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        svg.append(f'  <circle cx="{x}" cy="{y}" r="1" fill="white" opacity="0.3" />')

    # Draw the Constellation
    repos = list(counts.keys())
    for repo in repos:
        count = counts[repo]
        
        # Deterministic position based on name
        h = hashlib.md5(repo.encode()).hexdigest()
        x = (int(h[:4], 16) % (width - 200)) + 100
        y = (int(h[4:8], 16) % (height - 150)) + 75
        
        radius = 5 + (count * 4)
        color = "#58a6ff" if "shapash" in repo.lower() else "#ff7b72" if count > 5 else "#d2a8ff"
        
        # Draw star
        svg.append(f'  <circle cx="{x}" cy="{y}" r="{radius}" fill="{color}" opacity="0.8">')
        svg.append(f'    <title>{repo} ({count} contributions)</title>')
        svg.append(f'  </circle>')
        
        # Add glow
        svg.append(f'  <circle cx="{x}" cy="{y}" r="{radius + 5}" fill="{color}" opacity="0.2" />')
        
        # Add Label
        display_name = repo.split('/')[-1]
        svg.append(f'  <text x="{x}" y="{y + radius + 15}" fill="#c9d1d9" font-size="12" font-family="monospace" text-anchor="middle">{display_name}</text>')

    # Title
    svg.append(f'  <text x="20" y="30" fill="#f0f6fc" font-size="20" font-family="monospace">Gemini Scout Constellation</text>')
    svg.append(f'  <text x="20" y="50" fill="#8b949e" font-size="12" font-family="monospace">Updated: {os.popen("date +%Y-%m-%d").read().strip()}</text>')
    
    svg.append('</svg>')
    return "\n".join(svg)

if __name__ == "__main__":
    print("Mapping the archipelago...")
    contributions = get_contributions()
    print(f"Found footprints in {len(contributions)} harbors.")
    
    svg_content = generate_svg(contributions)
    
    output_path = "images/scout_constellation.svg"
    os.makedirs("images", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(svg_content)
    
    print(f"Constellation mapped to {output_path}")
