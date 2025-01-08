#import packages
from statsbombpy import sb
import pandas as pd
from mplsoccer import VerticalPitch,Pitch
from highlight_text import ax_text, fig_text
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import seaborn as sns

#call statsbombpy API to get all free competitions
free_comps = sb.competitions()

#print a list of free competitions
# free_comps
season_sorted = free_comps.sort_values(by='season_name', ascending = False)
season_sorted

#call the statsbombpy API to get a list of matches for a given competition
#Euro 2024 competition id, season id
#competition_id=55, season_id=282
# euro_2024_matches = sb.matches(competition_id=55, season_id=282)
copaamerica_2024_matches = sb.matches(competition_id=223, season_id=282)

#print the first 5 matches listed
# euro_2024_matches.head(5)
copaamerica_2024_matches.head(5)

