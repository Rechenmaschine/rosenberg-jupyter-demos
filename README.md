# rosenberg-jupyter-demos

Interactive Jupyter notebooks for teaching engineering concepts.

## Notebooks

| Notebook | Topic | Launch |
|---|---|---|
| [`filters.ipynb`](filters.ipynb) | Smoothing filters: EMA vs SMA vs Kalman | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Rechenmaschine/rosenberg-jupyter-demos/main?urlpath=%2Fnotebooks%2Ffilters.ipynb) |
| [`arduino_filters.ipynb`](arduino_filters.ipynb) | Write SMA / EMA in C, compile with gcc, plot the output, paste into Arduino | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Rechenmaschine/rosenberg-jupyter-demos/main?urlpath=%2Fnotebooks%2Farduino_filters.ipynb) |

## Run locally

```bash
pip install -r requirements.txt
jupyter notebook filters.ipynb
```

## Run on Binder

Click the badge above. Binder will build the environment from `requirements.txt`
and `runtime.txt` and open the notebook directly.
