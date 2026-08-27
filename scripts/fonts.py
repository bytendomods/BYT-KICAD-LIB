import pcbnew

# Load the currently opened board
board = pcbnew.GetBoard()

# Target font size in mm (converted to internal units - nanometers)
target_height_mm = 0.75
target_width_mm = 0.75
target_thickness_mm = 0.15
target_height_nm = pcbnew.FromMM(target_height_mm)
target_width_nm = pcbnew.FromMM(target_width_mm)
target_thickness_nm = pcbnew.FromMM(target_thickness_mm)

# Iterate over all footprints
for footprint in board.GetFootprints():
    ref = footprint.Reference()
    if ref:
        ref.SetTextHeight(target_height_nm)
        ref.SetTextWidth(target_width_nm)
        ref.SetTextThickness(target_thickness_nm)

# Refresh the board view (only needed in GUI)
pcbnew.Refresh()

print(f"Set all reference designator font sizes to {target_height_mm} mm.")
