"""
Run: python manage.py shell < store/seed.py
Seeds initial categories and products for Tony Motors
"""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tony_motors.settings")
django.setup()

from store.models import Category, Product

Category.objects.all().delete()
Product.objects.all().delete()

cats = [
    {"name": "Engine Parts", "icon": "bi-gear-fill", "description": "High-performance engine components"},
    {"name": "Exhaust Systems", "icon": "bi-wind", "description": "Aftermarket exhaust for more power and sound"},
    {"name": "Suspension", "icon": "bi-arrows-collapse-vertical", "description": "Coilovers, springs, and handling upgrades"},
    {"name": "Brakes", "icon": "bi-stop-circle-fill", "description": "Big brake kits, rotors, and pads"},
    {"name": "Aerodynamics", "icon": "bi-fan", "description": "Spoilers, diffusers, and body kits"},
    {"name": "Wheels & Tires", "icon": "bi-circle", "description": "Lightweight alloys and performance rubber"},
    {"name": "Interior", "icon": "bi-speedometer2", "description": "Racing seats, steering wheels, harnesses"},
    {"name": "Electronics", "icon": "bi-lightning-charge-fill", "description": "ECU tuning, gauges, and performance electronics"},
]
category_objs = {}
for c in cats:
    obj = Category.objects.create(**c)
    category_objs[c["name"]] = obj
    print(f"Created category: {c['name']}")

products = [
    {
        "category": "Engine Parts",
        "name": "High-Flow Cold Air Intake Kit",
        "price": "289.99",
        "discount_price": "229.99",
        "description": "Dramatically improves airflow to your engine with a precision-engineered cold air intake. Features a high-flow performance filter and mandrel-bent aluminum tubing for maximum gains.",
        "brand": "Arma Speed",
        "compatibility": "Universal / Most sports cars",
        "is_featured": True,
        "is_new": False,
        "stock": 15,
    },
    {
        "category": "Engine Parts",
        "name": "Performance Camshaft Set",
        "price": "1249.00",
        "description": "Race-spec camshafts engineered for high-RPM power. Precision ground to exact tolerances for maximum lift and duration.",
        "brand": "Kelford Cams",
        "compatibility": "Ferrari 488, Ferrari F8",
        "is_featured": False,
        "is_new": True,
        "stock": 6,
    },
    {
        "category": "Engine Parts",
        "name": "Short-Ram Performance Intake",
        "price": "149.99",
        "description": "Increase throttle response and power with this polished short-ram intake system. CNC-machined adapters ensure a perfect fit.",
        "brand": "Injen",
        "compatibility": "Porsche 911, Porsche Boxster",
        "is_featured": True,
        "is_new": False,
        "stock": 22,
    },
    {
        "category": "Exhaust Systems",
        "name": "Titanium Cat-Back Exhaust System",
        "price": "3499.00",
        "discount_price": "2999.00",
        "description": "Full titanium construction saves 18 lbs over stock. Features hand-welded mandrel bends and a polished 115mm quad tip setup. Deep, aggressive exhaust note.",
        "brand": "Akrapovic",
        "compatibility": "Lamborghini Huracan EVO",
        "is_featured": True,
        "is_new": False,
        "stock": 4,
    },
    {
        "category": "Exhaust Systems",
        "name": "Stainless Steel Cat-Back Exhaust",
        "price": "899.00",
        "description": "Premium 304 stainless steel construction. Bolt-on installation, significant weight reduction, and a rich exhaust tone that turns heads.",
        "brand": "Milltek Sport",
        "compatibility": "Audi R8, Audi RS5",
        "is_featured": False,
        "is_new": True,
        "stock": 9,
    },
    {
        "category": "Exhaust Systems",
        "name": "Valvetronic Exhaust System",
        "price": "2299.00",
        "description": "Electronically controlled butterfly valves let you switch between stealth and beast mode at the push of a button. Smartphone app compatible.",
        "brand": "Armytrix",
        "compatibility": "McLaren 720S",
        "is_featured": True,
        "is_new": True,
        "stock": 3,
    },
    {
        "category": "Suspension",
        "name": "Coilover Suspension Kit",
        "price": "1899.00",
        "discount_price": "1599.00",
        "description": "Fully adjustable 32-way damping coilovers with inverted monotube design. Independently adjust ride height and rebound for track or street use.",
        "brand": "KW Suspensions",
        "compatibility": "Porsche 911 (997/991), Cayman",
        "is_featured": True,
        "is_new": False,
        "stock": 8,
    },
    {
        "category": "Suspension",
        "name": "Adjustable Anti-Roll Bar Kit",
        "price": "649.00",
        "description": "Stiffen your chassis response with this 4-position adjustable anti-roll bar set. Eliminates understeer and keeps your front end planted.",
        "brand": "Whiteline",
        "compatibility": "Subaru BRZ, Toyota GR86",
        "is_featured": False,
        "is_new": False,
        "stock": 18,
    },
    {
        "category": "Brakes",
        "name": "6-Piston Big Brake Kit",
        "price": "2799.00",
        "description": "Massive stopping power from monoblock 6-piston calipers paired with 380mm cross-drilled and slotted rotors. Available in red or black caliper finish.",
        "brand": "Brembo",
        "compatibility": "Ferrari 458, Ferrari 488",
        "is_featured": True,
        "is_new": False,
        "stock": 5,
    },
    {
        "category": "Brakes",
        "name": "Performance Brake Pads — Track",
        "price": "189.00",
        "description": "High-temperature racing compound brake pads for aggressive track driving. Excellent cold bite and fade resistance up to 900°C.",
        "brand": "Pagid Racing",
        "compatibility": "Universal (multiple fitments available)",
        "is_featured": False,
        "is_new": True,
        "stock": 30,
    },
    {
        "category": "Aerodynamics",
        "name": "Carbon Fiber Rear Wing",
        "price": "1899.00",
        "description": "3K woven carbon fiber swan-neck rear wing. Generates 180 lbs of downforce at 150 mph. Includes adjustable angle of attack from 0° to 20°.",
        "brand": "APR Performance",
        "compatibility": "Universal / Custom mount included",
        "is_featured": True,
        "is_new": True,
        "stock": 7,
    },
    {
        "category": "Aerodynamics",
        "name": "Front Splitter Kit",
        "price": "499.00",
        "description": "Aggressive carbon fiber front splitter with integrated end plates. Dramatically increases front downforce and improves turn-in behavior.",
        "brand": "VR Aero",
        "compatibility": "Porsche 911 GT3 (992)",
        "is_featured": False,
        "is_new": False,
        "stock": 11,
    },
    {
        "category": "Wheels & Tires",
        "name": "Forged Monoblock Wheel Set (4)",
        "price": "4299.00",
        "description": "One-piece forged 6061-T6 aluminum wheels. Weighing just 17 lbs each, these are significantly lighter than cast alternatives. 5-spoke design.",
        "brand": "Vossen Forged",
        "compatibility": "5x120 PCD — BMW M2, M3, M4",
        "is_featured": True,
        "is_new": False,
        "stock": 4,
    },
    {
        "category": "Interior",
        "name": "Racing Bucket Seat",
        "price": "799.00",
        "discount_price": "649.00",
        "description": "FIA-approved composite shell racing seat with harness slots and side bolsters. Weighs only 9 lbs. Black microfiber and Alcantara finish.",
        "brand": "Sparco",
        "compatibility": "Universal with adapter rails",
        "is_featured": True,
        "is_new": False,
        "stock": 12,
    },
    {
        "category": "Interior",
        "name": "Carbon Fiber Steering Wheel",
        "price": "549.00",
        "description": "350mm flat-bottom steering wheel with carbon fiber spokes and Alcantara grip. D-cut design for better legroom in low seating positions.",
        "brand": "OMP",
        "compatibility": "Universal with hub adapter",
        "is_featured": False,
        "is_new": True,
        "stock": 20,
    },
    {
        "category": "Electronics",
        "name": "ECU Tune & Flash Kit",
        "price": "699.00",
        "description": "Professional ECU reflash with custom dyno-tuned maps for your vehicle. Adds 25-60 whp depending on model. Includes remote tuning support.",
        "brand": "Ecutek",
        "compatibility": "Multiple (contact us for compatibility check)",
        "is_featured": True,
        "is_new": True,
        "stock": 25,
    },
    {
        "category": "Electronics",
        "name": "Wide-Band O2 & Boost Gauge Kit",
        "price": "349.00",
        "description": "Dual 52mm gauge set including a wideband air/fuel ratio gauge and boost pressure gauge. Precision sensors with color LED display.",
        "brand": "AEM",
        "compatibility": "Universal",
        "is_featured": False,
        "is_new": False,
        "stock": 17,
    },
]

for p in products:
    cat_name = p.pop("category")
    Product.objects.create(category=category_objs[cat_name], **p)
    print(f"Created product: {p['name']}")

print("\nDone! Created", Category.objects.count(), "categories and", Product.objects.count(), "products.")
