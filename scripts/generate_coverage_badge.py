#!/usr/bin/env python3
"""
Coverage Badge Generator for Python CI/CD Demo

This script generates SVG coverage badges from coverage.xml files, replacing external
services like CodeCov for self-hosted deployments.

Features:
- Reads coverage data from coverage.xml files
- Generates customizable SVG badges
- Color-coded based on coverage percentage
- Supports multiple badge styles and formats
- Can generate branch coverage badges as well

Usage:
    python scripts/generate_coverage_badge.py [options]

Options:
    --coverage-file FILE    Path to coverage.xml file (default: coverage.xml)
    --output FILE          Output SVG file path (default: coverage-badge.svg)
    --style STYLE          Badge style: flat, plastic, or for-the-badge (default: flat)
    --title TEXT           Badge title text (default: coverage)
    --min-good N          Minimum percentage for green (default: 80)
    --min-ok N            Minimum percentage for yellow (default: 60)
"""

import argparse
import xml.etree.ElementTree as ET  # nosec B405 - parsing trusted coverage.xml files only
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import quote


class CoverageBadgeGenerator:
    """Generates SVG coverage badges from coverage.xml files."""

    def __init__(self):
        self.badge_templates = {
            "flat": self._flat_badge_template,
            "plastic": self._plastic_badge_template,
            "for-the-badge": self._for_the_badge_template,
        }

    def generate_badge(
        self,
        coverage_file: Path,
        output_file: Path,
        style: str = "flat",
        title: str = "coverage",
        min_good: int = 80,
        min_ok: int = 60,
    ) -> None:
        """Generate a coverage badge from coverage.xml."""
        # Parse coverage data
        coverage_percent = self._parse_coverage_xml(coverage_file)

        # Determine color based on coverage
        color = self._get_coverage_color(coverage_percent, min_good, min_ok)

        # Format percentage text
        coverage_text = f"{coverage_percent:.0f}%"

        # Generate SVG badge
        svg_content = self._generate_svg_badge(title, coverage_text, color, style)

        # Write to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(svg_content)

        print(f"Generated coverage badge: {output_file}")
        print(f"Coverage: {coverage_text} ({color})")

    def _parse_coverage_xml(self, coverage_file: Path) -> float:
        """Parse coverage percentage from coverage.xml file."""
        try:
            tree = ET.parse(
                coverage_file
            )  # nosec B314 - parsing trusted coverage.xml from pytest
            root = tree.getroot()

            # Get line-rate from the coverage element
            line_rate = root.get("line-rate")
            if line_rate:
                return float(line_rate) * 100

            # Fallback: calculate from package data
            total_lines = 0
            covered_lines = 0

            for package in root.findall(".//package"):
                package_line_rate = package.get("line-rate")
                if package_line_rate:
                    # This is a simplified approach; for more accuracy,
                    # we'd need to parse individual class/method data
                    return float(package_line_rate) * 100

            raise ValueError("Could not find coverage data in XML")

        except (ET.ParseError, ValueError, FileNotFoundError) as e:
            raise RuntimeError(f"Error parsing coverage file {coverage_file}: {e}")

    def _get_coverage_color(self, coverage: float, min_good: int, min_ok: int) -> str:
        """Determine badge color based on coverage percentage."""
        if coverage >= min_good:
            return "brightgreen"
        elif coverage >= min_ok:
            return "yellow"
        else:
            return "red"

    def _generate_svg_badge(self, title: str, text: str, color: str, style: str) -> str:
        """Generate SVG badge content."""
        template_func = self.badge_templates.get(style, self.badge_templates["flat"])
        return template_func(title, text, color)

    def _calculate_text_width(self, text: str, font_size: int = 11) -> int:
        """Estimate text width for SVG positioning."""
        # Rough approximation for text width in pixels
        # This is a simplified calculation; real implementation would use
        # font metrics, but this works for most cases
        char_width = font_size * 0.6
        return int(len(text) * char_width)

    def _flat_badge_template(self, title: str, text: str, color: str) -> str:
        """Generate flat style badge SVG."""
        # Color mappings for shield.io compatible colors
        color_map = {
            "brightgreen": "#4c1",
            "green": "#97ca00",
            "yellow": "#dfb317",
            "orange": "#fe7d37",
            "red": "#e05d44",
            "lightgrey": "#9f9f9f",
            "blue": "#007ec6",
        }

        badge_color = color_map.get(color, color)

        # Calculate dimensions
        title_width = self._calculate_text_width(title)
        text_width = self._calculate_text_width(text)
        total_width = title_width + text_width + 20  # padding

        title_x = title_width // 2 + 6
        text_x = title_width + (text_width // 2) + 10

        return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{total_width}" height="20" role="img" aria-label="{title}: {text}">
    <title>{title}: {text}</title>
    <linearGradient id="s" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <clipPath id="r">
        <rect width="{total_width}" height="20" rx="3" fill="#fff"/>
    </clipPath>
    <g clip-path="url(#r)">
        <rect width="{title_width + 10}" height="20" fill="#555"/>
        <rect x="{title_width + 10}" width="{text_width + 10}" height="20" fill="{badge_color}"/>
        <rect width="{total_width}" height="20" fill="url(#s)"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
        <text aria-hidden="true" x="{title_x * 10}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)">{title}</text>
        <text x="{title_x * 10}" y="140" transform="scale(.1)" fill="#fff">{title}</text>
        <text aria-hidden="true" x="{text_x * 10}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)">{text}</text>
        <text x="{text_x * 10}" y="140" transform="scale(.1)" fill="#fff">{text}</text>
    </g>
</svg>"""

    def _plastic_badge_template(self, title: str, text: str, color: str) -> str:
        """Generate plastic style badge SVG."""
        # Similar to flat but with rounded corners and gradients
        color_map = {
            "brightgreen": "#4c1",
            "green": "#97ca00",
            "yellow": "#dfb317",
            "orange": "#fe7d37",
            "red": "#e05d44",
            "lightgrey": "#9f9f9f",
            "blue": "#007ec6",
        }

        badge_color = color_map.get(color, color)

        title_width = self._calculate_text_width(title)
        text_width = self._calculate_text_width(text)
        total_width = title_width + text_width + 20

        title_x = title_width // 2 + 6
        text_x = title_width + (text_width // 2) + 10

        return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{total_width}" height="18" role="img" aria-label="{title}: {text}">
    <title>{title}: {text}</title>
    <linearGradient id="s" x2="0" y2="100%">
        <stop offset="0" stop-color="#fff" stop-opacity=".7"/>
        <stop offset=".1" stop-color="#aaa" stop-opacity=".1"/>
        <stop offset=".9" stop-color="#000" stop-opacity=".3"/>
        <stop offset="1" stop-color="#000" stop-opacity=".5"/>
    </linearGradient>
    <clipPath id="r">
        <rect width="{total_width}" height="18" rx="4" fill="#fff"/>
    </clipPath>
    <g clip-path="url(#r)">
        <rect width="{title_width + 10}" height="18" fill="#555"/>
        <rect x="{title_width + 10}" width="{text_width + 10}" height="18" fill="{badge_color}"/>
        <rect width="{total_width}" height="18" fill="url(#s)"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
        <text aria-hidden="true" x="{title_x * 10}" y="140" fill="#010101" fill-opacity=".3" transform="scale(.1)">{title}</text>
        <text x="{title_x * 10}" y="130" transform="scale(.1)" fill="#fff">{title}</text>
        <text aria-hidden="true" x="{text_x * 10}" y="140" fill="#010101" fill-opacity=".3" transform="scale(.1)">{text}</text>
        <text x="{text_x * 10}" y="130" transform="scale(.1)" fill="#fff">{text}</text>
    </g>
</svg>"""

    def _for_the_badge_template(self, title: str, text: str, color: str) -> str:
        """Generate for-the-badge style badge SVG."""
        color_map = {
            "brightgreen": "#4c1",
            "green": "#97ca00",
            "yellow": "#dfb317",
            "orange": "#fe7d37",
            "red": "#e05d44",
            "lightgrey": "#9f9f9f",
            "blue": "#007ec6",
        }

        badge_color = color_map.get(color, color)

        # For-the-badge uses uppercase text and larger size
        title_upper = title.upper()
        text_upper = text.upper()

        title_width = self._calculate_text_width(title_upper, 12)
        text_width = self._calculate_text_width(text_upper, 12)
        total_width = title_width + text_width + 24

        title_x = title_width // 2 + 8
        text_x = title_width + (text_width // 2) + 16

        return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{total_width}" height="28" role="img" aria-label="{title_upper}: {text_upper}">
    <title>{title_upper}: {text_upper}</title>
    <g shape-rendering="crispEdges">
        <rect width="{title_width + 16}" height="28" fill="#555"/>
        <rect x="{title_width + 16}" width="{text_width + 8}" height="28" fill="{badge_color}"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-weight="bold" font-size="100">
        <text x="{title_x * 10}" y="175" transform="scale(.1)" fill="#fff">{title_upper}</text>
        <text x="{text_x * 10}" y="175" transform="scale(.1)" fill="#fff">{text_upper}</text>
    </g>
</svg>"""


def main():
    """Main entry point for coverage badge generation."""
    parser = argparse.ArgumentParser(
        description="Generate SVG coverage badges from coverage.xml files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--coverage-file",
        type=Path,
        default=Path("coverage.xml"),
        help="Path to coverage.xml file (default: coverage.xml)",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("coverage-badge.svg"),
        help="Output SVG file path (default: coverage-badge.svg)",
    )

    parser.add_argument(
        "--style",
        choices=["flat", "plastic", "for-the-badge"],
        default="flat",
        help="Badge style (default: flat)",
    )

    parser.add_argument(
        "--title",
        default="coverage",
        help="Badge title text (default: coverage)",
    )

    parser.add_argument(
        "--min-good",
        type=int,
        default=80,
        help="Minimum percentage for green color (default: 80)",
    )

    parser.add_argument(
        "--min-ok",
        type=int,
        default=60,
        help="Minimum percentage for yellow color (default: 60)",
    )

    args = parser.parse_args()

    try:
        generator = CoverageBadgeGenerator()
        generator.generate_badge(
            coverage_file=args.coverage_file,
            output_file=args.output,
            style=args.style,
            title=args.title,
            min_good=args.min_good,
            min_ok=args.min_ok,
        )

        print(f"\n✅ Coverage badge generated successfully!")
        print(f"📁 Output: {args.output}")

    except Exception as e:
        print(f"❌ Error generating coverage badge: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
