"""
SonicFlow AI Logo GIF Generator
Creates an animated logo similar to trace-research-paper-studio style
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

def create_sonicflow_logo():
    # Settings
    width, height = 800, 400
    frames = 60
    fps = 30
    
    # Colors (Purple gradient theme)
    bg_color = (255, 255, 255)
    gradient_start = (102, 126, 234)  # #667eea
    gradient_mid = (118, 75, 162)      # #764ba2
    gradient_end = (240, 147, 251)     # #f093fb
    
    images = []
    
    for frame in range(frames):
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Animation progress
        progress = frame / frames
        angle = progress * 2 * math.pi
        
        # Draw background gradient circles (pulsing)
        center_x, center_y = width // 2, height // 2 - 20
        
        for i in range(3):
            pulse = math.sin(angle + i * math.pi / 3) * 5
            radius = 150 - i * 30 + pulse
            alpha_val = int(40 - i * 10)
            
            # Create circle with gradient
            circle_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            circle_draw = ImageDraw.Draw(circle_img)
            
            color = gradient_start if i == 0 else (gradient_mid if i == 1 else gradient_end)
            circle_draw.ellipse(
                [center_x - radius, center_y - radius, 
                 center_x + radius, center_y + radius],
                fill=(*color, alpha_val)
            )
            img = Image.alpha_composite(img.convert('RGBA'), circle_img)
            img = img.convert('RGB')
        
        # Draw microphone body
        mic_width, mic_height = 40, 60
        mic_x = center_x - mic_width // 2
        mic_y = center_y - mic_height // 2 - 20
        
        # Microphone capsule (rounded rectangle)
        mic_color = gradient_start
        draw.rounded_rectangle(
            [mic_x, mic_y, mic_x + mic_width, mic_y + mic_height],
            radius=20,
            fill=mic_color,
            outline=gradient_mid,
            width=2
        )
        
        # Microphone stand
        stand_x = center_x
        stand_y = mic_y + mic_height
        draw.line([stand_x - 5, stand_y, stand_x - 5, stand_y + 30], 
                  fill=gradient_mid, width=3)
        draw.line([stand_x + 5, stand_y, stand_x + 5, stand_y + 30], 
                  fill=gradient_mid, width=3)
        draw.line([stand_x - 20, stand_y + 30, stand_x + 20, stand_y + 30], 
                  fill=gradient_mid, width=4)
        
        # Animated sound waves (left)
        for i in range(3):
            wave_progress = (progress + i * 0.2) % 1
            if wave_progress < 0.6:  # Only show wave for part of cycle
                opacity = int(255 * (1 - wave_progress / 0.6))
                offset = -50 - i * 20 - wave_progress * 30
                wave_height = 15 + i * 10
                
                wave_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                wave_draw = ImageDraw.Draw(wave_img)
                
                wave_draw.arc(
                    [center_x + offset - 5, center_y - wave_height,
                     center_x + offset + 5, center_y + wave_height],
                    start=270, end=90,
                    fill=(*gradient_end, opacity),
                    width=3
                )
                img = Image.alpha_composite(img.convert('RGBA'), wave_img)
                img = img.convert('RGB')
        
        # Animated sound waves (right)
        for i in range(3):
            wave_progress = (progress + i * 0.2) % 1
            if wave_progress < 0.6:
                opacity = int(255 * (1 - wave_progress / 0.6))
                offset = 50 + i * 20 + wave_progress * 30
                wave_height = 15 + i * 10
                
                wave_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                wave_draw = ImageDraw.Draw(wave_img)
                
                wave_draw.arc(
                    [center_x + offset - 5, center_y - wave_height,
                     center_x + offset + 5, center_y + wave_height],
                    start=90, end=270,
                    fill=(*gradient_end, opacity),
                    width=3
                )
                img = Image.alpha_composite(img.convert('RGBA'), wave_img)
                img = img.convert('RGB')
        
        # Add text with fade effect
        try:
            font_large = ImageFont.truetype("arial.ttf", 48)
            font_small = ImageFont.truetype("arial.ttf", 18)
        except:
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # Main title
        title = "SonicFlow AI"
        text_bbox = draw.textbbox((0, 0), title, font=font_large)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = (width - text_width) // 2
        text_y = height - 100
        
        # Text with gradient effect
        text_opacity = int(200 + 55 * math.sin(angle))
        draw.text((text_x, text_y), title, fill=gradient_start, font=font_large)
        
        # Subtitle
        subtitle = "Real-Time Voice Agent"
        sub_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
        sub_width = sub_bbox[2] - sub_bbox[0]
        sub_x = (width - sub_width) // 2
        draw.text((sub_x, text_y + 60), subtitle, fill=(100, 100, 100), font=font_small)
        
        images.append(img)
    
    # Save as GIF
    output_path = 'SonicFlow_AI_Logo.gif'
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=1000//fps,
        loop=0,
        optimize=False
    )
    
    print(f"✅ Logo saved as: {output_path}")
    print(f"   Size: {width}x{height}")
    print(f"   Frames: {frames}")
    print(f"   FPS: {fps}")

if __name__ == "__main__":
    create_sonicflow_logo()
