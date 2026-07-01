import pandas as pd

# This code reads a CSV file that discusses the relationship between the year and video game success. 
# It creates an SVG scatter plot visualization, with year on the x-axis and video games on the y-axis. 
# I made a simple scatter plot with a legend and axis labels. 
# The code uses the pandas library to read the CSV file and utilize the relevant data for plotting.
# I used colors I liked like light blue for the background, pink for the data points, and light green for the legend box.

df = pd.read_csv('simplelinearregression.csv')

df_filtered = df.head(25)

# SVG canvas dimensions and padding
Width = 800
Height = 600
Padding = 100

# x and y ranges for the scatter plot
x_min, x_max = 15, 35
y_min, y_max = 5000, 30000

svg_lines = [
    f'<svg width="{Width}" height="{Height}" xmlns="http://www.w3.org/2000/svg" style="background-color: lightblue;">'
]

svg_lines.append(f' <text x="{Width/2}" y="{Padding/2}" font-family="Sans Serif" text-anchor="middle" font-size="32" font-weight="bold" fill="black">Insurance Premium vs. Age!</text>')

#x-axis line
svg_lines.append(f' <line x1="{Padding}" y1="{Height-Padding}" x2="{Width-Padding}" y2="{Height-Padding}" stroke="black" stroke-width="2"/>')

#y-axis line
svg_lines.append(f' <line x1="{Padding}" y1="{Padding}" x2="{Padding}" y2="{Height-Padding}" stroke="black" stroke-width="2"/>')

# x-axis labels
svg_lines.append(f' <text x="{Width/2}" y="{Height - Padding + 40}" font-family="Sans Serif" text-anchor="middle" font-size="16" fill="black">Age (Years)</text>')  
# y-axis labels
svg_lines.append(f' <text x="{Padding - 60}" y="{Height/2}" font-family="Sans Serif" text-anchor="middle" font-size="16" fill="black" transform="rotate(-90 {Padding - 60},{Height/2})">Premium ($)</text>')

# draw value marks and labels for x-axis and y-axis
for age_val in range(x_min, x_max + 1, 5):
    tick_x = Padding + ((age_val - x_min) / (x_max - x_min)) * (Width - 2 * Padding)
    svg_lines.append(f' <line x1="{tick_x}" y1="{Height-Padding}" x2="{tick_x}" y2="{Height-Padding + 6}" stroke="black" stroke-width="1.5"/>')
    svg_lines.append(f' <text x="{tick_x}" y="{Height-Padding + 22}" font-family="Sans Serif" text-anchor="middle" font-size="11" fill="black">{age_val}</text>')

# draw value marks and labels for y-axis
for prem_val in range(y_min, y_max + 1, 5000):
    tick_y = (Height - Padding) - ((prem_val - y_min) / (y_max - y_min)) * (Height - 2 * Padding)
    svg_lines.append(f' <line x1="{Padding-6}" y1="{tick_y}" x2="{Padding}" y2="{tick_y}" stroke="black" stroke-width="1.5"/>')
    svg_lines.append(f' <text x="{Padding - 12}" y="{tick_y + 4}" font-family="Sans Serif" text-anchor="end" font-size="11" fill="black">{prem_val}</text>')

#4. map feature values to visual primitives (circles)
for _, row in df_filtered.iterrows():
    age = row['Age']
    premium = row['Premium']

    cx = Padding + ((age - x_min) / (x_max - x_min)) * (Width - 2 * Padding)
    cy = (Height - Padding) - ((premium - y_min) / (y_max - y_min)) * (Height - 2 * Padding)

    svg_lines.append(f' <circle cx="{cx}" cy="{cy}" r="5" fill="pink" opacity="0.7" stroke="black" stroke-width="1.5"/>')
    svg_lines.append(f' <text x="{cx + 10}" y="{cy + 4}" font="Roboto" font-size="11" fill="black">{age}, {premium}</text>')  

#legend
svg_lines.append(f' <rect x="{Width - Padding - 130}" y="{Height-Padding-70}" width="140" height="60" fill="lightgreen" stroke="black" stroke-width="1.5" rx="4"/>')
svg_lines.append(f' <circle cx="{Width - Padding - 119}" cy="{Height-Padding-35}" r="5" fill="pink" opacity="0.7" stroke="black" stroke-width="1.5"/>')
svg_lines.append(f' <text x="{Width - Padding - 110}" y="{Height-Padding-35}" font-family="Sans Serif" font-size="12" fill="black">Age, Premium Costs</text>')

svg_lines.append('</svg>')

if __name__ == "__main__":
    f = open('videogames.svg', 'w')
    f.write('\n'.join(svg_lines))
    f.close()
    # print test code for VS code that lets you know the SVG file has been updated and created successfully
    print("SVG file 'videogames.svg' has been created successfully.")
