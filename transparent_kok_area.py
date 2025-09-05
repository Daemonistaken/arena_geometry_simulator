from PIL import Image, ImageDraw
import math

# Load the base image
img_path = "A:/Desktop/anythin/20EECD1.JPG"
base_img = Image.open(img_path).convert("RGBA")


# Dimensions in meters
bridge_width_m = 4
obround_height_m = 7
obround_width_m = 6
dome_radius_m = 2.6

# Get bridge pixel width from the second image (bridge close-up)
bridge_img_path = "A:/Desktop/anythin/bridge_closeup.png"
bridge_img = Image.open(bridge_img_path)
bridge_pixel_width = bridge_img.width

# Compute meters per pixel
m_per_px = bridge_width_m / bridge_pixel_width
px_per_m = 1 / m_per_px

# Convert dimensions to pixels
obround_height_px = int(obround_height_m * px_per_m)
obround_width_px = int(obround_width_m * px_per_m)
dome_radius_px = int(dome_radius_m * px_per_m)

# Create a transparent canvas same size as base image
transparent_canvas = Image.new("RGBA", base_img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(transparent_canvas)

# Positioning: place obround near the center of the bridge in the main image
center_x, center_y = base_img.width // 2, base_img.height // 2

mini_radius_m = 0.5        # small circle radius in meters (default 0.5 m)
gap_from_bottom_m = 1.0    # separation from bottom of obround in meters

mini_r_px = int(mini_radius_m * px_per_m)
gap_px = gap_from_bottom_m * px_per_m

# Redraw obround
r = obround_width_px // 2
straight = obround_height_px - 2 * r
top_y = center_y - obround_height_px // 2

# Top semicircle
draw.pieslice([center_x - r, top_y, center_x + r, top_y + 2*r],
              180, 360, outline="red", width=3)

# Bottom semicircle
bottom_y = top_y + 2*r + straight

draw.pieslice([center_x - r, bottom_y - 2*r, center_x + r, bottom_y],
              0, 180, outline="red", width=3)

# Vertical lines
draw.line([(center_x - r, top_y + r), (center_x - r, bottom_y - r)], fill="red", width=3)
draw.line([(center_x + r, top_y + r), (center_x + r, bottom_y - r)], fill="red", width=3)

# Circle center: horizontally centered, vertically placed gap_from_bottom above bottom edge
mini_cx = center_x
mini_cy = int(bottom_y - gap_px - mini_r_px)

# Draw the mini circle (outline)
draw.ellipse(
    [
        mini_cx - mini_r_px, mini_cy - mini_r_px,
        mini_cx + mini_r_px, mini_cy + mini_r_px
    ],
    outline="cyan",
    width=3
)

'''
# Dome (circle)
draw.ellipse([center_x - dome_radius_px, center_y - dome_radius_px,
              center_x + dome_radius_px, center_y + dome_radius_px],
             outline="yellow", width=3)
'''
'''# Labels + dimensions
draw.text((center_x + obround_width_px//2 + 20, center_y), "Obround", fill="red")
draw.text((center_x + obround_width_px//2 + 20, center_y + 40), "7m x 6m", fill="red")

draw.text((center_x - dome_radius_px - 80, center_y - dome_radius_px - 20), "Dome", fill="yellow")
draw.text((center_x - dome_radius_px - 80, center_y - dome_radius_px - 50), "r = 2.6m", fill="yellow")

draw.text((center_x - 40, center_y + obround_height_px//2 + 40), "Bridge", fill="white")
draw.text((center_x - 40, center_y + obround_height_px//2 + 70), "4m x 4m", fill="white")
'''
# Save as transparent PNG
out_transparent_path = "A:/Desktop/anythin/khora_skana_range7x6_obround_shape2.png"
transparent_canvas.save(out_transparent_path)

out_transparent_path
