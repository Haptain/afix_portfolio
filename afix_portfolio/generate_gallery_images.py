from pathlib import Path

root = Path(r"c:\Users\PC\Desktop\afix_portfolio\images")
root.mkdir(parents=True, exist_ok=True)

items = [
    ("unit1_hotspot_kianjiru.svg", "Wireless Hotspot Installation", "Rural deployment", "network"),
    ("unit1_equipment_mounting.svg", "Equipment Mounting", "Pole and cabinet setup", "install"),
    ("unit1_fiber_splice.svg", "Fiber Optic Splicing", "High-speed backbone", "fiber"),
    ("unit1_coverage_mururi.svg", "Coverage Planning", "Area mapping", "map"),
    ("unit3_firewall.svg", "Network Security", "Firewall protection", "security"),
    ("unit3_access_control.svg", "Access Control", "User permissions", "access"),
    ("unit8_analytics.svg", "Data Analytics", "Dashboard reporting", "analytics"),
    ("unit8_financial.svg", "Financial Reporting", "Budget tracking", "finance"),
    ("unit8_performance.svg", "Performance Metrics", "System monitoring", "monitor"),
    ("unit8_kpi.svg", "KPI Tracking", "Service targets", "kpi"),
    ("unit9_network_diagram.svg", "Network Diagram", "Topology design", "diagram"),
    ("unit9_app_ui.svg", "UI Mockup", "Mobile app design", "ui"),
    ("unit9_marketing.svg", "Marketing Graphic", "Brand visuals", "marketing"),
    ("unit9_user_guide.svg", "User Guide", "Documentation layout", "guide"),
    ("unit11_login.svg", "Mobile Login", "User authentication", "login"),
    ("unit11_dashboard.svg", "Dashboard UI", "Status overview", "dashboard"),
    ("unit11_payment.svg", "Payment Flow", "Digital payments", "payment"),
    ("unit11_support.svg", "Support Chat", "Customer service", "support"),
    ("extra_photo_1.svg", "Field Deployment", "On-site work", "field"),
    ("extra_photo_2.svg", "Team Collaboration", "Technical teamwork", "team"),
    ("extra_photo_3.svg", "System Testing", "Performance checks", "testing"),
    ("extra_photo_4.svg", "Documentation", "Evidence records", "docs"),
]

for filename, title, subtitle, theme in items:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">
  <rect width="1200" height="900" fill="#07111f"/>
  <rect x="30" y="30" width="1140" height="840" rx="24" fill="#0f172a" stroke="#6366f1" stroke-width="8"/>
  <rect x="70" y="70" width="1060" height="760" rx="20" fill="#111827"/>
  <circle cx="250" cy="240" r="110" fill="#1d4ed8"/>
  <rect x="260" y="300" width="320" height="220" rx="16" fill="#3b82f6"/>
  <rect x="700" y="220" width="320" height="280" rx="18" fill="#2563eb"/>
  <path d="M780 620c80-90 140-130 220-160" stroke="#93c5fd" stroke-width="8" fill="none" stroke-linecap="round"/>
  <text x="110" y="160" fill="#f8fafc" font-family="Arial, sans-serif" font-size="44" font-weight="700">{title}</text>
  <text x="110" y="220" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="28">{subtitle}</text>
  <text x="110" y="760" fill="#818cf8" font-family="Arial, sans-serif" font-size="20">TVET ICT Portfolio Evidence</text>
  <text x="110" y="795" fill="#94a3b8" font-family="Arial, sans-serif" font-size="18">Theme: {theme}</text>
</svg>'''
    (root / filename).write_text(svg, encoding="utf-8")

print(f"Created {len(items)} SVG images in {root}")
