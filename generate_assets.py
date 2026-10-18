import os
from PIL import Image, ImageDraw

ASSET_DIR = "/home/developer/.gemini/antigravity-ide/scratch/apps-femininos/app-seguranca-feminina/store_assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def create_icon():
    img = Image.new("RGBA", (512, 512), color=(250, 245, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer circle
    draw.ellipse([32, 32, 480, 480], fill=(168, 85, 247, 255))
    draw.ellipse([64, 64, 448, 448], fill=(126, 34, 206, 255))
    
    # Shield shape / protection emblem in the center
    # Top points: (160, 160) to (352, 160), bottom point (256, 380)
    shield_pts = [
        (160, 170), (352, 170),
        (352, 270), (256, 370), (160, 270)
    ]
    draw.polygon(shield_pts, fill=(255, 255, 255, 255))
    
    # Inner star / heart emblem
    draw.ellipse([216, 200, 296, 280], fill=(147, 51, 234, 255))
    draw.ellipse([236, 220, 276, 260], fill=(255, 255, 255, 255))
    
    path = os.path.join(ASSET_DIR, "icon-512.png")
    img.save(path, "PNG")
    print("Icon generated:", path)

def create_feature():
    img = Image.new("RGB", (1024, 500), color=(250, 245, 255))
    draw = ImageDraw.Draw(img)
    
    # Decorative purple shapes
    draw.rectangle([0, 0, 1024, 500], fill=(245, 243, 255))
    draw.ellipse([-100, -100, 400, 400], fill=(233, 213, 255))
    draw.ellipse([700, 180, 1200, 680], fill=(216, 180, 254))
    
    # Center Card container
    draw.rounded_rectangle([150, 70, 874, 430], radius=24, fill=(255, 255, 255))
    draw.rounded_rectangle([180, 100, 320, 240], radius=16, fill=(147, 51, 234))
    
    # Shield emblem on the left card
    draw.polygon([(210, 130), (290, 130), (290, 180), (250, 220), (210, 180)], fill=(255, 255, 255))
    
    # Lines representing text
    draw.rectangle([360, 120, 780, 160], fill=(126, 34, 206))
    draw.rectangle([360, 180, 680, 210], fill=(156, 163, 175))
    draw.rectangle([180, 280, 840, 310], fill=(243, 244, 246))
    draw.rectangle([180, 330, 800, 360], fill=(243, 244, 246))
    draw.rectangle([180, 380, 720, 400], fill=(243, 244, 246))
    
    path = os.path.join(ASSET_DIR, "feature-graphic-1024x500.png")
    img.save(path, "PNG")
    print("Feature graphic generated:", path)

def create_screenshots():
    screens = [
        ("SOS & Alerta Rápido", (147, 51, 234)),
        ("Contatos de Confiança", (126, 34, 206)),
        ("Localização em Tempo Real", (168, 85, 247)),
        ("Privacidade Total no Aparelho", (107, 33, 168))
    ]
    for idx, (title, color) in enumerate(screens, 1):
        img = Image.new("RGB", (1080, 1920), color=(250, 245, 255))
        draw = ImageDraw.Draw(img)
        
        # Header banner
        draw.rectangle([0, 0, 1080, 360], fill=color)
        draw.rectangle([120, 140, 600, 180], fill=(255, 255, 255))
        draw.rectangle([120, 210, 840, 240], fill=(233, 213, 255))
        
        # Phone mockup card
        draw.rounded_rectangle([100, 440, 980, 1780], radius=40, fill=(255, 255, 255))
        
        # Inner widgets
        draw.rounded_rectangle([160, 520, 920, 780], radius=24, fill=(245, 243, 255))
        draw.ellipse([460, 560, 620, 720], fill=color)
        
        draw.rounded_rectangle([160, 840, 920, 1100], radius=24, fill=(249, 250, 251))
        draw.rectangle([200, 900, 600, 930], fill=(126, 34, 206))
        draw.rectangle([200, 960, 800, 985], fill=(209, 213, 219))
        draw.rectangle([200, 1010, 700, 1035], fill=(229, 231, 235))
        
        draw.rounded_rectangle([160, 1160, 920, 1420], radius=24, fill=(249, 250, 251))
        draw.rectangle([200, 1220, 500, 1250], fill=(147, 51, 234))
        draw.rectangle([200, 1280, 840, 1305], fill=(209, 213, 219))
        
        # Bottom action button
        draw.rounded_rectangle([160, 1500, 920, 1660], radius=32, fill=color)
        draw.rectangle([340, 1560, 740, 1600], fill=(255, 255, 255))
        
        path = os.path.join(ASSET_DIR, f"phone-{idx}.png")
        img.save(path, "PNG")
        print(f"Screenshot {idx} generated:", path)

if __name__ == "__main__":
    create_icon()
    create_feature()
    create_screenshots()
