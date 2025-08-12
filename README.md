# Eta Oscillators Visualization Repository

This repository contains Python scripts using Manim to visualize properties related to the partial eta function and its oscillators.

## Scripts

- **EtaOscillatorsStatic.py**  
  Generates a static snapshot of the odd and even branches for given parameters \(N\), \(\sigma\), and \(t\).

- **EtaOscillatorsDynamic.py**  
  For given \(N\) and \(\sigma\), generates a video showing the oscillators' branches moving over time \(t\).  
  Additionally, it dynamically plots the magnitude of the "partial eta function" versus time \(t\) alongside the animation.  
  It also produces a separate static image of this magnitude plot.

- **EtaMagnitudeVsSigmaPlot.py**  
  For a given \(N\), generates a dynamic video of the magnitude of the "partial eta function" versus \(\sigma\) as time \(t\) advances.  
  This visualizes how the non-trivial zeros are dynamically formed.  
  The script also outputs a `.csv` file containing the detected zeros' locations — specifically, the \(\sigma\) and \(t\) values that nullify the function, generating a local minimum.

## Output Locations

- Images are saved to:  
  `./media/images/script_name`

- Videos are saved to:  
  `./media/videos/script_name`

- The CSV output from `EtaMagnitudeVsSigmaPlot.py` is saved to:  
  `./media/text_output/script_name`

---

Feel free to explore and modify the scripts for further analysis or visualization improvements.
