#! /usr/bin/env python3

# Paste your ASCII-Art between the triple quotes
ascii_art = r"""
                                   +       +
                     ++            ++     ++            ++
                ++++++             +++++++++             ++++++
             +++++++++            +++++++++++            +++++++++
          ++++++++++++            +++++++++++            ++++++++++++
        ++++++++++++++           +++++++++++++           +++++++++++++++
      ++++++++++++++++++        +++++++++++++++        ++++++++++++++++++
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     +++++++++++        ++++     +++++++++++++     ++++        +++++++++++
       ++++++++           +        +++++++++        +           ++++++++
         +++++++                     +++++                     +++++++
             ++++                     +++                      +++
                                       +

          ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐   ╔╦╗┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔╗ ┬─┐┬ ┬┌─┐┌─┐┬
          ║║║├┤ │  │  │ ││││├┤    ║║║├─┤└─┐ │ ├┤ ├┬┘  ╠╩╗├┬┘│ ││  ├┤ │
          ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘┘  ╩ ╩┴ ┴└─┘ ┴ └─┘┴└─  ╚═╝┴└─└─┘└─┘└─┘o
"""

# Rest of theme details
theme_header = r"""
title-text: ""
title-color: "#55ff55"
desktop-color: "#000000"
terminal-left: "0%"
terminal-top: "0%"
terminal-width: "100%"
terminal-height: "100%"

+ boot_menu {
    left = 25%
    width = 50%
    top = 90%
    height = 8%
    item_color = "#fff777"
    selected_item_color = "#ffffff"
    item_height = 15
    item_padding = 0
    item_spacing = 0
    scrollbar_width = 0
}

+ vbox {
  left = 0
  width = 100%
  top = 0
  height = 300
"""

# Define the output file name
output_file = "theme.txt"

# Open the file in write mode and process each line of the ASCII art
with open(output_file, "w") as file:
    file.write(f'{theme_header}')
    for line in ascii_art.split("\n"):
        if line.strip():  # Skip empty lines
            # Write the formatted label text to the file
            file.write(f'  + label {{\n    text = "{line}"\n    font = "Terminus-32"\n    color = "#fff000"\n  }}\n')
    file.write("}")
