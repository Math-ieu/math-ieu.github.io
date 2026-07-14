#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path

# Verify dependencies
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Error: 'playwright' is not installed. Please install it using: pip install playwright")
    sys.exit(1)

def parse_markdown(md_content):
    # Parse title and description
    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Guide de Présentation de la Soutenance"
    
    # Parse timing structure block
    timing_block = ""
    timing_match = re.search(r'##\s+Structure du Temps.*?\n(.*?)(?=\n---|##|$)', md_content, re.DOTALL | re.IGNORECASE)
    if timing_match:
        timing_items = re.findall(r'\*\s+\*\*(.*?)\*\*.*?:?\s*(.*)$', timing_match.group(1), re.MULTILINE)
        for label, val in timing_items:
            timing_block += f'<div class="timing-item"><strong>{label}</strong> <span>{val}</span></div>'

    # Split into sections and slides
    lines = md_content.split('\n')
    sections = []
    current_section = None
    current_slide = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Section header
        if line.startswith('### '):
            if current_slide and current_section:
                current_section['slides'].append(current_slide)
                current_slide = None
            if current_section:
                sections.append(current_section)
                
            sec_title = line.replace('### ', '').strip()
            current_section = {
                'title': sec_title,
                'slides': []
            }
            
        # Slide header
        elif line.startswith('#### Slide '):
            if current_slide and current_section:
                current_section['slides'].append(current_slide)
                
            slide_info = line.replace('#### Slide ', '').strip()
            # Extract number, title, and duration
            match = re.match(r'^(\d+[a-zA-Z]?)\s*:\s*(.*?)\s*\((\d+\s*\w+.*?)\)$', slide_info)
            if match:
                num, s_title, duration = match.groups()
            else:
                num = "X"
                s_title = slide_info
                duration = "-"
                
            current_slide = {
                'num': num,
                'title': s_title,
                'duration': duration,
                'speech': '',
                'cues': '',
                'transition': ''
            }
            
        # Content parsing inside slide
        elif current_slide:
            if '**Speech :**' in line or 'Speech :' in line:
                # Extract speech blockquote
                continue
            elif line.startswith('>') and current_slide:
                clean_line = line.lstrip('>').strip().strip('"').strip('*"').strip('"*')
                current_slide['speech'] += (" " if current_slide['speech'] else "") + clean_line
            elif '**Cues visuels :**' in line or 'Cues visuels :' in line:
                cues = line.replace('*   **Cues visuels :**', '').replace('* **Cues visuels :**', '').strip()
                current_slide['cues'] = cues
            elif '**Action :**' in line or 'Action :' in line:
                action = line.replace('*   **Action :**', '').replace('* **Action :**', '').strip()
                current_slide['cues'] = action
            elif '**Transition :**' in line or 'Transition :' in line:
                trans = line.replace('*   **Transition :**', '').replace('* **Transition :**', '').strip().strip('"')
                current_slide['transition'] = trans

    if current_slide and current_section:
        current_section['slides'].append(current_slide)
    if current_section:
        sections.append(current_section)
        
    return title, timing_block, sections

def main():
    workspace_dir = Path("/home/mathdev/Works/PFE-NIDS-AI")
    md_file = workspace_dir / "speech_presentation.md"
    html_file = workspace_dir / "speech_presentation.html"
    pdf_file = workspace_dir / "speech_presentation.pdf"
    
    if not md_file.exists():
        print(f"Error: speech_presentation.md not found at {md_file}")
        sys.exit(1)
        
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
        
    title, timing_block, sections = parse_markdown(md_content)
    
    # Render HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;700&family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');
        
        :root {{
            --primary: #ef4444;
            --secondary: #00f2fe;
            --accent: #a78bfa;
            --dark: #0f172a;
            --light-bg: #f8fafc;
            --border-subtle: #cbd5e1;
            --text-main: #334155;
            --text-dark: #0f172a;
            --font-title: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
            --font-mono: 'Fira Code', monospace;
        }}
        
        body {{
            font-family: var(--font-body);
            color: var(--text-main);
            line-height: 1.6;
            background: #fff;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact;
        }}
        
        /* A4 Print Layout Rules */
        @page {{
            size: A4;
            margin: 18mm 15mm 20mm 15mm;
        }}
        
        @media print {{
            body {{
                background: #fff;
            }}
            .page-break {{
                page-break-before: always;
                break-before: page;
            }}
            .slide-card {{
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }}
        }}
        
        .container {{
            max-width: 820px;
            margin: 0 auto;
            padding: 10px;
        }}
        
        /* Cover Page */
        .cover-page {{
            height: 255mm; /* Dynamic spacing to prevent spillover */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 30px 10px;
            box-sizing: border-box;
            page-break-after: always;
        }}
        
        .cover-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #000;
            padding-bottom: 15px;
        }}
        
        .cover-logo-text {{
            font-family: var(--font-title);
            font-weight: 900;
            font-size: 1.6rem;
            color: var(--text-dark);
            text-transform: uppercase;
            letter-spacing: -0.5px;
        }}
        
        .cover-logo-sub {{
            font-family: var(--font-mono);
            font-size: 0.75rem;
            color: var(--primary);
            font-weight: bold;
        }}
        
        .cover-center {{
            margin: auto 0;
        }}
        
        .cover-badge {{
            display: inline-block;
            background: rgba(239, 68, 68, 0.08);
            border: 2px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-size: 0.85rem;
            font-weight: 800;
            padding: 5px 12px;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 25px;
            box-shadow: 3px 3px 0px #000;
        }}
        
        .cover-title {{
            font-family: var(--font-title);
            font-size: 3.2rem;
            font-weight: 900;
            color: var(--text-dark);
            line-height: 1.1;
            margin: 0 0 15px 0;
            letter-spacing: -1.5px;
            text-transform: uppercase;
        }}
        
        .cover-subtitle {{
            font-family: var(--font-body);
            font-size: 1.35rem;
            color: #64748b;
            margin: 0 0 40px 0;
            font-weight: 400;
            line-height: 1.4;
        }}
        
        .timing-box {{
            background: var(--light-bg);
            border: 3px solid #000;
            box-shadow: 5px 5px 0px #000;
            padding: 20px;
            margin-top: 10px;
        }}
        
        .timing-title {{
            font-family: var(--font-title);
            font-size: 1.1rem;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--text-dark);
            margin: 0 0 12px 0;
            border-bottom: 2.5px solid var(--primary);
            padding-bottom: 6px;
            display: inline-block;
        }}
        
        .timing-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }}
        
        .timing-item {{
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            border-bottom: 1px dashed var(--border-subtle);
            padding-bottom: 4px;
        }}
        
        .timing-item strong {{
            color: var(--text-dark);
        }}
        
        .cover-footer {{
            border-top: 2px solid #000;
            padding-top: 20px;
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            font-family: var(--font-mono);
            color: #64748b;
        }}
        
        /* Section Title Page-Break block */
        .section-header {{
            border-left: 6px solid var(--primary);
            padding-left: 15px;
            margin-top: 45px;
            margin-bottom: 25px;
            page-break-inside: avoid;
        }}
        
        .section-title {{
            font-family: var(--font-title);
            font-size: 1.7rem;
            font-weight: 900;
            color: var(--text-dark);
            margin: 0;
            text-transform: uppercase;
            letter-spacing: -0.5px;
        }}
        
        /* Slide Presentation Card styling */
        .slide-card {{
            border: 3px solid #000;
            box-shadow: 6px 6px 0px #000;
            background: #fff;
            padding: 24px;
            margin-bottom: 30px;
            border-radius: 0px;
        }}
        
        .slide-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 2.5px solid #000;
            padding-bottom: 8px;
            margin-bottom: 18px;
        }}
        
        .slide-num {{
            font-family: var(--font-mono);
            font-weight: 900;
            color: var(--primary);
            font-size: 1.25rem;
            text-transform: uppercase;
        }}
        
        .slide-title-text {{
            font-family: var(--font-title);
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--text-dark);
            flex-grow: 1;
            margin: 0 20px;
            text-transform: uppercase;
            letter-spacing: -0.3px;
        }}
        
        .slide-duration {{
            font-family: var(--font-mono);
            font-size: 0.85rem;
            background: #000;
            color: #fff;
            padding: 3px 10px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        .speech-box {{
            background: var(--light-bg);
            border-left: 5px solid var(--accent);
            padding: 16px 20px;
            margin-bottom: 18px;
            font-size: 1.05rem;
            color: var(--text-dark);
            line-height: 1.55;
            font-style: italic;
            font-weight: 400;
        }}
        
        .meta-list {{
            list-style: none;
            padding: 0;
            margin: 0;
            font-size: 0.95rem;
        }}
        
        .meta-item {{
            margin-bottom: 8px;
            display: flex;
            align-items: flex-start;
        }}
        
        .meta-label {{
            font-family: var(--font-title);
            font-weight: 900;
            width: 150px;
            flex-shrink: 0;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 1px;
            color: #64748b;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        
        .meta-content {{
            color: var(--text-dark);
            font-weight: 500;
        }}
        
    </style>
</head>
<body>
    <div class="container">
        
        <!-- COVER PAGE -->
        <div class="cover-page">
            <div class="cover-header">
                <div>
                    <div class="cover-logo-text">HESTIM</div>
                    <div class="cover-logo-sub">ENGINEERING & BUSINESS SCHOOL</div>
                </div>
                <div style="text-align: right;">
                    <div class="cover-logo-text" style="color: var(--primary);">3D SMART FACTORY</div>
                    <div class="cover-logo-sub" style="color: var(--text-dark);">R&D CYBERSECURITY LAB</div>
                </div>
            </div>
            
            <div class="cover-center">
                <div class="cover-badge">SCRIPT ORAL OFFICIEL</div>
                <h1 class="cover-title">Guide de Présentation<br>Soutenance PFE</h1>
                <p class="cover-subtitle">Script fidèle de soutenance de stage de fin d'études pour l'obtention du diplôme d'Ingénieur d'État en Ingénierie Informatique et Intelligence Artificielle.</p>
                
                <div class="timing-box">
                    <h3 class="timing-title">Timing Global &amp; Gestion des 15 Minutes</h3>
                    <div class="timing-grid">
                        {timing_block}
                    </div>
                </div>
            </div>
            
            <div class="cover-footer">
                <div>Présenté par : Option IA &amp; Big Data</div>
                <div>Session : Juillet 2026</div>
            </div>
        </div>
        
        <!-- SECTIONS AND SLIDES -->
"""
    
    for section_idx, section in enumerate(sections):
        html_template += f"""
        <!-- SECTION {section_idx + 1} -->
        <div class="section-header {"page-break" if section_idx > 0 else ""}">
            <h2 class="section-title">{section['title']}</h2>
        </div>
        """
        
        for slide in section['slides']:
            html_template += f"""
            <!-- SLIDE {slide['num']} -->
            <div class="slide-card">
                <div class="slide-header">
                    <span class="slide-num">Slide {slide['num']}</span>
                    <h3 class="slide-title-text">{slide['title']}</h3>
                    <span class="slide-duration">{slide['duration']}</span>
                </div>
                <div class="speech-box">
                    "{slide['speech']}"
                </div>
                <ul class="meta-list">
            """
            
            if slide['cues']:
                html_template += f"""
                    <li class="meta-item">
                        <span class="meta-label">🎬 Cues Visuels</span>
                        <span class="meta-content">{slide['cues']}</span>
                    </li>
                """
                
            if slide['transition']:
                html_template += f"""
                    <li class="meta-item">
                        <span class="meta-label">➡️ Transition</span>
                        <span class="meta-content">{slide['transition']}</span>
                    </li>
                """
                
            html_template += """
                </ul>
            </div>
            """
            
    html_template += """
    </div>
</body>
</html>
"""
    
    # Save the HTML file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"HTML presentation guide generated at: {html_file}")
    
    # Convert HTML to PDF using Playwright
    print("Starting Playwright to compile HTML to PDF...")
    with sync_playwright() as p:
        chrome_path = "/usr/bin/google-chrome"
        if not os.path.exists(chrome_path):
            browser = p.chromium.launch(headless=True)
        else:
            browser = p.chromium.launch(executable_path=chrome_path, headless=True)
            
        page = browser.new_page()
        page.goto(html_file.as_uri())
        
        # Wait for google fonts to load
        page.wait_for_timeout(1000)
        
        # Output to PDF using native A4 printing features
        page.pdf(
            path=str(pdf_file),
            format="A4",
            print_background=True,
            margin={
                "top": "18mm",
                "bottom": "20mm",
                "left": "15mm",
                "right": "15mm"
            }
        )
        browser.close()
        
    print(f"PDF successfully compiled at: {pdf_file}")

if __name__ == "__main__":
    main()
