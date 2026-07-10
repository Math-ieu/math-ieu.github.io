#!/usr/bin/env python3
"""
Script to convert the custom HTML presentation (Soutenance_PFE_NIDS_AI.html) to PDF.
It launches a headless browser, navigates through the slides, hides UI buttons,
captures screenshots, and compiles them into a single high-quality PDF.
"""

import os
import sys
import time
import argparse
from pathlib import Path

# Try importing playwright. If not installed, raise an error.
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Error: 'playwright' is not installed in your Python environment.")
    print("Please install it using: pip install playwright")
    sys.exit(1)

try:
    from PIL import Image
    # Initialize all image plugins so formats like JPEG are registered for PDF saving
    Image.init()
except ImportError:
    print("Error: 'Pillow' is not installed in your Python environment.")
    print("Please install it using: pip install Pillow")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert custom HTML presentation to PDF.")
    parser.add_argument(
        "--input", "-i",
        default="Soutenance_PFE_NIDS_AI.html",
        help="Path to the input HTML file (default: Soutenance_PFE_NIDS_AI.html)"
    )
    parser.add_argument(
        "--output", "-o",
        default="Soutenance_PFE_NIDS_AI.pdf",
        help="Path to the output PDF file (default: Soutenance_PFE_NIDS_AI.pdf)"
    )
    parser.add_argument(
        "--theme", "-t",
        choices=["dark", "light"],
        default="dark",
        help="Theme of the slides: dark or light (default: dark)"
    )
    parser.add_argument(
        "--delay", "-d",
        type=float,
        default=2.5,
        help="Delay in seconds to wait for transitions and count-up animations to settle (default: 2.5)"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1920,
        help="Viewport width in pixels (default: 1920)"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=1080,
        help="Viewport height in pixels (default: 1080)"
    )
    
    args = parser.parse_args()
    
    # Resolve paths relative to working directory
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    
    if not input_path.exists():
        print(f"Error: Input HTML file not found at {input_path}")
        sys.exit(1)
        
    print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")
    print(f"Theme: {args.theme}")
    print(f"Resolution: {args.width}x{args.height}")
    print(f"Transition Delay: {args.delay} seconds")
    print("Starting Playwright and Google Chrome...")
    
    temp_images = []
    
    # We use sync_playwright to run the headless browser session
    with sync_playwright() as p:
        # Launch using system-installed Google Chrome to avoid downloading 100MB+ Chromium binary
        chrome_path = "/usr/bin/google-chrome"
        if not os.path.exists(chrome_path):
            # Fallback to default chromium launch if system path is different
            print("Google Chrome not found at /usr/bin/google-chrome. Trying standard chromium...")
            browser = p.chromium.launch(headless=True)
        else:
            browser = p.chromium.launch(executable_path=chrome_path, headless=True)
            
        # Create page with specified viewport
        page = browser.new_page(viewport={"width": args.width, "height": args.height})
        
        # Load the HTML file
        url = input_path.as_uri()
        print(f"Loading presentation: {url}")
        page.goto(url)
        
        # Inject CSS to hide theme toggle button, bottom nav buttons, timer, and index modal
        page.add_style_tag(content="""
            .theme-toggle-btn, 
            .btn-control, 
            .timer-widget,
            #directory-modal { 
                display: none !important; 
            }
        """)
        
        # Set the desired theme
        if args.theme == "light":
            print("Setting light theme...")
            page.evaluate("document.body.classList.add('light-theme'); updateThemeButton();")
        else:
            print("Setting dark theme...")
            page.evaluate("document.body.classList.remove('light-theme'); updateThemeButton();")
            
        # Let the first slide transition finish
        time.sleep(args.delay)
        
        # Get total slides from JavaScript
        total_slides = page.evaluate("totalSlides")
        print(f"Detected {total_slides} slides in presentation.")
        
        # Temporary directory for screenshots (created inside workspace)
        temp_dir = Path("temp_slides")
        temp_dir.mkdir(exist_ok=True)
        
        try:
            for idx in range(total_slides):
                slide_num = idx + 1
                print(f"Processing slide {slide_num}/{total_slides}...")
                
                # Navigate to slide index
                page.evaluate(f"currentSlideIdx = {idx}; updateSlide();")
                
                # Wait for transitions and count-up animations to settle
                time.sleep(args.delay)
                
                # Take screenshot
                temp_img_path = temp_dir / f"slide_{slide_num:03d}.png"
                page.screenshot(path=str(temp_img_path))
                
                # Open with Pillow and append to list
                img = Image.open(temp_img_path).convert("RGB")
                temp_images.append(img)
                
            # Compile screenshots into a single PDF
            if temp_images:
                print(f"Compiling {len(temp_images)} slides into PDF...")
                temp_images[0].save(
                    output_path,
                    save_all=True,
                    append_images=temp_images[1:]
                )
                print(f"PDF successfully generated at: {output_path}")
            else:
                print("Error: No slides captured.")
                
        finally:
            # Clean up temporary screenshots
            print("Cleaning up temporary screenshot files...")
            for img in temp_images:
                img.close()
            for f in temp_dir.glob("slide_*.png"):
                try:
                    f.unlink()
                except Exception:
                    pass
            try:
                temp_dir.rmdir()
            except Exception:
                pass
                
        browser.close()

if __name__ == "__main__":
    main()
