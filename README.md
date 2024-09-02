# BYT-KICAD-LIB

Common Kicad symbols and footprints used for Bytendo related projects.

# Credits

The following symbols and footprints are used in this library. All credit goes to the original authors.

* HDR for RP2350 symbols and footprints [link](https://github.com/HDR/RP2350_KiCad)
* Natalie the Nerd for AGB symbols [link](https://github.com/nataliethenerd/AGB_ReverseEngineer)
* Nicolò Carandini for Pico symbol and footprints [link](https://github.com/ncarandini/KiCad-RP-Pico)

***

## How to add the Footprint library to Kicad

### Step 1: Open KiCad and the PCB Editor
1. Launch KiCad.
2. Open the project you're working on.
3. Open the **PCB Editor** by clicking the PCB icon or selecting it from the project window.

### Step 2: Open the Footprint Library Manager
1. In the PCB Editor, go to the top menu and click on **Preferences**.
2. Select **Footprint Library Manager** from the drop-down menu.

### Step 3: Add the Library
1. In the Footprint Library Manager, click on the **Browse Libraries** button (usually on the right side of the window).
2. Navigate to `BytendoMods.pretty`
3. Select the library folder and click **OK**.

### Step 4: Choose the Library Type and Configure
1. After selecting the library, you'll be prompted to choose the **library type**:
   - **Global**: The library will be available for all projects.
   - **Project**: The library will only be available for the current project.
2. Select the appropriate option based on your needs.

### Step 5: Save and Apply
1. Once you've added the library and configured its type, click **OK** or **Apply** to save the changes.
2. The footprint library should now be available in the footprint selection dialogs within KiCad.

***

## How to add the Symbol library to Kicad

### Step 1: Open KiCad and the Schematic Editor
1. Launch KiCad.
2. Open the project you're working on.
3. Open the **Schematic Editor** by clicking the schematic icon or selecting it from the project window.

### Step 2: Open the Symbol Library Manager
1. In the Schematic Editor, go to the top menu and click on **Preferences**.
2. Select **Symbol Library Manager** from the drop-down menu.

### Step 3: Add a New Library
1. In the Symbol Library Manager, click on the **Browse Libraries** button (usually on the right side of the window).
2. Navigate to `Bytendo.kicad_sym`
3. Select the library file and click **OK**.

### Step 4: Choose the Library Type and Configure
1. After selecting the library, you'll be prompted to choose the **library type**:
   - **Global**: The library will be available for all projects.
   - **Project**: The library will only be available for the current project.
2. Select the appropriate option based on your needs.

### Step 5: Save and Apply
1. Once you've added the library and configured its type, click **OK** or **Apply** to save the changes.
2. The new symbol library should now be available in the symbol selection dialogs within KiCad.

### Step 6: Verify the Library Addition
1. Open the **Add Symbol** tool in the Schematic Editor and check if the newly added symbols are available in the library list.
2. You can now place symbols from this library into your schematic.

That’s it!